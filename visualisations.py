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

# Chart 1: Countries with most number one appearances

def plot_number_one_rankings(df: pd.DataFrame) -> None:
    """Plot countries with the most number one ranking appearances."""

    # Filter the dataset to records where a country was ranked number one
    # Group by country and count the number of appearances
    top_countries = (
        df[df["rank"] == 1]
        .groupby("country_full")
        .size()
        .reset_index(name="number_one_appearances")
        .sort_values(
            "number_one_appearances",
            ascending=False
        )
        .head(10)
    )

    # Create the figure
    plt.figure(figsize=(10, 6))

    # Create the bar chart
    plt.bar(
        top_countries["country_full"],
        top_countries["number_one_appearances"]
    )

    # Add a chart title and axis labels
    plt.title("Countries with Most FIFA #1 Ranking Appearances")
    plt.xlabel("Country")
    plt.ylabel("Number of #1 Appearances")

    # Rotate country names so they are easier to read
    plt.xticks(rotation=45)

    # Adjust the layout to prevent labels being cut off
    plt.tight_layout()

    # Display the chart
    plt.show()

# Chart 2: Countries with most Top 10 appearances

def plot_top_10_appearances(df: pd.DataFrame) -> None:
    """Plot countries with the most Top 10 ranking appearances."""

    # Filter the data to rankings between 1 and 10
    # Then count how often each country appeared in the Top 10
    top_10 = (
        df[df["rank"] <= 10]
        .groupby("country_full")
        .size()
        .reset_index(name="top_10_appearances")
        .sort_values(
            "top_10_appearances",
            ascending=False
        )
        .head(10)
    )

    # Create the figure
    plt.figure(figsize=(10, 6))

    # Create the bar chart
    plt.bar(
        top_10["country_full"],
        top_10["top_10_appearances"]
    )

    # Add a chart title and axis labels
    plt.title("Countries with Most FIFA Top 10 Appearances")
    plt.xlabel("Country")
    plt.ylabel("Number of Top 10 Appearances")

    # Rotate country names for readability
    plt.xticks(rotation=45)

    # Adjust spacing
    plt.tight_layout()

    # Display the chart
    plt.show()


# Chart 3: Ranking history for selected countries


def plot_ranking_history(df: pd.DataFrame) -> None:
    """Plot FIFA ranking history for selected countries."""

    # Countries selected for comparison
    selected_countries = [
        "Brazil",
        "Germany",
        "Argentina",
        "Spain",
        "France"
    ]

    # Filter the dataset to only include the selected countries
    selected_data = df[
        df["country_full"].isin(selected_countries)
    ].copy()

    # Sort the data by country and ranking date
    selected_data = selected_data.sort_values(
        ["country_full", "rank_date"]
    )

    # Create the figure
    plt.figure(figsize=(12, 7))

    # Create one line for each country
    for country in selected_countries:

        country_data = selected_data[
            selected_data["country_full"] == country
        ]

        plt.plot(
            country_data["rank_date"],
            country_data["rank"],
            label=country
        )

    # Add chart title and labels
    plt.title("FIFA Ranking History of Selected Countries")
    plt.xlabel("Ranking Date")
    plt.ylabel("FIFA Ranking")

    # Rank 1 should appear at the top of the chart
    plt.gca().invert_yaxis()

    # Display the country names
    plt.legend()

    # Add grid lines to make changes easier to follow
    plt.grid(alpha=0.3)

    # Prevent labels from being cut off
    plt.tight_layout()

    # Display the chart
    plt.show()

# Main workflow

def main():
    """Run the visualisation workflow."""

    # Load the cleaned dataset
    df = load_data(DATA_PATH)

    # Chart 1: Countries with most number one appearances
    plot_number_one_rankings(df)

    # Chart 2: Countries with most Top 10 appearances
    plot_top_10_appearances(df)

    # Chart 3: Ranking history for selected countries
    plot_ranking_history(df)


# Run the visualisation workflow when this file is executed directly
if __name__ == "__main__":
    main()
