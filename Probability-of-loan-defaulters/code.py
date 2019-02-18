# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# code starts here
df = pd.read_csv(path)
isficocorrect = len(df[df["fico"]>700])
total = len(df)
p_a = isficocorrect/total
print(p_a)

ispurposecorrect = len(df[df["purpose"]=="debt_consolidation"])
p_b = ispurposecorrect/total
print(p_b)

df1 = df[df["purpose"]=="debt_consolidation"]
p_a_b = ispurposecorrect/isficocorrect
print(p_a_b)

result = (p_a_b == p_a)
print(result)
# code ends here


# --------------
# code starts here
paidbackyes = len(df[df["paid.back.loan"]=="Yes"])
print("Loan paid back no.:",paidbackyes)
total = len(df)
prob_lp = paidbackyes/total
print(prob_lp)
creditpolicyyes = len(df[df["credit.policy"]=="Yes"])
print("Credit policy yes no.:",creditpolicyyes)
prob_cs = creditpolicyyes/total
print(prob_cs)
table = pd.crosstab([df["paid.back.loan"]=="Yes"],[df["credit.policy"]=="Yes"])
print(table)
new_df = [df["paid.back.loan"]=="Yes"]
prob_pd_cs = 6696/(1349+6696)
print(prob_pd_cs)
bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
df1 = df[df["paid.back.loan"]=="No"]
print(df1)
df2 = df1["purpose"].value_counts()
print(df2)
#table = pd.crosstab(df1,df2)
#print(table)
df2.plot(kind="bar")
# code ends here


# --------------
# code starts here
inst_median = df["installment"].median()
inst_mean = df["installment"].mean()
df.hist(column="log.annual.inc",bins=8)
# Display plot
plt.axvline(x=inst_median,color="green")
plt.axvline(x=inst_mean,color="black")
# code ends here


