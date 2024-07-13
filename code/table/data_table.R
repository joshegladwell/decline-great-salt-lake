# Import libraries
library(tidyverse)
library(DT)
library(htmlwidgets)

# Read in water elevation data
water_elev <- read.csv(
  "../../data/raw/USGS_Water_Levels/usgs_water_levels.tsv", 
  sep = '\t',
  skip = 29
) %>%
  # Drop first row
  filter(!row_number() %in% c(1)) %>%
  # Rename elevation column
  rename(
    "water_elevation_ft" = "X178324_62614_00003"
  ) %>%
  # Drop rows with missing values in water elevation column
  filter(water_elevation_ft != "") %>%
  # Convert water_elevation_ft to numeric
  mutate(water_elevation_ft = as.numeric(water_elevation_ft)) %>%
  # Create year column to group by year and get summary statistics on water
  # elevation
  separate(datetime, c("year", NA, NA), sep = "-") %>%
  group_by(year) %>%
  summarize(
    avg_water_elev_ft = round(mean(water_elevation_ft), 2),
    max_water_elev_ft = max(water_elevation_ft),
    min_water_elev_ft = min(water_elevation_ft)
  )

# Write to csv
write.csv(
  water_elev,
  "../../data/modified/elevation/water_elevation.csv", 
  row.names = FALSE
)

# Generate datatable
dt_result <- datatable(
  water_elev,
  rownames = FALSE,
  colnames = c(
    "Year", 
    "Average Water Elevation (ft)",
    "High Water Elevation (ft)",
    "Low Water Elevation (ft)"
  )
)

saveWidget(dt_result, "./table.html")
