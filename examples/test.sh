#!/usr/bin/env bash

set -e

log() {
    echo "$(date):" "$@"
}

rm -f output
log "Removed output file."

python example.py >output 2>&1 &
pid=$!
log "Subprocess started. pid=$pid"

sleep 1
mkdir data
log "Created data folder."
sleep 1

echo "1" > data/test
log "Created test file."
sleep 1

echo "2" > data/test
log "Updated test file."
sleep 1

rm -r data
log "Removed data folder."
sleep 1

kill $pid
log "Stopped process."


assert_contains() {
    if ! grep "$1" output >/dev/null 2>&1; then
        log "assertion failed: $1"
        exit 1
    fi
}

assert_contains "Created directory.*/examples/data"
assert_contains "Created file.*/examples/data/test"
assert_contains "Modified file.*/examples/data/test"
assert_contains "Deleted file.*/examples/data/test"
assert_contains "Deleted directory.*/examples/data"
