#!/usr/bin/env bash

REPORT_PATH=$1
END_PATTERN="end"
START_PATTERN="start"
PASS_PERCENT="passPercent"

get_datetime_from_json(){
#grep -Eo "\"$START_PATTERN\"[^,]*" "$REPORT_PATH" # Extracts a row from the JSON file. Does NOT handle multiple matches, so the key must be unique
# awk -F ': "' '{print $2}'                        # Retrieves the value from the key and strips the leading quote. Does NOT work for numerical responses.
# awk -F 'T' '{print $1}'                          # Retrieves just the day from a date formatted like YYYY-MM-DDTHH:MM:SS.NNNZ
  KEY=$1
  FILE=$2
  grep -Eo "\"$KEY\"[^,]*" "$FILE" | awk -F ': "' '{print $2}' | awk -F 'T' '{print $1}'
}

get_number_from_json(){
  KEY=$1
  FILE=$2
  grep -Eo "\"$KEY\"[^,]*" "$REPORT_PATH" | awk -F ': ' '{print $2}'
}

grep -Eo "\"$START_PATTERN\"[^,]*" "$REPORT_PATH"
START_TIME=$(get_datetime_from_json "$START_PATTERN" "$REPORT_PATH")

grep -Eo "\"$END_PATTERN\"[^,]*" "$REPORT_PATH"

grep -Eo "\"$PASS_PERCENT\"[^,]*" "$REPORT_PATH"
PASS_RESULT=$(get_number_from_json "$PASS_PASS_PERCENT" "$REPORT_PATH")


TODAY=$(date +"%Y-%m-%d")

if [ "$START_TIME" == "$TODAY" ];
then
  echo "Cypress tests were ran today, based upon $REPORT_PATH"
else
  echo "Cypress tests were NOT ran today, based upon $REPORT_PATH."
  echo "Cypress tests were last executed on: $START_TIME"
  exit 1
fi

if [ "$PASS_RESULT" == "100" ];
then
  echo "Cypress tests passed, based upon $REPORT_PATH."
else
  echo "ERROR - Not all the tests passed. Only $PASS_RESULT% passed."
  exit 1
fi
