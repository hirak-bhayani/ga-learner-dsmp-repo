### Project Overview

 **Problem statement**
I am a die hard Lego enthusiast wishing to collect as many board sets as I possibly can. But before that I wish to be able to predict the price of a new lego product before its price is revealed so that I can budget it accordingly. Since (luckily!), I am a data scientist in the making, I figured I could solve this problem myself. This dataset contains information on lego sets scraped from lego.com. Each observation is a different lego set with various features like how many pieces in the set, rating for the set, number of reviews per set etc. My aim is to build a linear regression model to predict the price of a set.

**Data snapshot:**
!!![container width="100%" align="center"]
![Lego](undefined/account/b16/6a1f0c95-2915-474c-917f-dc711cc8d89b/b125/4543f024-52ee-4f70-99c6-9cfb2ab7fe6c/file.PNG)
!!![container-end]


### Learnings from the project

 Post this project completion, I now have a better understanding of building a regression model and important concept applications for:
- Train-test split
- Correlation between the features and how to eliminate redundancies to develop a better fit model
- Linear Regression
- Mean squared error (MSE) and R-squared Evaluation Metrics


### Approach taken to solve the problem

 - The first step was to split the data into training set and testing set.
- The next step was to check the co-relation of the different features versus the "List Price." This was depicted through scatter plots.
- Subsequently, the next task was to check features that are highly correlated with each other as these would adversely affect the lego pricing model. An inter-feature correlation threshold of 0.75 was set and if two correlated features had a value greater than 0.75, then I dropped the redundant features.
- Once the above explorations were cleared out, the most significant task was to use linear regression to predict the price. The model accuracy was then checked through the "Mean square error" and "R-sqaure" evaluation methods.
- Based on the distance between the true target y_test and predicted target y_pred, also known as the residual the cost function is defined. I then calculated the residual and visualized the errors in the model through a histogram.


