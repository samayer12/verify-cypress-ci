# Verify Cypress Test Results without CI/CD Support

This repo provides a proof-of-concept for how you can verify that your team ran cypress tests locally within a CI/CD pipeline that does not support Cypress.

Sometimes you do not have access to Cypress in your CI/CD environment.
Cypress tests are still useful, but only if you execute them and look at the results.

This repo does not assume access to `jq`.

## Getting Started

Run `./test/test-verify-cypress.sh` if you're making changes to the script.
The `test/data` directory contains example test reports.

## TODO

* Fix sad-path test by inspecting messages returned in log
* Auto-commit `output.json` as part of a git hook?
* Can we also assert no skipped tests or something like that?
* Consider doing time comparisons with epoch instead of strings
* More robust date checks in `verify-cypress.sh`
