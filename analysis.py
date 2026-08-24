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


# Question 1
def number_one_rankings(df: pd.DataFrame) -> pd.DataFrame:
    """Which countries appeared at number one most often?"""

    result = (
        df[df["rank"] == 1]
        .groupby("country_full")
        .size()
        .reset_index(name="number_one_appearances")
        .sort_values(
            "number_one_appearances",
            ascending=False
        )
    )

    return result

# Question 2
def top_10_appearances(df: pd.DataFrame) -> pd.DataFrame:
    """Which countries appeared in the Top 10 most often?"""

    result = (
        df[df["rank"] <= 10]
        .groupby("country_full")
        .size()
        .reset_index(name="top_10_appearances")
        .sort_values(
            "top_10_appearances",
            ascending=False
        )
    )

    return result

# Question 3
def top_50_by_confederation(df: pd.DataFrame) -> pd.DataFrame:
    """Which confederations have the most Top 50 appearances?"""

    result = (
        df[df["rank"] <= 50]
        .groupby("confederation")
        .size()
        .reset_index(name="top_50_appearances")
        .sort_values(
            "top_50_appearances",
            ascending=False
        )
    )

    return result

# Question 4
def latest_rankings(df: pd.DataFrame) -> pd.DataFrame:
    """Show the Top 10 countries on the latest ranking date."""

    latest_date = df["rank_date"].max()

    result = (
        df[df["rank_date"] == latest_date]
        .sort_values("rank")
        .head(10)
        [["rank", "country_full", "confederation"]]
    )

    return result