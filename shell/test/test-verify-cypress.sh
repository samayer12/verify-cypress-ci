#!/usr/bin/env bash
echo "Starting tests from $(pwd)"

# Happy Path Tests
touch tests.log
yarn test
cp ./cypress/report/output.json shell/test/data/good-output.json

for TEST_FILE in shell/test/data/good-output.json
do
  echo "" >> tests.log
  if ./shell/verify-cypress.sh $TEST_FILE >> tests.log; then
    echo "PASS - $TEST_FILE"
  else
    echo "FAIL - $TEST_FILE"
 fi
done

# Sad Path Tests
for TEST_FILE in shell/test/data/bad-date-output.json shell/test/data/failing-tests-output.json;
do
  echo "" >> tests.log
  if ! ./shell/verify-cypress.sh $TEST_FILE >> tests.log; then
    echo "PASS - $TEST_FILE"
  else
    echo "FAIL - $TEST_FILE"
  fi
done
