from unittest import TestCase
from constants import DirPaths
from os import path
import shutil


def check_dir_exist(*args) -> bool:
    """
    Check whether a directory exists at the specified path.

    Args:
        *args: Variable-length arguments that represent the path components.

    Returns:
        bool: True if the directory exists, False otherwise.

    This function constructs an absolute path from the provided path components using `os.path.join`
    and checks if a directory exists at that path. It returns True if the directory exists, and False
    otherwise.
    """
    absolute_path = path.join(*args)
    return path.isdir(absolute_path)

def before_test_check(self: TestCase) -> None:
    """
    Check for directories which should not exist prior to a test run.
        - e.g., /tmp/test1, /tmp/test2
    """
    for abs_path in DirPaths.NON_NESTED_DIRS:
        if check_dir_exist(abs_path):
            self.fail(f"Directory which should not exist is present on the system: '{abs_path}'")

def after_test_check() -> None:
    """
    Check that there are no directories left after a test run.
    """
    for abs_path in DirPaths.NON_NESTED_DIRS:
        if path.exists(abs_path):
            shutil.rmtree(abs_path)

def construct_exit_code_msg(
        msg: str,
        cmd: list[str],
        expected: int,
        actual: int,
        stdout: bytes,
        stderr: bytes) -> str:
    """
    Construct an exit code message for assertion errors.

    Args:
        msg (str): A description of the assertion error.
        expected (int): The expected exit code.
        actual (int): The actual exit code.

    Returns:
        str: A formatted message for assertion errors.

    This function takes a message, an expected exit code, and an actual exit code and constructs
    a descriptive message for assertion errors. It includes the provided message along with
    a comparison of the expected and actual exit codes.
    """
    return  (
        f"\n{msg}\n"
        "Command:\n"
        f"{' '.join(cmd)}\n"
        "Returned exit code not equal to expected.\n"
        f"Expected: {expected}\n"
        f"Got: {actual}\n"
        f"Captured stdout:\n"
        "=====\n"
        f"{str(stdout)}\n"
        "=====\n"
        f"Captured stderr:\n"
        "=====\n"
        f"{str(stderr)}\n"
        "====="
    )