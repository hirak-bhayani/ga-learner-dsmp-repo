# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here

banks = bank.drop(columns="Loan_ID")
print("*******************************")
print(banks.isnull().sum())
print("*******************************")
bank_mode = banks.mode()
banks.fillna(bank_mode.iloc[0], inplace=True)
print(banks)
#code ends here


# --------------
# Code starts here
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')

# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks["Self_Employed"]=="Yes") & (banks["Loan_Status"]=="Y")].shape[0]
loan_approved_nse = banks[(banks["Self_Employed"]=="No") & (banks["Loan_Status"]=="Y")].shape[0]
percentage_se = 100*(loan_approved_se/614)
print(percentage_se)
percentage_nse = 100*(loan_approved_nse/614)
print(percentage_nse)

# code ends here


# --------------
# code starts here
loan_term = banks["Loan_Amount_Term"].apply(lambda x:x/12)

#big_loan_term = loan_term>=25

big_loan_term = len(loan_term[loan_term>=25])

print(big_loan_term)
#df[(df > 3).sum(axis=1) >= 3]
# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby["ApplicantIncome","Credit_History"]
mean_values = loan_groupby.mean()



# code ends here


