# --------------
# Importing header files
import numpy as np
# Path of the file has been stored in variable called 'path'
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Code starts here
data = np.genfromtxt(path,delimiter=",",skip_header=1)
print(data)
census = np.concatenate((data, new_record))
print(census)


# --------------
#Code starts here
age = np.array(census[:,0])
print(age)
max_age = age.max()
print("The maximum age observed is:",max_age)
min_age = age.min()
print("The minimum age observed is:",min_age)
age_mean = age.mean()
print("The mean age observed is:",age_mean)
age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
import numpy as np
race = np.array(census[:,2])
race_0 = np.array(census[race==0])
race_1 = np.array(census[race==1])
race_2 = np.array(census[race==2])
race_3 = np.array(census[race==3])
race_4 = np.array(census[race==4])
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
minlength = min(len_0,len_1,len_2,len_3,len_4)
minority_race = 3





# --------------
#Code starts here
import numpy as np
age = np.array(census[:,0])
senior_citizens = np.array(census[age>60])
working_hours = senior_citizens[:,6]
print(working_hours)
working_hours_sum = working_hours.sum()
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
import numpy as np
educationnum = np.array(census[:,1])
high = np.array(census[educationnum>10])
low = np.array(census[educationnum<=10])

income = np.array(census[:,7])
high_income = np.array(high[:,7])
low_income = np.array(low[:,7])
avg_pay_high = high_income.mean()
print(avg_pay_high)
avg_pay_low = low_income.mean()
print(avg_pay_low)


