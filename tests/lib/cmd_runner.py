import subprocess
from unittest import TestCase

from constants import MKDIR
from lib.utils import construct_exit_code_msg


def run_cmd(test_desc: str, exp_rc: int, test_case: TestCase, *args: str) -> int:
    """
    Run a command and perform an assertion on its return code.

    Args:
        test_desc (str): A short description of the test.
        exp_rc (int): The expected return code that should be returned by the `mkdir` command.
        test_case (TestCase): The `TestCase` instance from the class running the test.
        *args: Variable-length arguments that are passed to the `mkdir` command.

    Returns:
        Return code for a given run

    This function constructs and executes a command using the provided arguments. It captures the return code,
    compares it to the expected return code, and raises an assertion error if they do not match, along with a
    descriptive message.
    """
    cmd = [MKDIR] + list(args)
    result = subprocess.run(args=cmd, capture_output=True)
    test_case.assertEqual(
        first=result.returncode,
        second=exp_rc,
        msg=construct_exit_code_msg(
            msg=test_desc,
            cmd=cmd,
            expected=exp_rc,
            actual=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
        ),
    )
    return result.returncode
