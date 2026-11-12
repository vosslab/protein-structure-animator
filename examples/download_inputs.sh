#!/usr/bin/env bash
# Retrieve public structural sources; original mmCIF files stay in output/inputs.
set -euo pipefail
mkdir -p output/inputs
curl --fail --location --proto '=https' https://files.rcsb.org/download/3O80.cif -o output/inputs/3o80.cif
curl --fail --location --proto '=https' https://files.rcsb.org/download/3O8M.cif -o output/inputs/3o8m.cif
curl --fail --location --proto '=https' https://files.rcsb.org/download/3N0G.cif -o output/inputs/3n0g.cif
curl --fail --location --proto '=https' https://files.rcsb.org/download/1OEL.cif -o output/inputs/1oel.cif
curl --fail --location --proto '=https' https://files.rcsb.org/download/1OEL-assembly1.cif -o output/inputs/1oel_assembly1.cif
curl --fail --location --proto '=https' https://files.rcsb.org/download/8DBU.cif -o output/inputs/8dbu.cif
curl --fail --location --proto '=https' https://files.rcsb.org/download/8DBU-assembly1.cif -o output/inputs/8dbu_assembly1.cif
shasum -a 256 -c examples/input_hashes.sha256
