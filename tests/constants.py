from os import path

MKDIR = "mkdir"
WD = "/tmp"

EX_OK = 0
EX_FAIL = 1

ILLEGAL_CHARS = [".", ".."]


class DirNames:
    """
    Names of the test directories
    """

    DIR_NAME = "test"
    DIR_NAME1 = "test1"
    DIR_NAME2 = "test2"
    DIR_NAME3 = "test3"
    DIR_NAME4 = "test4"
    DIR_NAME_ON_LIMIT = "a" * 255
    DIR_NAME_TOO_LONG = "a" * 256
    DIR_NAME_WAY_TOO_LONG = "a" * 5000
    DIR_NAMES = [DIR_NAME, DIR_NAME1, DIR_NAME2, DIR_NAME3, DIR_NAME4]


class DirPaths:
    """
    Paths to test directories
    - without nesting
    - with nesting (3 level deep)
    """

    DIR_PATH = path.join(WD, DirNames.DIR_NAME)
    DIR_PATH1 = path.join(WD, DirNames.DIR_NAME1)
    DIR_PATH2 = path.join(WD, DirNames.DIR_NAME2)
    DIR_PATH3 = path.join(WD, DirNames.DIR_NAME3)
    DIR_PATH4 = path.join(WD, DirNames.DIR_NAME4)
    DIR_PATH_ON_LIMIT = path.join(WD, DirNames.DIR_NAME_ON_LIMIT)
    DIR_PATH_TOO_LONG = path.join(WD, DirNames.DIR_NAME_TOO_LONG)
    NON_NESTED_DIRS = [DIR_PATH, DIR_PATH1, DIR_PATH2, DIR_PATH3, DIR_PATH4, DIR_PATH_ON_LIMIT, DIR_PATH_TOO_LONG]

    # Absolute paths to the directories to be created, e.g., /tmp/test1/test
    NESTED_DIR_PATH1 = path.join(WD, DirNames.DIR_NAME1, DirNames.DIR_NAME)
    NESTED_DIR_PATH2 = path.join(WD, DirNames.DIR_NAME2, DirNames.DIR_NAME)
    NESTED_DIR_PATH3 = path.join(WD, DirNames.DIR_NAME3, DirNames.DIR_NAME)
    NESTED_DIRS = [NESTED_DIR_PATH1, NESTED_DIR_PATH2, NESTED_DIR_PATH3]


class Params:
    PARENTS_SHORT = "-p"
    PARENTS_LONG = "--parents"
    PARENTS_VARIANTS = [PARENTS_SHORT, PARENTS_LONG]

    VERBOSE_SHORT = "-v"
    VERBOSE_LONG = "--verbose"
    HELP = "--help"
    VERSION = "--version"
