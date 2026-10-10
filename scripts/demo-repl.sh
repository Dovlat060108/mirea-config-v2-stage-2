#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
printf "ls\ncd /docs\nls a b\nunknown\nexit\n" | sh run.sh
