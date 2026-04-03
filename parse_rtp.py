sub_sections = {"atoms", "bonds", "impropers", "dihedrals", "exclusions"}

residues = {}
current_residue = None
current_section = None

with open("aminoacids.rtp", "r") as f:
    for line in f:
        cleaned_line = line.split(";")[0].strip()
        if not cleaned_line:
            continue

        if cleaned_line.startswith("[") and cleaned_line.endswith("]"):
            name=cleaned_line[1:-1].strip()

            if name=="bondedtypes":
                current_residue=None
                current_section=None
                continue

            elif name in sub_sections:
                current_section=name
               
            else:
                current_residue=name
                residues[current_residue]={
                    "atoms":{},
                    "bonds":[],
                    "dihedrals":[],
                    "exclusions":[],
                    "impropers":[]
                }
                

        else:
            if current_residue is None or current_section is None:
                continue
            fields=cleaned_line.split()
            
            if current_section == "atoms":
                if len(fields) >= 3:
                    atom_name = fields[0]
                    atom_type = fields[1]
                    charge = float(fields[2])

                    residues[current_residue]["atoms"][atom_name] = {
                        "type": atom_type,
                        "charge": charge
                    }

            elif current_section == "bonds":
                if len(fields) >= 2:
                    atom_1 = fields[0]
                    atom_2 = fields[1]
                    residues[current_residue]["bonds"].append((atom_1, atom_2))

            elif current_section == "impropers":
                if len(fields) >= 1:
                    residues[current_residue]["impropers"].append(tuple(fields))

            elif current_section == "dihedrals":
                if len(fields) >= 1:
                    residues[current_residue]["dihedrals"].append(tuple(fields))

            elif current_section == "exclusions":
                if len(fields) >= 1:
                    residues[current_residue]["exclusions"].append(tuple(fields))

