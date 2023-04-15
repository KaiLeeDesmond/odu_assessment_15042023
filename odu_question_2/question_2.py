import pandas as pd
import matplotlib.pyplot as plt

# Importing the pandas library and aliasing it as pd
# Before loading the csv file provided, I noticed there was an UnicodeDecode Error with UTF-8.
# In order to fix that, I saved the file as CSV UTF-8 type.
df = pd.read_csv("autos1.csv")
# Reads the csv file into a dataframe. The variable df stores the dataframe
# print(df.to_string)
# When the to_string method is used, it only displays the first 5 and last 5 records of the dataframe
# the dataframe displaying is optional

#3.a answer:
print("The average of price is "+str(df["price"].mean()))
#specifiying the column label as price and calculating the average using the mean method

#3.b:
print("The list of different types of VehicleType found in dataset are "+str(df['vehicleType'].unique()))
print("Alternatively, the list of different types of VehicleType found in the dataset along with the count is: \n"+str(df['vehicleType'].value_counts()))


#3.c:
#Initially, if the max() method is used with the dataframe with column mentioned as yearOfRegistration, it gives 9999.0
#This is because NaN (which is what the blank cells are assigned with), are considered as 9999, which reduces the accuracy
#Therefore, we first check to see if there are any missing cells
# Checking for missing values in the column
miss_val = df['yearOfRegistration'].isna().sum()
#print('Number of missing values in the column:', miss_val)



# Finding the maximum and minimum yearOfRegistration
max = df['yearOfRegistration'].max()
min = df['yearOfRegistration'].min()


#Displaying
print('The maximum yearOfRegistration:', max)
print('The minimum yearOfRegistration:', min)

'''
#3.d:
#the same logic for missing cells applies for standard deviation as well
#print('Number of missing values in the column:', miss_val)
print(str(df['kilometer'].std()))
'''

#3.e:
df.brand.value_counts().sort_values().plot(kind='bar')
#selecting column brand from the dataframe and calculating the count.
#then sorting the values and plotting them with kind set to 'bar'
#using matplotlib to show the graph
plt.show()

#3.f:
print("The vehicleType with maximum number of sales is limousine with "+str(df['vehicleType'].value_counts().max()))
print("The vehicleType with maximum number of sales is volkswagen with "+str(df['vehicleType'].value_counts().min()))

#3.g:
#selecting column brand from the dataframe and calculating the count.
#then sorting the values and plotting them with kind set to 'bar'
#using matplotlib to show the graph
df.gearbox.value_counts().sort_values().plot(kind='pie')
plt.show()