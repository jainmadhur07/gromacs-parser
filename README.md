# gromacs-parser

A Python tool to parse GROMACS force field files and PDB structures,
and link atomic parameters for use in LAMMPS simulations.

## What it does

- Parses GROMACS residue topology files (`.rtp`) to extract atom types
  and partial charges for each residue
- Parses GROMACS non-bonded parameter files (`ffnonbonded.itp`) to extract
  mass, sigma, and epsilon for each atom type
- Parses PDB structure files using BioPython to extract atom positions
- Links all three sources together so each atom has its coordinates,
  atom type, charge, and mass in one place

## Files

- `parse_rtp.py` — parses aminoacids.rtp into a residues dictionary
- `parse_itp.py` — parses ffnonbonded.itp into an atom_types dictionary
- `link.py` — combines PDB structure with force field parameters

## Dependencies

- Python 3.x
- BioPython

Install BioPython with:
pip install biopython

## Usage

Place your .pdb, .rtp, and .itp files in the same directory and run:
python link.py
