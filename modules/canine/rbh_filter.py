import pandas as pd

def filter_canine_targets(df):

    try:
        db = pd.read_csv("data/canine_db/validated_orthologs.tsv", sep="\t")
    except:
        print("⚠️ Canine DB missing → skipping filter")
        return df

    filtered = df[df["uniprot"].isin(db["human_acc"])]

    return filtered
