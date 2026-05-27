import os

def generate_report(df):

    os.makedirs("outputs", exist_ok=True)

    df.to_csv("outputs/final_targets.tsv", sep="\t", index=False)

    print("\n📄 Report generated: outputs/final_targets.tsv")
