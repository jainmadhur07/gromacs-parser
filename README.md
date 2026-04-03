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

## Sample Output

### parse_rtp.py — residues["ALA"]
```python
{
  'atoms': {
    'N':   {'type': 'N',  'charge': -0.4157},
    'H':   {'type': 'H',  'charge':  0.2719},
    'CA':  {'type': 'CX', 'charge':  0.0337},
    'HA':  {'type': 'H1', 'charge':  0.0823},
    'CB':  {'type': 'CT', 'charge': -0.1825},
    'HB1': {'type': 'HC', 'charge':  0.0603},
    'HB2': {'type': 'HC', 'charge':  0.0603},
    'HB3': {'type': 'HC', 'charge':  0.0603},
    'C':   {'type': 'C',  'charge':  0.5973},
    'O':   {'type': 'O',  'charge': -0.5679}
  },
  'bonds': [
    ('N','H'), ('N','CA'), ('CA','HA'), ('CA','CB'),
    ('CA','C'), ('CB','HB1'), ('CB','HB2'), ('CB','HB3'),
    ('C','O'), ('-C','N')
  ]
}
```

### parse_itp.py — atom_types["C"] and atom_types["N"]
```python
{'mass': 12.01, 'sigma': 0.339967, 'epsilon': 0.359824}  # C
{'mass': 14.01, 'sigma': 0.325,    'epsilon': 0.71128}   # N
```

### link.py — first 3 atoms from 1BRS.pdb
```python
{'atom_name': 'N',  'res_name': 'VAL', 'chain': 'A', 'coordinate': [16.783, 48.812, 26.447], 'atom_type': 'N',  'charge': -0.4157, 'mass': 14.01}
{'atom_name': 'CA', 'res_name': 'VAL', 'chain': 'A', 'coordinate': [17.591, 48.101, 25.416], 'atom_type': 'CX', 'charge': -0.0875, 'mass': 12.01}
{'atom_name': 'C',  'res_name': 'VAL', 'chain': 'A', 'coordinate': [16.643, 47.160, 24.676], 'atom_type': 'C',  'charge':  0.5973, 'mass': 12.01}
```
