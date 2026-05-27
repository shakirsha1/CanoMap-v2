import pandas as pd

def merge_targets(net_df, track_df):

    net_df["source_type"] = "NetInfer"
    track_df["source_type"] = "TrackMyPDB"

    merged = pd.concat([net_df, track_df], ignore_index=True)

    merged = merged.drop_duplicates(subset=["uniprot"])

    return merged
