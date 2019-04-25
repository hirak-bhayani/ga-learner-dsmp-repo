### Project Overview

 The dataset contained information on the insurance claim. Each observation is about a different policyholder with various features like the age of the person, the gender of the policyholder, body mass index, providing an understanding of the body, number of children of the policyholder, smoking state of the policyholder and individual medical costs billed by health insurance.



### Learnings from the project

 After completing this project, I have a better understanding of how to build a logistic regression model post application of concepts like:

- Train-test split
- Correlation between different features
- Logistic Regression
- Auc score
- ROC AUC plot


### Approach taken to solve the problem

 - The first step was to split the training & testing data
- A boxplot was then plotted to check for any outliers followed by plotting of a pair plot to gauge the most internally strongly co-related features. This in turn helped me with a better logistic regression model.
- The target variable for this dataset was "insuranceclaim." Post the internal co-relation amongst features, the next step was to check how each feature individually co-related to the target variable. This was done by creating a dataframe & then looping through rows & columns and subsequently using seaborn to create a countplot depiction.
- The next key task was to instantiate a Logistic Regression model to predict the insurance claim & calculating the accuracy score for the same (which turned out to be 82%)
- As a last step, the performance of the binary classifier was checked by calculating the ROC AUC curve & visualizing the same.
 



