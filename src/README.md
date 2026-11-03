# Reading the ROM from the working Petster Deluxe

The ROM fitted in the working Petster Deluxe is the authoritative source for
that unit. Do not program, erase, overwrite, or modify its original EPROM.
Use the Barlino II burner only to **read** the device and save independent
copies.

## Before removing the EPROM

1. Power the Petster off and disconnect its batteries or external supply.
2. Photograph the board, EPROM label, notch, and pin-1 orientation before
   removing anything.
3. Note the board revision and every marking visible on the EPROM. The
   expected early-revision device is a 24-pin 27C32-compatible EPROM, but
   select the exact device type shown on the part rather than assuming it.
4. Use an IC extractor; do not lever against nearby components or bend pins.

## Read with the Barlino II

1. Insert the EPROM in the Barlino II socket or its appropriate adapter with
   pin 1 aligned to the programmer's pin-1 mark.
2. In the Barlino II software, select the exact EPROM part number if it is
   available; otherwise use the confirmed compatible 27C32 device type.
3. Perform a **read** operation only and save it as
   `src/petster-deluxe-original-read-1.bin`.
4. Remove and reseat the EPROM, then read it again in a separate operation as
   `src/petster-deluxe-original-read-2.bin`.
5. Do not proceed with any programming, blank-check, erase, or auto-program
   operation.

## Verify the reads

Run these commands from the repository root:

```sh
sha256sum src/petster-deluxe-original-read-1.bin \
          src/petster-deluxe-original-read-2.bin \
          code/petster.bin
cmp -s src/petster-deluxe-original-read-1.bin \
       src/petster-deluxe-original-read-2.bin
```

The two new reads must be byte-for-byte identical. Then compare either one
with the repository baseline:

```sh
cmp -s src/petster-deluxe-original-read-1.bin code/petster.bin
echo $?
```

An exit status of `0` means the physical ROM matches the preserved baseline,
whose SHA-256 is:

```text
609d6505297a6365abb4fdbd869a2d76aad65ebd2accc628e37023a11ffefee9
```

If the two physical reads differ, stop and repeat the read process; do not
assume either result is correct. If they agree but differ from `code/petster.bin`,
keep both the new image and its hash as a separate, documented ROM revision.

## Reinstall

With power still removed, reinstall the original EPROM in the same orientation
recorded in the photographs. Verify that all pins enter the socket cleanly and
that the notch and pin-1 orientation match the board before powering the
Petster again.
