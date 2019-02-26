# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000
rootofsample = math.sqrt(sample_size)
#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  
# path        [File location variable]
#Code starts here
data = pd.read_csv(path)
data_sample = data.sample(n=sample_size, random_state=0)
sample_mean = data_sample["installment"].mean()
sample_std = data_sample["installment"].std()
margin_of_error = z_critical*(sample_std/rootofsample)
upper_confidence_interval = sample_mean + margin_of_error
print("Upper confidence interval is:", upper_confidence_interval)
lower_confidence_interval = sample_mean - margin_of_error
print("Lower confidence interval is:", lower_confidence_interval)
confidence_interval = np.array([lower_confidence_interval, upper_confidence_interval])
print("Confidence interval is", confidence_interval)
true_mean = data["installment"].mean()
print("True mean of the installment for the population is:", true_mean)


# --------------
import matplotlib.pyplot as plt
import numpy as np
#Different sample sizes to take
sample_size=np.array([20,50,100])
fig, axes = plt.subplots(nrows=3, ncols=1)
for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        data_sample = data.sample(n=sample_size[i], random_state=0)
        mean_sample = data_sample["installment"].mean()
        m.append(mean_sample)
mean_series = pd.Series(m)
mean_series.hist()


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest
#Code starts here
data['int.rate'] = data['int.rate'].map(lambda x: x.rstrip('%'))
data['int.rate'] = pd.to_numeric(data['int.rate'])
#data['int.rate'].dtype.kind
data['int.rate'] = data['int.rate']/100
z_statistic, p_value = ztest(data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative="larger")
print("Z-statistics = ",z_statistic)
print("p-value = ",p_value)
if(p_value>0.05):
    inference = "Accept"
else:
    inference = "Reject"
print(inference)


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest
#Code starts here
z_statistic, p_value = ztest(data[data['paid.back.loan']=='No']['installment'],data[data['paid.back.loan']=='Yes']['installment'])
print("Z-statistics = ",z_statistic)
print("p-value = ",p_value)
if(p_value>0.05):
    inference = "Accept"
else:
    inference = "Reject"
print(inference)


# --------------
#Importing header files
from scipy.stats import chi2_contingency
#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1
#Code starts here
yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()
no = data[data['paid.back.loan'] == 'No']['purpose'].value_counts()
yes.dtype.kind
#observed = pd.concat([yes.transpose(), no.transpose()], keys=['Yes', 'No'])
#print(observed)
observed = pd.concat([yes.transpose(), no.transpose()], axis = 1, keys=['Yes', 'No'])
print(observed)
chi2, p, dof, ex = stats.chi2_contingency(observed)
print("Chi-square statistic = ",chi2)
print("p-value = ",p)
if(chi2>critical_value):
    inference = "Reject"
else:
    inference = "Accept"
print(inference)


