from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# Path to the cleaned FIFA rankings dataset
DATA_PATH = Path("data/cleaned/fifa_ranking_clean.csv")


def load_data(path: Path) -> pd.DataFrame:
    """Load the cleaned FIFA rankings dataset."""

    # Read the cleaned CSV file
    # parse_dates ensures rank_date is treated as a datetime column
    df = pd.read_csv(
        path,
        parse_dates=["rank_date"]
    )

    print(f"Loaded {len(df):,} cleaned rows.")

    return df

