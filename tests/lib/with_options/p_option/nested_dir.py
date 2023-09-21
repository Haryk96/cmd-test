from unittest import TestCase

from constants import EX_FAIL, EX_OK, MKDIR, DirPaths, Params
from lib.cmd_runner import run_cmd
from lib.utils import after_test_check, before_test_check, check_dir_exist


class CreateNestedDirParentsOption(TestCase):
    """
    A set of tests for creating nested directories with the '-p' parameter in the 'mkdir' command.

    This test class checks the behavior of the 'mkdir' command when attempting to create nested directories
    with the '-p' parameter. It verifies that the command should succeed, and the nested directories should be
    created.
    """

    def setUp(self) -> None:
        """
        Runs before all the tests in the class.
        """
        before_test_check(self)

    def test_p_param_nested_single_arg(self) -> None:
        """
        Test creating a single nested directory without `-p` provided to `mkdir` command.

        `mkdir` should return exit code `0` in this case, as it should be able to create nested directories
        with the '-p' parameter.
        - test tries both variants of the parameter: `-p`, `--parents`
        """
        for param in Params.PARENTS_VARIANTS:
            returncode = run_cmd(
                f"Test single NESTED dir creation with '{param}' parameter",
                EX_OK,
                self,
                param,
                DirPaths.NESTED_DIR_PATH1,
            )
            self.assertFalse(
                check_dir_exist(DirPaths.NESTED_DIR_PATH1),
                msg=(
                    f"'{MKDIR}' command returned exit code "
                    f"'{returncode}', but the directory '{DirPaths.NESTED_DIR_PATH1}' does exist."
                ),
            )

    def test_p_param_nested_many_args(self) -> None:
        """
        Test creating multiple nested directories with `-p` parameter provided to `mkdir` command.
        - test tries both variants of the parameter: `-p`, `--parents`
        """
        for param in Params.PARENTS_VARIANTS:
            returncode = run_cmd(
                f"Test many NESTED dir creation with {param} parameter",
                EX_FAIL,
                self,
                param,
                DirPaths.NESTED_DIR_PATH1,
                DirPaths.NESTED_DIR_PATH2,
                DirPaths.NESTED_DIR_PATH3,
            )
            for dir_path in DirPaths.NESTED_DIRS:
                self.assertTrue(
                    check_dir_exist(dir_path),
                    msg=(
                        f"'{MKDIR}' command returned exit code "
                        f"'{returncode}', but the directory '{dir_path}' does not exist."
                    ),
                )

    def tearDown(self) -> None:
        """
        Delete directories created during the tests.
        - only check for the occurrence of the first dir in a nested sequence
        - ie: the test created /tmp/test/test1/test2, then /tmp/test will be deleted
        """
        after_test_check()
