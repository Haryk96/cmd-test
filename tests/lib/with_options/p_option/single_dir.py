from os import rmdir
from unittest import TestCase

from constants import EX_OK, MKDIR, DirPaths, Params
from lib.cmd_runner import run_cmd
from lib.utils import after_test_check, before_test_check, check_dir_exist


class CreateSingleDirParentsOption(TestCase):
    """
    A set of tests for creating a single directory without nesting and with a `-p` parameter.

    This test class checks the behavior of the 'mkdir' command when attempting to create a single directory
    without any nesting and with specifying a `-p` parameter. It verifies various scenarios, such as creating a
    single directory, creating a duplicate directory, creating multiple non-nested directories, and attempting to
    create directories with illegal characters in their names.
    """

    def setUp(self) -> None:
        """
        Runs before all the tests in the class.
        """
        before_test_check(self)

    def test_p_param_single_arg(self) -> None:
        """
        Test creating a single directory in a working directory.
        This test should successfully create a directory.
        - test tries both variants of the parameter: `-p`, `--parents`
        """
        for param in Params.PARENTS_VARIANTS:
            returncode = run_cmd(
                "Test SINGLE dir creation with `-p` parameter",
                EX_OK,
                self,
                param,
                DirPaths.DIR_PATH)
            self.assertTrue(
                check_dir_exist(DirPaths.DIR_PATH),
                msg=(
                    f"'{MKDIR}' command returned exit code "
                    f"'{returncode}', but the directory '{DirPaths.DIR_PATH}' does not exist."
                ),
            )
            rmdir(DirPaths.DIR_PATH)

    def test_p_param_many_args(self) -> None:
        """
        Test creating multiple single directories in a working directory.
        This test should successfully create multiple directories.
        - test tries both variants of the parameter: `-p`, `--parents`
        """
        for param in Params.PARENTS_VARIANTS:
            returncode = run_cmd(
                "Test SINGLE dir creation with `-p` parameter",
                EX_OK,
                self,
                param,
                DirPaths.DIR_PATH,
                param,
                DirPaths.DIR_PATH1,
                param,
                DirPaths.DIR_PATH2,
            )
        for dir in [DirPaths.DIR_PATH, DirPaths.DIR_PATH1, DirPaths.DIR_PATH2]:
            self.assertTrue(
                check_dir_exist(dir),
                msg=(
                    f"'{MKDIR}' command returned exit code "
                    f"'{returncode}', but the directory '{dir}' does not exist."
                ),
            )
            rmdir(dir)

    def tearDown(self) -> None:
        """
        Delete directories created during the tests.
        """
        after_test_check()
