from pathlib import Path

import pandas as pd



# File paths

RAW_PATH = Path("data/raw/fifa_ranking.csv")
OUTPUT_PATH = Path("data/cleaned/fifa_ranking_clean.csv")

def load_data(path: Path) -> pd.DataFrame:
    """Load the raw FIFA rankings dataset."""
    df = pd.read_csv(path)

    print(f"Loaded {len(df):,} rows and {df.shape[1]} columns.")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare the FIFA rankings data for analysis."""

    df = df.copy()

    