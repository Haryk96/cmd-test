from unittest import TextTestResult
from typing import TextIO


class ModifiedTestResult(TextTestResult):
    def __init__(self, stream: TextIO, descriptions: bool, verbosity: int):
        super().__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.verbosity = verbosity

    def addSuccess(self, test):
        super(TextTestResult, self).addSuccess(test)
        if self.showAll:
            self._write_status(test, "[PASS]")
        elif self.dots:
            self.stream.write(".")
            self.stream.flush()

    def addFailure(self, test, err):
        super(TextTestResult, self).addFailure(test, err)
        if self.showAll:
            self._write_status(test, "[FAIL]")
        elif self.dots:
            self.stream.write("F")
            self.stream.flush()
