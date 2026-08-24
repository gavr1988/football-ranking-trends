from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/cleaned/fifa_ranking_clean.csv")


def load_data(path: Path) -> pd.DataFrame:
    """Load the cleaned FIFA rankings dataset."""

    df = pd.read_csv(
        path,
        parse_dates=["rank_date"]
    )

    print(f"Loaded {len(df):,} cleaned rows.")

    return df


def basic_summary(df: pd.DataFrame) -> None:
    """Display a basic overview of the dataset."""

    print("\nDataset Summary")
    print("-" * 40)

    print(f"Countries: {df['country_full'].nunique()}")
    print(f"Confederations: {df['confederation'].nunique()}")
    print(f"First ranking date: {df['rank_date'].min().date()}")
    print(f"Last ranking date: {df['rank_date'].max().date()}")


