import pandas as pd

def run_netinfer(name, smiles):

    print(f"\n🧠 NetInfer: {name}")

    # MOCK OUTPUT (replace later with API)
    data = {
        "uniprot": ["P12345", "Q9Y2X1", "P99999"],
        "score": [0.9, 0.85, 0.8],
        "source": ["NetInfer"] * 3
    }

    return pd.DataFrame(data)
