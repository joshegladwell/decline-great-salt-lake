# Import pandas
import pandas as pd

# Read in data from GSLEP
shrimp_tables = pd.read_html("https://wildlife.utah.gov/gslep/harvests/sampling-data.html")

# Add year and season column to each table, adding 1 where the month is January
season_start= 2022

for season_table in shrimp_tables:
    # Define year column
    season_table['Year'] = season_start
    season_table.loc[season_table['Date'].str.contains("Jan"), 'Year'] = season_start+1

    # Define season column
    season_table['Season'] = str(season_start) + "-" + str(season_start - 2000 + 1)

    season_start -= 1

    season_table = season_table[season_table['Unnamed: 0'].isna()]

# Concatenate all tables into one df
shrimp_df = pd.concat(shrimp_tables)

# Drop description rows
shrimp_df = shrimp_df[shrimp_df['Unnamed: 0'].isna()]

# Append year to date
shrimp_df['Date'] = pd.to_datetime(shrimp_df['Date'] + ", " + shrimp_df['Year'].astype(str))

# Drop unnecessary columns
shrimp_df = shrimp_df.drop(['Unnamed: 0', 'Unnamed: 10', 'Year'], axis=1)

# Save dataframe
shrimp_df.to_csv("../../data/modified/shrimp/seasons.csv", index=False)


