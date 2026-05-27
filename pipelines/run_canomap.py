from modules.netinfer.runner import run_netinfer
from modules.trackmypdb.runner import run_trackmypdb
from modules.integration.merge import merge_targets
from modules.canine.rbh_filter import filter_canine_targets
from modules.scoring.score_engine import score_targets
from modules.report.generator import generate_report


def main():

    compound_name = "Cannflavin A"
    smiles = "O=C1C=CC(O)=C..."  # placeholder

    print("\n🧬 Starting CanoMap v2 Pipeline...\n")

    # 1. NetInfer
    net_df = run_netinfer(compound_name, smiles)

    # 2. TrackMyPDB
    track_df = run_trackmypdb(compound_name, smiles)

    # 3. Merge
    merged = merge_targets(net_df, track_df)

    # 4. Canine filtering
    canine_targets = filter_canine_targets(merged)

    # 5. Scoring
    scored = score_targets(canine_targets)

    # 6. Report
    generate_report(scored)

    print("\n✅ CanoMap v2 Completed Successfully")


if __name__ == "__main__":
    main()
