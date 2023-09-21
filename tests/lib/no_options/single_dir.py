from unittest import TestCase

from constants import EX_FAIL, EX_OK, ILLEGAL_CHARS, MKDIR, DirPaths
from lib.cmd_runner import run_cmd
from lib.utils import after_test_check, before_test_check, check_dir_exist


class CreateSingleDirNoParams(TestCase):
    """
    A set of tests for creating a single directory without nesting and without any parameters to the 'mkdir' command.

    This test class checks the behavior of the 'mkdir' command when attempting to create a single directory
    without any nesting and without specifying any parameters. It verifies various scenarios, such as creating a
    single directory, creating a duplicate directory, creating multiple non-nested directories, and attempting to
    create directories with illegal characters in their names.
    """

    def setUp(self) -> None:
        """
        Runs before all the tests in the class.
        """
        before_test_check(self)

    def test_no_params_single_arg(self) -> None:
        """
        Test creating a single directory in a working directory.

        This test should successfully create a directory.
        """
        returncode = run_cmd("Test SINGLE dir creation without any parameters", EX_OK, self, DirPaths.DIR_PATH)
        self.assertTrue(
            check_dir_exist(DirPaths.DIR_PATH),
            msg=(
                f"'{MKDIR}' command returned exit code "
                f"'{returncode}', but the directory '{DirPaths.DIR_PATH}' does not exist."
            ),
        )

    def test_no_params_duplicit(self):
        """
        Test creating a regular single directory and then try to create the same directory again.
        """
        returncode = run_cmd("Test duplicit dir creation - create first directory", EX_OK, self, DirPaths.DIR_PATH4)
        self.assertTrue(
            check_dir_exist(DirPaths.DIR_PATH4),
            msg=(
                f"'{MKDIR}' command returned exit code "
                f"'{returncode}', but the directory '{DirPaths.DIR_PATH4}' does exist."
            ),
        )
        returncode = run_cmd(
            "Test duplicit dir creation - create the previously created directory again",
            EX_FAIL,
            self,
            DirPaths.DIR_PATH4,
        )

    def test_no_params_many_args(self) -> None:
        """
        Test creating many non-nested directories.
        """
        returncode = run_cmd(
            "Test many non-nested directories creation without any parameters",
            EX_OK,
            self,
            DirPaths.DIR_PATH1,
            DirPaths.DIR_PATH2,
            DirPaths.DIR_PATH3,
        )
        for dir in [DirPaths.DIR_PATH1, DirPaths.DIR_PATH2, DirPaths.DIR_PATH3]:
            self.assertTrue(
                check_dir_exist(dir),
                msg=(f"'{MKDIR}' command returned exit code " f"'{returncode}', but the directory '{dir}' does exist."),
            )

    def test_no_params_ill_chars(self) -> None:
        """
        Test creating single directories with illegal characters as names.
        """
        for char in ILLEGAL_CHARS:
            run_cmd("Test creating single directories with illegal characters as names", EX_FAIL, self, char)

    def test_no_params_long_names(self) -> None:
        """
        Test creating single directories with a name that is unexpectedly long.
        """
        run_cmd(
            "Test creating single directory which name is of maximum possible length.",
            EX_OK,
            self,
            DirPaths.DIR_PATH_ON_LIMIT,
        )
        run_cmd(
            "Test creating single directory with a name that is too long.", EX_FAIL, self, DirPaths.DIR_PATH_TOO_LONG
        )

    def tearDown(self) -> None:
        """
        Delete directories created during the tests.
        """
        after_test_check()
