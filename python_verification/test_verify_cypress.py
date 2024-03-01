import unittest

import python_verification.verify_cypress


class VerificationTests(unittest.TestCase):

    def test_should_accept_passing_report(self):
        self.assertTrue(python_verification.verify_cypress.inspect_report(['python_verification/test/data/good-output'
                                                                           '.json']))

    def test_should_reject_failing_report(self):
        self.assertRaises(ValueError, python_verification.verify_cypress.inspect_report,
                          ['python_verification/test/data/failing-test-output.json'])

    def test_should_reject_old_report(self):
        self.assertRaises(ValueError, python_verification.verify_cypress.inspect_report,
                          ['python_verification/test/data/old-test-output.json'])


if __name__ == '__main__':
    unittest.main()
