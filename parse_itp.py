atom_types={}

with open("ffnonbonded.itp","r") as f:
    for line in f:
        result=line.split(";")[0].strip()
        if not result:
            continue
        if result.startswith("[") and result.endswith("]"):
            name=result[1:-1].strip()

        else:
            fields=result.split()
            type_name=fields[0]
            mass=fields[2]
            sigma=fields[5]
            epsilon=fields[6]
            atom_types[type_name]={
                "mass":float(mass),
                "sigma":float(sigma),
                "epsilon":float(epsilon)
                }