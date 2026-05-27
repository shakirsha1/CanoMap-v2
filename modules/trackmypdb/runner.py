import pandas as pd

def run_trackmypdb(name, smiles):

    print(f"\n🧪 TrackMyPDB: {name}")

    data = {
        "pdb_id": ["1ABC", "2DEF", "3XYZ"],
        "uniprot": ["P12345", "Q8AAA1", "P77777"],
        "score": [0.75, 0.82, 0.78],
        "source": ["TrackMyPDB"] * 3
    }

    return pd.DataFrame(data)
