# football-ranking-trends
# FIFA Ranking Analysis

This project explores historical FIFA World Rankings using **Python**, **pandas**, **matplotlib**, and **Tableau**.

The workflow is split into three main stages:

```text
Raw FIFA rankings
        ↓
Data cleaning and preparation
        ↓
Exploratory analysis and Python visualisations
        ↓
Interactive Tableau dashboard
```

The aim of the project is to demonstrate a simple end-to-end data analysis workflow, from cleaning raw data through to answering analytical questions and presenting the findings visually.

---

## 1. Data Preparation

The first stage of the project focuses on preparing the raw FIFA World Rankings dataset for analysis.

The cleaning process is handled in `run.py` using **Python** and **pandas**.

The purpose of this stage is to create a consistent, analysis-ready dataset that can be reused throughout the rest of the project.

### Dataset

The raw dataset is stored in:

```text
data/raw/fifa_ranking.csv
```

The dataset contains historical FIFA international ranking information, including:

* Country
* Country abbreviation
* FIFA ranking
* Ranking date
* Total ranking points
* Previous ranking points
* Ranking movement
* Confederation
* Historical weighted ranking metrics

### Cleaning Process

The `run.py` script performs the following steps:

1. **Loads the raw dataset**

   * The CSV file is imported using `pandas.read_csv()`.

2. **Checks the original data types**

   * Column data types are inspected before any transformations are made.
   * This helps identify fields that may require conversion.

3. **Converts the ranking date**

   * `rank_date` is converted from an `object` data type into a pandas `datetime`.
   * Invalid date values are converted to missing values using `errors="coerce"`.

4. **Removes invalid dates**

   * Records where `rank_date` cannot be successfully converted are removed.

5. **Removes duplicate observations**

   * Duplicate records are identified using the combination of `country_full` and `rank_date`.
   * The most recent duplicate occurrence is retained.

6. **Cleans text fields**

   * Leading and trailing whitespace is removed from:

     * `country_full`
     * `country_abrv`
     * `confederation`

7. **Creates additional date fields**

   * `year`
   * `month`
   * `month_name`

   These fields make time-based filtering and analysis easier in both Python and Tableau.

8. **Creates ranking categories**

   * Rankings are grouped into:

     * Top 10
     * 11–25
     * 26–50
     * 51+

9. **Creates indicator fields**

   * `is_number_one`
   * `is_top_10`
   * `is_top_50`

   These fields simplify later calculations involving ranking performance.

10. **Flags available FIFA points data**

    * A `has_total_points` field identifies records where `total_points` is greater than zero.
    * This is useful because the points field is not consistently populated throughout the full historical dataset.

11. **Sorts the cleaned dataset**

    * Records are ordered by country and ranking date.

12. **Exports the cleaned dataset**

    * The processed file is saved to:

```text
data/cleaned/fifa_ranking_clean.csv
```

### Running the Cleaning Script

From the root directory of the project, run:

```bash
python run.py
```

The script prints useful information to the terminal, including:

* Number of rows loaded
* Original column data types
* `rank_date` data type before and after conversion
* A preview of the cleaned dataset
* Location of the exported file

### Output

The cleaned dataset becomes the main source for the remaining stages of the project:

```text
fifa_ranking.csv
        ↓
run.py
        ↓
fifa_ranking_clean.csv
        ↓
analysis.py
        ↓
visualisations.py
        ↓
Tableau
```

Keeping the raw and cleaned files separate ensures that the original dataset remains unchanged while providing a reproducible data preparation workflow.

---

## 2. Exploratory Analysis and Visualisation

The second stage of the project uses the cleaned FIFA rankings dataset to explore historical ranking performance.

The analysis is split between:

* `analysis.py` for calculations and summary findings
* `visualisations.py` for Python-based charts

This separation keeps the project organised and makes each stage easier to understand and maintain.

### Analysis Questions

The exploratory analysis focuses on four main questions.

#### 1. Which countries appeared at number one most often?

The dataset is filtered to records where:

```text
rank = 1
```

The remaining records are grouped by country and counted to identify which national teams appeared at the top of the FIFA rankings most frequently.

This provides a simple measure of historical dominance.

---

#### 2. Which countries appeared in the Top 10 most often?

The analysis filters the dataset to rankings between 1 and 10.

The number of Top 10 appearances is then calculated for each country.

This provides a broader view of long-term consistency compared with only examining teams that reached number one.

---

#### 3. Which confederations accumulated the most Top 50 appearances?

Records with a FIFA ranking of 50 or better are grouped by confederation.

This analysis compares the historical representation of each confederation within the Top 50.

The result should be interpreted as **total historical Top 50 appearances**, rather than a definitive measure of confederation strength, because confederations contain different numbers of national teams.

---

#### 4. What did the latest Top 10 ranking in the dataset look like?

The most recent ranking date in the dataset is identified using:

```python
df["rank_date"].max()
```

The dataset is then filtered to that date and sorted by FIFA ranking.

The first ten records provide a snapshot of the Top 10 national teams at the end of the dataset.

---

### Python Visualisations

The `visualisations.py` script creates three supporting charts using **matplotlib**.

These charts provide a quick visual overview of the main findings before the data is taken into Tableau.

### Chart 1: Most Number One Ranking Appearances

A bar chart is used to compare the countries with the highest number of appearances at FIFA rank number one.

The visualisation involves:

* Filtering records where `rank == 1`
* Grouping records by country
* Counting appearances
* Sorting countries from highest to lowest
* Displaying the leading countries in a bar chart

This chart highlights which national teams have historically dominated the top position.

---

### Chart 2: Most Top 10 Ranking Appearances

A second bar chart shows the countries with the most appearances inside the FIFA Top 10.

This provides a different perspective from the number-one analysis by focusing on sustained high-level ranking performance.

The analysis:

```text
Filters Top 10 records
        ↓
Groups by country
        ↓
Counts appearances
        ↓
Ranks the leading countries
```

---

### Chart 3: Ranking History of Selected Countries

A line chart compares the ranking history of selected major football nations:

* Brazil
* Germany
* Argentina
* Spain
* France

Each country's FIFA ranking is plotted against `rank_date`.

Because a lower numerical ranking represents better performance, the y-axis is inverted so that **rank 1 appears at the top of the chart**.

This makes changes in performance more intuitive to read.

The chart provides a time-series view of how the selected countries moved through the FIFA rankings across the period covered by the dataset.

---

### Running the Analysis

The analytical summary can be run using:

```bash
python analysis.py
```

The results are printed directly to the terminal.

The Python visualisations can then be run using:

```bash
python visualisations.py
```

The charts are displayed sequentially using matplotlib.

---

### Purpose of the Python Analysis

The Python analysis is intended to provide an initial understanding of the dataset rather than act as the final visual product.

It demonstrates:

* Data filtering
* Grouping and aggregation
* Sorting and ranking
* Working with datetime data
* Reusable Python functions
* pandas dataframe manipulation
* matplotlib visualisation
* Basic time-series analysis

The findings from this stage are then used to inform the design of the interactive **Tableau dashboard**, where users can explore ranking trends, countries, confederations, and time periods in more detail.
