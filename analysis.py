#Author: Dimitris Zafeiris
#Version: 1.0
#Created: 04/11/2017

#Starting analysing historical data process

#Import pandas and numpy libraries
import pandas as pd
import numpy as np

#Create dataframe df_entries, including all search historical entries
df_entries = pd.read_csv('dataset.csv')

#Create dataframe df_iterate_entries, including all search historical entries for iterate
df_iterate_entries = pd.read_csv('dataset.csv')

#Initiate variables
count_entries = df_entries.count() # counter of full dataset
count_iterate_entries = df_iterate_entries.count() # counter of full iterate dataset
cached_hit_entries = 0 # variable to help us calculate cache hit ratio

#For every row, we will search if it has a matching in cache layer
for i=0 in count_entries:

	for j=0 in count_iterate_entries:
		#Check if i is not equal to j. If yes, we are at the same line, so no need to check
		if (i != j):
			#First check if time(column index 1) is less than 30 minutes. If not, no need to check at all
			if (df_entries.iloc[i][1] - 1800 <= df_entries.iloc[j][1]):

				#Check all other prerequisites if exists. All below have to be equal
				#Index 2: Origin_airport
				#Index 3: Destination_airpot
				#Index 4: Passengers
				#Index 5: Departure_date
				#Index 6: Return_date
				if (df_entries.iloc[i][2] == df_entries.iloc[j][2] and df_entries.iloc[i][3] == df_entries.iloc[j][3] df_entries.iloc[i][4] == df_entries.iloc[j][4] df_entries.iloc[i][5] == df_entries.iloc[j][5] df_entries.iloc[i][6] == df_entries.iloc[j][6])
					
					#We found a cache hit, so increase counter
					cached_hit_entries+=1
					#if we find a cache entry, exit second for loop
					break

#Calculate cache_hit_ratio
cache_hit_ratio = cached_hit_entries/count_entries

#Return the result to management team
if (cache_hit_ratio < 0.20 ):
	print (" It is not a good idea to implement caching layer. Our results shows that cache hit ratio is",cache_hit_ratio)
else if (cache_hit_ratio > 0.20):
	print ("It is a good idea to implement caching layer. Our results shows that cache hit ratio is",cache_hit_ratio)
else:
	print ("After our analysis on historical data, we found that cache hit ratio is exactly 0.20.")
