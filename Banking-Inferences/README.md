### Project Overview

 **Problem Statement**
The Bank Of New York wants to expand its branches and for that it has certain hypothesis and statements it wants to verify. To do the verification for the bank, I will be using inferential statistics methods.

**Dataset snapshot:**
!!![container width="100%" align="center"]
![bank](undefined/account/b16/6a1f0c95-2915-474c-917f-dc711cc8d89b/b97/adf96db8-d6eb-44da-93e6-7950a0587f31/file.PNG)
!!![container-end]

Features of the dataset include the unique customer ID, loan interest rates, monthly installments owed if a loan is availed, the FICO score of the borrower, duration of the credit line, public records of the borrower (bankruptcy filings, tax liens, or judgments), the delinquency rate and so on.


### Learnings from the project

 This project has helped me get a better grasp on inferential statistics. Key concepts applied include:
- Central Limit Theorem
- Confidence Intervals
- Hypothesis Testing
- Chi Square Test


### Approach taken to solve the problem

 - The first step post loading the data was to extract a sample of the data and find the mean & standard deviation of one of the sample attributes. This was done to establish the margin of error given the z-score, which in turn helped me to determine the confidence interval of the sample. (Confidence interval = Sample mean +/- margin of error). It was found out that the true mean did lie in the confidence interval.
- The next step was to find out the veracity of the Central Limit Theorem for the "installment" column.
- Next, was to verify the bank manager's belief that people with purpose as "small business" have been issued a higher interest rate due to the risk associated. This was done using hypothesis testing with:
    **Null hypothesis**: There is no difference in interest rate being given to people with purpose as 'small business'
    **Alternate hypothesis**: Interest rate being given to people with purpose as 'small business' is higher than the average interest rate.
  The inference arrived at after finding the z-statistic & p-value was to reject the null hypothesis.
- A similar hypothesis testing was done to gauge if installment amounts had any effect on instances of loan defaults.
- Another thing that the bank suspected was that there was a strong association between the loan purpose of a person and whether this person had repaid the loan. Since both the columns were categorical, I applied the chi-square test to determine if the suspicion had any basis. The inference was that the distribution of purpose for loan defaulters and non defaulters was very different.


