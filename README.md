# Verify Cypress Test Results without CI/CD Support

This repo provides a proof-of-concept for how you can verify that your team ran cypress tests locally within a CI/CD pipeline that does not support Cypress.

Sometimes you do not have access to Cypress in your CI/CD environment.
Cypress tests are still useful, but only if you execute them and look at the results.

This repo does not assume access to `jq`.

## Getting Started

### Shell

Run `./shell/test/test-verify-cypress.sh` if you're making changes to the script.
The `shell/test/data` directory contains example test reports.

### Python

Run `yarn test && cp cypress/report/output.json python_verification/test/data/good-output.json` to generate an updated test report for automated tests.
Run `python python_verification/test_verify_cypress.py` from project root.
The `pytyhon_verification/test/data` directory contains example test reports.

## TODO

### General

* Auto-commit `output.json` as part of a git hook?
* Should we also assert no skipped tests?

### Python

* Resolve `ResourceWarning` in python tests
 
### Shell
* More robust date checks in `verify-cypress.sh`. Such as time comparisons with epoch instead of strings.
* Fix sad-path test by inspecting messages returned in log for shell tests
