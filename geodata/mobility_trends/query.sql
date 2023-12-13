SELECT
  country_region as country
  ,sub_region_1 as region
  ,date
  ,retail_and_recreation_percent_change_from_baseline as retail
  ,grocery_and_pharmacy_percent_change_from_baseline as grocery
  ,parks_percent_change_from_baseline as parks
  ,transit_stations_percent_change_from_baseline as transit
FROM
  `bigquery-public-data.covid19_google_mobility.mobility_report` 
WHERE
  country_region = "Indonesia" AND sub_region_1 = "Jakarta" AND EXTRACT(YEAR FROM date) = 2022
ORDER BY date
