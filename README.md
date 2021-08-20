# Machine learning application in predicting prices of real estate

## Summary
&nbsp;&nbsp;&nbsp;&nbsp;The goal of this project is to predict prices of real estates for sale in Belgrade, Serbia. Learning process was done by [linear regression](https://en.wikipedia.org/wiki/Linear_regression) and [kNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) algorithms.
  * First, it was necessary to create web crawler which will scrape real estates from various websites. 
  * Secondly, we needed to write a Python scripts to preprocess data. 
  * Thirdly, we used MySQL and Python scripts to generate queries and plots. 
  * Finally, we used Python to create linear regression and kNN and generate prediction.

## Web crawler & scraper
&nbsp;&nbsp;&nbsp;&nbsp;The data was scrapped from two websites ([4zida.rs](https://www.4zida.rs/) and [nekretnine.rs](https://www.nekretnine.rs/)) using [Scrapy framework](https://scrapy.org/) written in Python. Data, which was scrapped, has a total of **over 100,000 different real estates** over whole country. For each real eastate following features were scraped: price, type, city, address, square footage, year built, land area (for houses), floor, registration, heating type, number of rooms, number of bathrooms, parking, elevator, terrace. Since each real estate ad is manually added by user, many features were often missing. Output for each website was [json file](https://en.wikipedia.org/wiki/JSON) where each element had one real estate and its features.

## Preprocessing data
&nbsp;&nbsp;&nbsp;&nbsp;First step in preprocessing data was merging all data we got from different website into single json file. After that it was necessary to convert all characters and strings to integers or floats. Some ads were written in cyrillic and they had to be converted to latin. There were 5 special cases where user wrongly inserted information that was hard coded. Numerous real estates were deleted because of feature value error (very low/high price, very high number of rooms etc.).
Goal of this project is to predict prices of flats for sale in Belgrade, therefore separate json was created with real estates belonging to that category.

---
Address was separately converted to number because of its complexity. Because location is often key factor in predicting price of real estate, [Google Maps API](https://cloud.google.com/maps-platform/maps) was used to convert addresses to coordinates. After that [Geopy library](https://geopy.readthedocs.io/en/stable/) was used to calculate distance between [center of Belgrade](https://www.google.com/maps/place/%D0%A2%D0%B5%D1%80%D0%B0%D0%B7%D0%B8%D1%98%D1%81%D0%BA%D0%B0+%D1%87%D0%B5%D1%81%D0%BC%D0%B0/@44.8133536,20.4593651,18z/data=!4m13!1m7!3m6!1s0x0:0x0!2zNDTCsDQ4JzQ3LjkiTiAyMMKwMjcnMzEuMiJF!3b1!8m2!3d44.8132984!4d20.4586731!3m4!1s0x475a7b05667b6193:0x4a1ff6d1eae390cd!8m2!3d44.8132192!4d20.4604688) and given coordinate.

## Visualization
&nbsp;&nbsp;&nbsp;&nbsp;To get more general sense of real estates, six graphs were created.
- Top 10 most popular districts in Belgrade by number of avaliable real estates

![Plot1](visualisation/a/izgradjene_nekretnine.png)

- [Flats by number of square footage](visualisation/b/stanovi_po_kvadraturi.png)
- [Real estates by year of construction](visualisation/c/izgradjene_nekretnine.png)
- [For sale/rent by city](visualisation/d/prodaja_iznajmljivanje.png)
- [Price of real estates divided in six groups](visualisation/e/cene_po_opsegu.png)
- [Real estate with/without parking in Belgrade](visualisation/f/izgradjene_nekretnine.png)

## Linear regression
&nbsp;&nbsp;&nbsp;&nbsp; Since not every real estate has every feature, we had to remove some features that had very high amount of real estates ad with empty field. Remaining features which were chosen for linear regression features were **address, square footage, floor, number of rooms, parking, elevator and terrace**. Before learning data had to be normalized and shuffled. Learning was done by **nested 10-fold cross validation** with train and dev set so we can find best hyperparameters. There are two hyperparameters: **learning rate** and **mini-batch size**.

---

After finding best hyperparameters, **10-fold cross validation** was done on test and train (now train set is equal to train and dev set from previous step) set. This was first time evaluation is done on test set. Performanse was calculated with [average root mean squared error](https://en.wikipedia.org/wiki/Root-mean-square_deviation) and [average mean absolute error](https://en.wikipedia.org/wiki/Mean_absolute_error). Next step was training linear regression on whole data using chosen hyperparameters to get best parameters which were exported to [JSON file](\linear_regression\model_parameters.json) for future use.

## kNN
&nbsp;&nbsp;&nbsp;&nbsp;Since kNN is lazy learner, it does not have learning part but there was normalization as hyperparameter to find out does normalization helps in this case or not. K can be manually imputed or automatically calculated as square root of number of real estates. Distance from imputed real estate was calculated with two different methods. First was [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance), where distance between two points is calculated using the [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem). Second method was [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) where distance between two points is the sum of the absolute differences of their [Cartesian coordinates](https://en.wikipedia.org/wiki/Cartesian_coordinate_system). kNN does not have any parameters but for algorithm to predicts it needs to run throughout every real estate in data each time.

## Results
&nbsp;&nbsp;&nbsp;&nbsp; Output of each algorithm should be number from range from 0 to 4, where 0 represents price of real estate is under 50,000e, 1 is price between 50 and 100,000e and 4 is over 200,000e. At the evaluation linear regression sees test data for the first time and evaluates its parameters on that data. kNN on other hand just compares each real estate with rest of the data.

- ***Linear regression achieved ~67% accuracy***
- ***kNN achieved 64% without normalization*** and 60% with normalization

## Future improvements
&nbsp;&nbsp;&nbsp;&nbsp;Both linear regression and kNN proved not so efficient against complex problem, which means we should use algorithms that are more suited for solving very complex problems like [polynomial regression](https://en.wikipedia.org/wiki/Polynomial_regression), [SVM](https://en.wikipedia.org/wiki/Support-vector_machine), [neural networks](https://en.wikipedia.org/wiki/Artificial_neural_network) or [deep learning](https://en.wikipedia.org/wiki/Deep_learning).
