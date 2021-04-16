# lichess-coach-scraper
Python code to scrape [lichess.org coach](https://lichess.org/coach) metadata and generate a .csv for subsequent analysis. Lichess has a strong community of title-verified coaches with a variety of ratings, rates, and locations, but does not expose structured data or search tools allowing a prospective student to sort and filter on these criteria, which makes it challenging to find a suitable coach in a mutually convenient timezone.

It uses selenium for browser automation and generates a file containing selected metadata, currently

    coach['Name']
    coach['Country']
    coach['Rate']
    coach['Rating']
    coach['Link']
The output of this script is a .csv which is suitable for analysis by a tool of your choice or for import into Google Sheets, where you can create pivot tables, slicers, or other views to find good candidate coaches.

## Video
![](Media/Video-Small.gif)

## Example Post-Analysis

Breakdown of number of coaches available in each country; countries coded white have zero coaches.

![](Media/geo-breakdown.png)
