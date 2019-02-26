### Project Overview

 The rise of superheroes and supervillains is at an all time high. The 'Academy of Super Beings(ASB)' was formed to bring order to it. I have with me the data of more than 500 super humans on which I intend to apply my knowledge of descriptive statistics in figuring out the important insights from it.

**Data snapshot:**
!!![container width="100%" align="center"]
![Superhero](undefined/account/b16/6a1f0c95-2915-474c-917f-dc711cc8d89b/b609/ccb0f76e-dd67-477a-8715-3889c7f57fd6/file.PNG)
!!![container-end]

Features of the dataset are the unique character "ID", name, gender, eyecolor, skincolor, haircolor, race of the character and a point allocation basis the intelligence, strength, speed, durability of each character.


### Learnings from the project

 Solving this project has helped me have a firmer grip on descriptive statistics and concepts like:
- Bar, boxplot & pie-chart plotting
- Creating subplots
- Feature co-relations &
- Inter-quartile range operations


### Approach taken to solve the problem

 - The first step after loading the data was to know the stand of the members of 'ASB'. Does good overpower evil or does evil overwhelm good? This was done basis the "Alignment" column & visually depicting the results through a pie-chart.
- Now for any of the members of ASB, combat skills are really important to survive when they find themselves in unwanted situtations. But I wasn't sure if combat relates to person's strength or her intelligence? Hence, I sampled both of them to check which case showcased a stronger co-relation. The Pearson co-effecient of co-relation was found by first finding the co-variance & then the standard deviation in each case.
- Quantile operations were then carried out to find the top percentile of superheroes & super-villains. This was done by sub-setting dataframes using the appropriate quantile threshhold.
- The next step was to measure certain attributes like intelligence, speed, power of the top 1% members of 'ASB', in case they go rogue and become threatening to the human kind. This was depicted using the boxplot method.


