from parse_rtp import residues
from parse_itp import atom_types
import os
from Bio.PDB import PDBParser

pdb_file="1BRS.pdb"
if os.path.exists(pdb_file):
    parser=PDBParser(PERMISSIVE=True)
    structure=parser.get_structure("1BRS",pdb_file)
    atoms=[]

    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.resname=="HOH":
                    continue
                for atom in residue:
                    atom_name=atom.get_name()
                    res_name=residue.resname
                    chain_id=chain.id
                    coords=atom.get_coord()

                    atoms.append({
                        "atom_name":atom_name,
                        "res_name":res_name,
                        "chain":chain_id,
                        "coordinate": [round(float(x), 3) for x in coords]
                    })

    for atom in atoms:
        res_name=atom["res_name"]
        atom_name=atom["atom_name"]
        try:
            atom_type=residues[res_name]["atoms"][atom_name]["type"]
            charge=residues[res_name]["atoms"][atom_name]["charge"]
            mass=atom_types[atom_type]["mass"]

            atom["atom_type"]=atom_type
            atom["charge"]=charge
            atom["mass"]=mass
        except KeyError:
            atom["atom_type"] = None
            atom["charge"]    = None
            atom["mass"]      = None

    for atom in atoms[:3]:
        print(atom)
        