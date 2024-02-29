import unittest
from unittest.mock import patch

import python_verification.parseArgs

class MyTestCase(unittest.TestCase):

    @patch('python_verification.parseArgs.parse_args')
    def test_should_accept_passing_report(self, parse_args_mock):
        python_verification.parseArgs.inspect_report()
        parse_args_mock.assert_called_once()

    def test_should_reject_failing_report(self):
        python_verification.parseArgs.inspect_report()
        self.assertEqual(True, False)  # add assertion here

    def test_should_reject_old_report(self):
        python_verification.parseArgs.inspect_report()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
