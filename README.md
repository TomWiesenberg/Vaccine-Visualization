# COVID-19 Vaccine Effectiveness Visualization

Generates a graph plotting total vaccine doses per 100k population versus cumulative COVID-19 cases per 100k population in last 7 days for each of the 50 US states. Each time the Python script is run, it looks for updated data from the CDC. A trendline is plotted as well.

## Data Sources

* Covid Cases: https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36
* Vaccine Doses Adminstered: https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-Jurisdi/unsk-b7fc
* US State Populations: https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population
  * Census population, April 1, 2010
