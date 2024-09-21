import pandas as pd

# Read my CSV file and prints it's data frame
# You can replace the "daily_data_2023.csv" part by your own csv file name if you wanted to try this program on an other data file
df = pd.read_csv("daily_data_2023.csv", usecols=["Day", "Month", "Totalsnow", "Snowground"])
print(df)

# I Assigned the columns that I needed to read through to an new name to make it easier to reference in the future of my code.
# You can adapt the names of the variables to your own specific columns that you want to rename for later use
MonthList = df.Month
DayList = df.Day
SnowfallList = df.Totalsnow
GroundsnowList = df.Snowground

# I made a dictionnary to store my bootday count, it keeps record of the bootday at each day of the month 
bootday_count = {month: 0 for month in range(1, 13)}

# The conditions to the SnowfallList and GroundsnowList values to determine if it is a bootday, if it is true than the bootday count increases by one for the mont, else it just continues
for i in range(len(df)):
    if SnowfallList[i] > 0 or GroundsnowList[i] > 0:  # New condition for boot days
        bootday_count[MonthList[i]] += 1
    else: 
        continue

# This is the list where the months that have a bootday count higher than five will be appended to. It starts with nothing in it.
hatedmonths = []

# It checks for each month if the bootday count is higher than 5, if it does it adds the value of the month to the hatedmonths list
for month, count in bootday_count.items():
    if count > 5:
        hatedmonths.append(month)

# Created a dictionary since the months are represented by only numbers like 1,2,3,4... I want to attribute for each the name of the month. Like 1 is January, 2 is February etc... 
# This way I will be able to print the name of the month at the very end and not the number of the month. 
month_names = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

# This is converts the value of the months which are in numbers into their actual name by using the dictionary that I made. It is still in a list
hatedmonths_named = [month_names[month] for month in hatedmonths]

# This converts my list into a simple string, this is only to make it more beautiful for the print.
hatedmonths_str = ", ".join(hatedmonths_named)

# This finally prints the string (was a list but I converted it into a string) and a string before that gives context to why there will be name of months.
print("The months of the year that I will absolutely hate because I have to wear winterboots are: ", hatedmonths_str)


