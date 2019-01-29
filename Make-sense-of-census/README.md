### Project Overview

 Problem statement given: You have been hired by 'CACT'(Census Analysis and Collection Team) to test your numpy programming skills. Your major work for today involves census record management and data analysis. The dataset had details of 100 people with multiple features like: Age, race, sex, income, capital-gain, income etc. Data reading, age of a country, senior welfare etc. were some of the analysis carried out on he given dataset.


### Learnings from the project

 Key NumPy concepts utilized during this project were array appending, array slicing, array filtering & array aggregation.


### Approach taken to solve the problem

 - The dataset was first loaded basis the path given. New records were appended.
- We often associate the potential of a country based on the age distribution of the people residing there. So I carried out a simple analysis of the age distribution using basics like minimum age, maximum age, median & standard deviation.
- I then carried out a "minority report" which essentially involved extracting array subsets by stripping "census" by "race" & finding out the number of elements in each race.
- Part of the project involved ensuring senior welfare. As per the new govt. policy, all citizens above age 55 should not be made to work more than 25 hours per week. I wanted to check if the policy was being adhered to. So I first extracted the array "senior citizens" by stripping census where age>55. I then summed up their working hours. A simple division of these total hours by the number of senior citizens gave me their average working hours which were surprisingly above 25, hence reflecting that the policy was not being followed.
- My final step was to see if higher education levels indicated higher paying jobs.


