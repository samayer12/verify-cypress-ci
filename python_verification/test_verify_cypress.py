import unittest

from verify_cypress import inspect_report


class VerificationTests(unittest.TestCase):

    def test_should_accept_passing_report(self):
        self.assertTrue(inspect_report(['python_verification/test/data/good-output'
                                        '.json']))

    def test_should_reject_failing_report(self):
        self.assertRaises(ValueError, inspect_report,
                          ['python_verification/test/data/failing-test-output.json'])

    def test_should_reject_old_report(self):
        self.assertRaises(ValueError, inspect_report,
                          ['python_verification/test/data/old-test-output.json'])


if __name__ == '__main__':
    unittest.main()
