#!/usr/bin/env bash
echo "Starting tests from $(pwd)"

# Happy Path Tests
touch tests.log
yarn test
cp ../cypress/report/output.json data/good-output.json

for TEST_FILE in data/good-output.json
do
  echo "" >> tests.log
  if ../verify-cypress.sh $TEST_FILE >> tests.log; then
    echo "PASS - $TEST_FILE"
  else
    echo "FAIL - $TEST_FILE"
 fi
done

# Sad Path Tests
for TEST_FILE in data/bad-date-output.json data/failing-tests-output.json;
do
  echo "" >> tests.log
  if ! ../verify-cypress.sh $TEST_FILE >> tests.log; then
    echo "PASS - $TEST_FILE"
  else
    echo "FAIL - $TEST_FILE"
  fi
done
