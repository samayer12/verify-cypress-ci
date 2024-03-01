import unittest

import python_verification.parseArgs


class VerificationTests(unittest.TestCase):

    def test_should_accept_passing_report(self):
        self.assertTrue(python_verification.parseArgs.inspect_report(['test/data/good-output.json']))

    def test_should_reject_failing_report(self):
        self.assertRaises(ValueError, python_verification.parseArgs.inspect_report,
                          ['./test/data/failing-test-output.json'])

    def test_should_reject_old_report(self):
        self.assertRaises(ValueError, python_verification.parseArgs.inspect_report,
                          ['test/data/old-test-output.json'])


if __name__ == '__main__':
    unittest.main()
