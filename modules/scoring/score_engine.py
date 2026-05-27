
def score_targets(df):

    df["final_score"] = df.get("score", 0) * 1.0

    return df.sort_values("final_score", ascending=False)
