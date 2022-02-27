import os
import sys
import textwrap
import time
import unittest

import warnings

def show_warn(message, category, filename, lineno, file=None):
    """Hook to write a warning to a file; replace if you like."""
    if file is None:
        file = sys.stderr
        try:
            message = "%s: %s" % (category.__name__, message)
            for line in textwrap.wrap(message):
                file.write("\n    ")
                file.write(line)
            file.write("\n")
        except IOError:
            pass # the file (probably stderr) is invalid - this warning gets lost.
    else:
        try:
            file.write(formatwarning(message, category, filename, lineno))
        except IOError:
            pass # the file (probably stderr) is invalid - this warning gets lost.

warnings.showwarning = show_warn


def prefer_parent_path():
    # Place this __file__'s grandparent (../../) at the start of sys.path,
    # so that all imports are from this __file__'s package.
    localDir = os.path.dirname(__file__)
    curpath = os.path.normpath(os.path.join(os.getcwd(), localDir))
    grandparent = os.path.normpath(os.path.join(curpath, '../../'))
    if grandparent not in sys.path:
        sys.path.insert(0, grandparent)


class TerseTestResult(unittest._TextTestResult):
    
    def printErrors(self):
        # Overridden to avoid unnecessary empty line
        if self.errors or self.failures:
            if self.dots or self.showAll:
                self.stream.writeln()
            self.printErrorList('ERROR', self.errors)
            self.printErrorList('FAIL', self.failures)


class TerseTestRunner(unittest.TextTestRunner):
    """A test runner class that displays results in textual form."""
    
    def _makeResult(self):
        return TerseTestResult(self.stream, self.descriptions, self.verbosity)
    
    def run(self, test):
        "Run the given test case or test suite."
        # Overridden to remove unnecessary empty lines and separators
        result = self._makeResult()
        startTime = time.time()
        test(result)
        timeTaken = float(time.time() - startTime)
        result.printErrors()
        if not result.wasSuccessful():
            self.stream.write("FAILED (")
            failed, errored = map(len, (result.failures, result.errors))
            if failed:
                self.stream.write("failures=%d" % failed)
            if errored:
                if failed: self.stream.write(", ")
                self.stream.write("errors=%d" % errored)
            self.stream.writeln(")")
        return result

djvTestRunner = TerseTestRunner(verbosity=2)

