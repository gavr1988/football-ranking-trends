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

    # Check data types before making any conversions
    print("\nData types before cleaning:")
    print("-" * 40)
    print(df.dtypes)

    print(f"\nrank_date dtype before conversion: {df['rank_date'].dtype}")

  
 # Convert ranking date from text to datetime
    df["rank_date"] = pd.to_datetime(
        df["rank_date"],
        errors="coerce"
    )

    print(f"rank_date dtype after conversion: {df['rank_date'].dtype}")

     # Remove duplicate country/date observations
    df = df.drop_duplicates(
        subset=["country_full", "rank_date"],
        keep="last"
    )

    # Clean string columns
    text_columns = [
        "country_full",
        "country_abrv",
        "confederation"
    ]

    for column in text_columns:
        df[column] = df[column].str.strip()

    # Create useful date fields
    df["year"] = df["rank_date"].dt.year
    df["month"] = df["rank_date"].dt.month
    df["month_name"] = df["rank_date"].dt.month_name()

    # Create ranking groups
    df["rank_band"] = pd.cut(
        df["rank"],
        bins=[0, 10, 25, 50, float("inf")],
        labels=[
            "Top 10",
            "11-25",
            "26-50",
            "51+"
        ]
    )

    # Indicator fields
    df["is_number_one"] = df["rank"].eq(1)
    df["is_top_10"] = df["rank"].le(10)
    df["is_top_50"] = df["rank"].le(50)

