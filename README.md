# Machine learning application in predicting prices of real estate

## Summary
&nbsp;&nbsp;&nbsp;&nbsp;The goal of this project is to predict prices of real estates for sale in Belgrade, Serbia. Learning process was done by linear regression and kNN algorithms.
  * First, it was necessary to create web crawler which will scrape real estates from various websites. 
  * Secondly, we needed to write a Python scripts to preprocess data. 
  * Thirdly, we used MySQL and Python scripts to generate queries and plots. 
  * Finally, we used Python to create linear regression and kNN and generate prediction.

## Web crawler & scraper
&nbsp;&nbsp;&nbsp;&nbsp;The data was scrapped from two websites (4zida.rs and nekretnine.rs) using Scrapy framework written in Python. Data, which was scrapped, has a total of over 100,000 different real estates over whole country. For each real eastate following features were scraped: price, type, city, address, square footage, year built, land area (for houses), floor, registration, heating type, number of rooms, number of bathrooms, parking, elevator, terrace. Since each real estate ad is manually added by user, many features were often missing. Output for each website was json file where each element had one real estate and its features.

## Visualization
&nbsp;&nbsp;&nbsp;&nbsp;To get more general sense of real estates, six graphs were created.
- Top 10 most popular districts in Belgrade by number of real estates

- Flats by number of square footage

- Real estates by year of construction

- For sale/rent by city

- Price of real estates divided in six groups

- Real estate with/without parking in Belgrade
---
## Linear regression
&nbsp;&nbsp;&nbsp;&nbsp;Goal of this project is to predict prices of flats for sale in Belgrade, therefore first step in preprocessing was 
---
## kNN
&nbsp;&nbsp;&nbsp;&nbsp;
---
## Results
&nbsp;&nbsp;&nbsp;&nbsp;
---
## Future improvements
&nbsp;&nbsp;&nbsp;&nbsp;
