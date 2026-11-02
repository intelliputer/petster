#!/usr/bin/env sh
# Verify that every archival ROM representation resolves to petster.bin.
set -eu

cd "$(dirname "$0")/.."

rom='code/petster.bin'
expected_sha256='609d6505297a6365abb4fdbd869a2d76aad65ebd2accc628e37023a11ffefee9'
archive_member='Petster Deluxe Eprom/Petster Deluxe Eprom (Burnt on a 27c32 eprom).bin'
work_dir=$(mktemp -d)
trap 'rm -rf "$work_dir"' EXIT HUP INT TERM

actual_sha256=$(sha256sum "$rom" | awk '{print $1}')
test "$actual_sha256" = "$expected_sha256"
test "$(wc -c < "$rom" | tr -d ' ')" = '4096'

unzip -p code/PetsterDeluxeEprom.zip "$archive_member" > "$work_dir/from-archive.bin"
cmp -s "$rom" "$work_dir/from-archive.bin"

objcopy -I ihex -O binary code/petster.hex "$work_dir/from-hex.bin"
cmp -s "$rom" "$work_dir/from-hex.bin"

printf '%s\n' 'ROM verification passed: binary, ZIP payload, and Intel HEX agree.'
