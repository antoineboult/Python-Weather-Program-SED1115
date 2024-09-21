The program answers this question : Since I hate wearing winter boots, what are the months of the year that I would absolutely hate?
you can find my python and my csv files for this python weather program. My program reads through specific columns of the csv file that I consider important for the purpose the question.
The columns that I find important are : Day, Month, Snowfall, Groundsnow
All of these serve a purpose for my program since I need to determine if each day of the year is considered a day where I need to wear winter boots. 
It reads month by month, day by day (the use of Day, Month).
Than I need to have a bootday count that will help to determine if the month is a month that I would hate. 
To be a bootday (add 1 to the count), the values of the day has to follow these conditions : SnowfallList > 0 or GroundsnowList > 0.
After each month, if it's bootcount is > 5 bootdays, the value of the month gets appended to the hatedmonths list.
The value of the months gets converted to the actual name of the months by firstly having the dictionary that associates the number of the month to it's name.
Then, I replaced the value of the month to the name of the month associated to it from the dictionary.
Then, I made a new variable that converts the list into a string that will make it more beautiful when I print it
When the loop has went through all 12 months, it will print the a string that includes a context sentence and the variable that has the list converted into a string.
