# Election_Analysis

## Overview 

The purpose of the Election Analysis is to create an audit file to certify the results of the US Congressional Race in Colorado.

The information in this report is useful to determine/confirm the winning candidate based on vote count. The report also includes a count of total votes with a breakdown by Candidate and County in the congressional district.

The analysis was conducted by using a python script to read and analyze the raw election file and create output in the form of a text file and display to the terminal.

Following is the link to the python script: [PyPoll_Challenge.py](https://github.com/rciminera/Election_Analysis/blob/main/PyPoll_Challenge.py)

Following is the link to the source data file: [election_results.csv](https://github.com/rciminera/Election_Analysis/blob/main/Resources/election_results.csv) 


## Election-Audit Results: 

Following are the results of the election:

- 369,711 total votes were cast.
-	There were 3 counties represented in the election:
	- Jefferson with 38,855 votes representing 10.5% of the total votes.
	- Denver with 306,055 votes representing the majority the votes with 306,055 votes and 82.8% of the total votes.
	- Arapahoe with 24,801 votes and 6.7% of the total
-	Denver had the largest turnout by a significant margin
-	There were 3 candidates in the election:
	- Charles Casper Stockham with 85,213 votes representing 23.0% of the total votes counted.
	- Diana DeGette had the majority of votes at 272,892 and 73.8% of the total.
	- Raymon Anthony Doane had 11,606 votes with 3.1% of the total
-	The winner of the Congressional Election was Diana DeGette

Below is a screen print of the terminal output:

![GitHubLogo](https://github.com/rciminera/Election_Analysis/blob/main/Resources/PyPoll_Challenge%20Print%20to%20Terminal.png)

The output text file can be found here: [election_results.txt](https://github.com/rciminera/Election_Analysis/blob/main/Results/election_results.txt)


## Election-Audit Summary: 

This analysis is an efficient tool that can be used in other elections to quickly determine the distribution of votes from an election data source.  This information could be highly useful for monitoring and certifying the results of any election provided that the data is reliable from the source.

This script can be modified as follows:

-	Can be used for any local, state, and federal elections provided the information is in a CSV file.
-	It can report on additional data elements such as political party or any other data that can be obtained in an input file.
-	Different analyses can also be done.  For example, an analysis of votes by candidate by geography can be created as well as any other similar reports.
-	These reports can be standardized to run not only to certify the final result of an election but can also be run at will during the election event to monitor the race as the votes come in.

