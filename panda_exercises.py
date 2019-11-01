import numpy as np
import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


insurance_data = pd.read_csv(filepath_or_buffer='insurance.csv',
                      sep=',',
                      header=0)
#Question 2 - Expolring to_string(), columns,index,dtype(), shape, info(), describe
pretty_print("Printing Insurance Data", insurance_data)
pretty_print("Exploring to_string", insurance_data.to_string())
pretty_print("Exploring columns", insurance_data.columns)
pretty_print("Expolring index", insurance_data.index)
pretty_print("Exploring dtypes", insurance_data.dtypes)
pretty_print("Exploring shape", insurance_data.shape)
pretty_print("Exploring Info", insurance_data.info())
pretty_print("Exploring describe", insurance_data.describe())

# Question 3
pretty_print("Insurance Data - Column Age", insurance_data['age'])

#Question 4
pretty_print("Insurance Data - Columns age, children, charges", insurance_data[['age', 'children', 'charges']].head(5))

#Question 5
pretty_print("Insurance Data - 5 first records of Columns age, children, charges ", insurance_data[['age', 'children', 'charges']].head(5))

#Question 6
pretty_print("Average charges", insurance_data['charges'].mean())
pretty_print("Min charges", insurance_data['charges'].min())
pretty_print("Max charges", insurance_data['charges'].max())

#Question 7

person = insurance_data[['age','sex','smoker']][insurance_data['charges'] == 10797.3362]
if len(person) > 0 :
	print("Info of person who paid 10797.3362 \n", person.to_string())
else:
	print("We could not find data matching this criteria.")

#Question 8
person_who_paid_max_charge = insurance_data[['age']][insurance_data['charges'] == insurance_data['charges'].max()]
	
if len(person_who_paid_max_charge) > 0 :
	print("\nInfo of person who paid max Charge \n", person_who_paid_max_charge.to_string())
else:
	print("We could not find data matching this criteria.")

#Question 9
pretty_print("\nNumber of insurred people for each region", insurance_data['region'].value_counts().to_string())

#Question 10 
# Assumption1: count of all persons under 18 
pretty_print("\nNumber of insurred people who are children - Assumption 1: ", len(insurance_data[insurance_data['age'] < 18 ]))
# Assumption1: count of children who have an insurred parent
pretty_print("\nNumber of insurred people who are children - Assumption 2:", len(insurance_data[insurance_data['children'] > 0 ]))

#Question 11
# We assumed that : 
# We have a positive correlation between charges & age
#
# We have positive correlation  between bmi & children

#question 12
print("Correlation \n", insurance_data.corr().to_string())



