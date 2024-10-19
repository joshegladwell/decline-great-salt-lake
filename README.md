# ANLY 503 Data Visualization Project Final Project - Decline of the Great Salt Lake
## Joshua Gladwell
This is a project I completed as part of my master's program in Data Science and Analytics at Georgetown University.

View the hosted website at: [https://joshegladwell.github.io/projects/pages/decline-great-salt-lake/](https://joshegladwell.github.io/projects/pages/decline-great-salt-lake/)

View the local website at: [/website/_site/index.html](./website/_site/index.html)

## Executive Summary
Over the past forty years, Utah's Great Salt Lake has steadily receded. The growing demand for water fueled by agriculture and the growing local population has claimed more and more runoff that refills the lake after each dry season. This has posed several unforeseen consequences for the Salt Lake City metropolitan area including the threat of toxic dust and sediment from the dried lakebed blowing into the city and the loss of a longstanding brine shrimp ecosystem.

This project takes a data visualization-based approach to exploring the story of the Great Salt Lake and the ramifications for its rapid decline. View the website [here](http://gladwell.georgetown.domains/anly503/_site/).

## The Five Data Views
The website, which can be viewed [here](http://gladwell.georgetown.domains/anly503/_site/), features five unique views illustrating different data-driven aspects to the story of the Great Salt Lake's decline. The order in which they appear on the website goes as follows:

1. Figure 1: 3D model of the Great Salt Lake, circa April 2023.
   - The code for this visual can be found at [`code/3D_model/rayshader.Rmd`](./code/3D_model/rayshader.Rmd). The code renders a video (also saved in the `3D_model` directory) that has been embedded into the website.
   - This is considered the "innovative view" per the project requirements due to its challenging combination of elevation data with bathymetry data from completely different sources. It is also innovative in that none of the articles I have read about the Great Salt Lake's decline have anything close to a 3D model. The only similar visuals I have found are of simple satellite images.
2. Figure 2: Interactive line plots illustrating the change in Great Salt Lake’s water elevation.
   - The code for this visual can be found at [`code/plotly_elevation/plotly_elevation.ipynb`](./code/plotly_elevation/plotly_elevation.ipynb). The code saves the resulting plot in HTML, which has been manually copied into the `website/index.qmd` file that renders the entire website.
3. Figure 3: Figure 3: 3D model of the Great Salt Lake, illustrating the water elevation for every month for which there is recorded data (April 1966 - April 2023).
   - The code for this visual can be found at [`code/elevation_model/3d_water_anim_m.R`](./code/elevation_model/3d_water_anim_m.R). As with the code for Figure 1, this code renders and saves a video into the same directory, which is then embedded into the website.
   - Although the 3D model in this view is similar to that of Figure 1 (and is equally as innovative as Figure 1), it is considered a different view from Figure 1 because it is emphasizing a different aspect of the story. Figure 1 shows an overview of the lake as part of the introduction to the story while also illustrating the Union Pacific causeway. Figure 3, on the other hand, emphasizes the expansive dry land that the shrinking lake is exposing. Although on the surface one may argue that they are part of the same "view" as defined by the project requirements, they are fundamentally different views when considered in the context of the narrative.
4. Figure 4: Bubble map of arsenic levels around the Salt Lake Valley, circa 2018-19.
   - The code for this visual can be found at [`code/toxins/dust_choropleth.ipynb`](code/toxins/dust_choropleth.ipynb). The other Python script in this directory, `get_elevation.py`, is a script used to add elevation features to the raw dataset and save an updated dataset in `data/modified/toxins/`.
   - This is considered the "interactive tooltip" view per the project requirements.
5. Figure 5: Linked view of brine shrimp sample counts for every recorded brine shrimp harvest from 2010-2023.
   - The code for this visual can be found at [`code/brine_shrimp/brine_shrimp.ipynb`](./code/brine_shrimp/brine_shrimp.ipynb). The other Python script in this directory, `get_shrimp_data.py`, is a script used to scrape the shrimp data from [https://wildlife.utah.gov/gslep/harvests.html](https://wildlife.utah.gov/gslep/harvests.html), clean it, join it on the elevation data, and save the resulting dataset in `data/modified/shrimp/`.
   - This is considered the "linked view" per the project requirements.

## Data
The raw data sources are too large to include in this repository. They can be downloaded directly from Box. In order to run the code in this repository, which heavily references these data, download the `data/` directory from [this Box link](https://georgetown.box.com/s/yncptmh4jgn7945udiubcexetym5kf1q) and add downloaded directory to the root directory of this repository (preserving the directory name `data/`).

The raw datasets used for this project are as follows:
- `DWR_Water_Budget` is downloaded from the [Utah Division of Water Resources site](https://dwre-utahdnr.opendata.arcgis.com/pages/water-budget) and contains data relating to planned water usage.
- `DWR_Water_Use` is downloaded from the [Utah Division of Water Resources site](https://dwre-utahdnr.opendata.arcgis.com) and contains data relating to water usage.
- `SRTM` contains satellite imagery of the Great Salt Lake and is downloaded from [Derek Watkins' 30-Meter SRTM Tile Downloader](https://dwtkns.com/srtm30m/), which features data from the NASA Shuttle Radar Topography Mission.
- `Tarboton_USU` contains bathymetry data (terrain data beneath the surface of the lake) from David Tarboton of Utah State University. It can be downloaded [here](https://www.hydroshare.org/resource/582060f00f6b443bb26e896426d9f62a/).
- `UGRC_Shoreline` contains shoreline geospatial data from the Utah Geospatial Resource Center. It can be downloaded [here](https://opendata.gis.utah.gov/datasets/utah::utah-great-salt-lake-shoreline/explore).
- `USGS_Dust_and_Sediment` contains data from a two-year study sampling dust around the Salt Lake Valley. It is published by Molly A Blakowski of Utah State University and the U.S. Geological Survey. It can be downloaded [here](https://www.sciencebase.gov/catalog/item/62ebed2ad34eacf539724ce2)
- `USGS_Landsat` contians Landsat terrain data from the U.S. Geological Survey in the area surrounding the Great Salt Lake. It can be downloaded [here](https://earthexplorer.usgs.gov).
- `USGS_Water_Levels` contains data on the water elevation for the Great Salt Lake since 1966. It can be downloaded [here](https://waterdata.usgs.gov/monitoring-location/10010000/#parameterCode=62614&period=P7D)

The modified datasets are as follows:
- `elevation/water_elevation.csv` is adapted from `USGS_Water_Levels` and serves as the datatable at the end of the main webpage. The code for creating this datatable is at [`/code/table/data_table.R`](./code/table/data_table.R).
- `rasters/` is a directory containing intermediate raster images for the 3D models.
- `shrimp/` is a directory containing cleaned data adapted from `USGS_Water_Levels` and shrimp data from [https://wildlife.utah.gov/gslep/harvests.html](https://wildlife.utah.gov/gslep/harvests.html). `shrimp/seasons.csv` is the cleaned dataset scraped directly from the link above, while `shrimp/seasons_levels.csv` contains the same data joined to the water elevation data.
- `toxins/dust_data.csv` is adapted from `USGS_Dust_and_Sediment`, the only difference being that it includes elevation as calculated by `code/toxins/get_elevation.py`.
- 

## Repository structure

You will work within an **organized** repository and apply coding and development best practices. The repository has the following structure:

```.
├── code/       <- Contains all code used in this project
├── data/       <- Contains all data used in this project (see Box link above)
├── documents/  <- Contains a project outline, proposal, and design files for the poster
├── img/        <- Contains designs for poster elements
├── website/    <- Contains all website files
└── README.md
```

