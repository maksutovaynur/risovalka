#!/usr/bin/env python3
"""Build lesson PDFs from Marp and Markdown sources."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LESSONS_DIR = ROOT / "lessons"
STYLE_PATH = ROOT / "tools" / "pdf" / "markdown-pdf.css"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert lesson .marp.md and needed .md files into sibling PDFs."
    )
    parser.add_argument(
        "sources",
        nargs="*",
        type=Path,
        help="Optional source files to convert. Defaults to lesson materials.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print files that would be converted without writing PDFs.",
    )
    return parser.parse_args()


def needed_markdown(path: Path) -> bool:
    if path.name.endswith(".marp.md"):
        return False
    if path.name.lower() == "readme.md":
        return False
    if path.parent == LESSONS_DIR:
        return False
    return path.suffix == ".md" and any(part.startswith("lesson") for part in path.parts)


def discover_sources() -> list[Path]:
    marp_sources = sorted(LESSONS_DIR.glob("**/*.marp.md"))
    markdown_sources = sorted(path for path in LESSONS_DIR.glob("**/*.md") if needed_markdown(path))
    return marp_sources + markdown_sources


def output_path(source: Path) -> Path:
    if source.name.endswith(".marp.md"):
        return source.with_name(source.name.removesuffix(".marp.md") + ".pdf")
    return source.with_suffix(".pdf")


def run(command: list[str]) -> None:
    print(" ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def marp_command() -> list[str]:
    marp = shutil.which("marp")
    if marp:
        return [marp]

    npx = shutil.which("npx")
    if npx:
        return [npx, "--yes", "@marp-team/marp-cli"]

    raise RuntimeError("Marp CLI is required. Install `marp` or make `npx` available.")


def chrome_args() -> list[str]:
    chrome = shutil.which("chromium") or shutil.which("chromium-browser")
    chrome = chrome or shutil.which("google-chrome") or shutil.which("google-chrome-stable")

    if not chrome:
        downloaded = sorted(ROOT.glob("chrome/**/chrome-linux64/chrome"), reverse=True)
        if downloaded:
            chrome = str(downloaded[0])

    if not chrome:
        return []

    return ["--browser", "chrome", "--browser-path", chrome]


def build_marp(source: Path, destination: Path) -> None:
    run(
        marp_command()
        + [
            "--allow-local-files",
            "--browser-timeout",
            "120",
            *chrome_args(),
            "--pdf",
            "--output",
            str(destination),
            str(source),
        ]
    )


def build_markdown(source: Path, destination: Path) -> None:
    pandoc = shutil.which("pandoc")
    wkhtmltopdf = shutil.which("wkhtmltopdf")

    if not pandoc:
        raise RuntimeError("pandoc is required to convert Markdown files.")
    if not wkhtmltopdf:
        raise RuntimeError("wkhtmltopdf is required to render Markdown PDFs.")

    with tempfile.TemporaryDirectory(prefix="risovalka-pdf-") as tmp:
        html_path = Path(tmp) / f"{source.stem}.html"
        run(
            [
                pandoc,
                "--from",
                "gfm",
                "--to",
                "html5",
                "--standalone",
                "--metadata",
                f"pagetitle={source.stem}",
                "--css",
                str(STYLE_PATH),
                "--output",
                str(html_path),
                str(source),
            ]
        )
        run(
            [
                wkhtmltopdf,
                "--enable-local-file-access",
                "--print-media-type",
                str(html_path),
                str(destination),
            ]
        )


def main() -> int:
    args = parse_args()
    sources = [path.resolve() for path in args.sources] if args.sources else discover_sources()

    if not sources:
        print("No PDF sources found.")
        return 0

    for source in sources:
        if not source.exists():
            print(f"Missing source: {source}", file=sys.stderr)
            return 1
        destination = output_path(source)
        print(f"{source.relative_to(ROOT)} -> {destination.relative_to(ROOT)}")
        if args.dry_run:
            continue
        if source.name.endswith(".marp.md"):
            build_marp(source, destination)
        else:
            build_markdown(source, destination)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
