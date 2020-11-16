# Story
A junior developer has implemented a feature that will parse a csv file containing product inventories of different categories for a set of companies. The feature then sums the inventories for each company and outputs each of the sums that falls within a provided list of ranges as both a list and a string. Their code is not working and they've asked you to help them debug it. Find the bugs in the parse and the new_function function, and suggest to them some practices they can use to write bug-free code and prevent regressions. Advise them on how they would apply these practices to prevent such problems in the future and show how code problems should be investigated and solved.

## The Problem
Given a CSV file, when the user inputs a list of ranges, then feature.py outputs all the total inventories that fall within those ranges in a list and a string. In the following **example**, given the following small CSV file, when the user demands total inventories between ranges 2200 to 2500 and 3000 to 3300, feature.py outputs [2353,2240,3013] and '2353 2240 3013 '. Please note that this is just an example and does not cover all possible test cases. You are encouraged to come up with tests and write them if possible. Feel free to ask any questions. 

CSV file:   
Company No.,Groceries,Confectionaries,Pharamceuticals,Stationary  
0,662,640,828,402  
1,848,534,758,757  
2,820,669,602,704  
3,792,557,502,502  
4,948,623,668,658  
5,437,573,602,628  
6,780,838,711,649  
7,972,672,767,602  
8,604,647,588,676  
9,943,824,554,532  

Input:
[(2200,2500),(3000,3300)]

Process:
Find the sum of the rows to find the total inventory of each company. Then pick out the ones that fall in he specified ranges.

total_inventories: [2532, 2897, 2795, 2353, 2897, 2240, 2978, 3013, 2515]

Expected Output:
([2353, 2240, 3013], '2353 2240 3013')

**Note**: The list output can be changed as long as the information about the total_inventories is included.

### Files
 * large_data.csv: A CSV file that conains the inventories of numerous companies in differnet catefories like Groceries,Confectionaries,Pharamceuticals, and Stationary. Please note that this is file is much larger than the data.csv file you were provided in the take home assignment and the companies are identified by numbers instead of names.
 * feature.py: A file that parses this CSV file, sums the rows and finds the the total inventories within a set of given ranges. It contains a main and 3 helper functions which perform the 3 functions mentioned here. Please refer to the individual function definitions to further understand them.
