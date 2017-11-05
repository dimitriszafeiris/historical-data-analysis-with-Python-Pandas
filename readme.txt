#Analyzing Historical data to find out if we could implement a caching layer or not

A company wants to optimize its? services, in order search results to return quicker to visitors. 

They will implement a caching layer between their server and all airlines servers.

If search result exists in cache database, entry will be appeared to visitor (without searching at airlines).

We will analyze historical data of Company, in order to find cache hit ratio, if caching logic was implemented in the past.

If this number is above 0.20, we will propose management team to proceed with caching layer.


We will load-use the whole dataset.
Dataset count rows is stored at variable A.
For each record exists in cache database, variable  B will be increased by 1.
Cache hit ratio is B/A.
If it is above 0.20, we will proceed with the implementation.

We will use Python big data practices to analyze this large amount of data.
We will create a Python program, named analysis.py.
Python library Pandas will be used.

Download gzip files and create one single csv file (dataset.csv).
Create 2 dataframes using Pandas, including all historical data (2nd one is just for iteration purposes).
Initiate 3 variables, to help you calculate cache hit ratio.
	Total count of datasets rows.
	Number of cache hits(zero at first)

Iterate through full dataset and check one by one iteration dataframe.
Check only if row is within 30 minutes.
Check all prerequisites indexes at our row and at iteration current dataframe row.

Every time a cache hit found:
Increase specific counter by one.
Exit second loop, cache hits will be unique.
Cache hit ratio will be:
	cache hits founds / total searches

Inform management team about our findings and propose the best solution.

