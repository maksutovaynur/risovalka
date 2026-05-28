"""File location helpers for examples and small student projects."""

from inspect import stack
from pathlib import Path


def get_project_root_folder():
    return Path(__file__).resolve().parents[2]


def get_current_folder():
    caller = stack()[1]
    return Path(caller.filename).resolve().parent
