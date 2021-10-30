# Election Analysis


 
## Overview of Election Audit
We have been tasked with completing the following tasks for the Colorado Board of Elections in order for them to complete an audit of their recent local congressional election.  The Board of Elections need us to complete the following tasks so that they can successfully complete their audit.
  
  1.Calculate the total amount of votes casted.\
  2.Get a complete list of candidates who received votes.\
  3.Calculate the total amount of votes each candidate received.\
  4.Calculate the percentage of total votes each candidate received.\
  5.Determine the winner of the election based off of the popular vote.\
  6.Get a complete list of the counties where the votes were casted.\
  7.Calculate the amount of votes casted by county.\
  8.Calculate the percentage of total votes casted by each county.\
  9.Determine the county with the largest voter turnout based on the amount of votes casted.
  

## Election Audit Results

 Our analysis of the election showed that:
 
   * There were 369,711 total votes casted in this election.
   * The three candidates were:Charles Casper Stockham, Dianna DeGette, Raymon Anthony Doan
   * Charles Casper Stockham received 23.0% of the total votes and 85,213 votes total.
   * Diana DeGette received 73.8% of the total votes and 272,892 votes total.
   * Raymon Anthony Doane received 3.1% of the total votes and 11,606 votes total.

   * Diana DeGette was the winner of the election receiveing 272,892 votes, 73.8% of the total votes casted.
   
   * On a county by county breakdown, Jefferson County had 38,885 votes (10.5%), Denver county had 306,055 votes (82.8%), and Arapahoe County had 24,801 votes (3.1%)
  
A summary of the voting results can be found below

<img width="1085" alt="Screen Shot 2021-10-30 at 2 19 56 PM" src="https://user-images.githubusercontent.com/87248687/139554035-cba107f1-4bab-4a53-96d3-66015ea91343.png">


## Election Audit Summary

As we have seen from running this script with the data from this previous election, this is an extremely fast and efficient way to analyze the results from this election as well as for any future election as well.  I would propose to the election commission that they adopt using this same script for future elections.  Due to the way this script was composed, it is very simple to apply to any other election.  If we were to receive another election data csv file for a different election, we would just have to simply update the file path in our script to include the location and name of the csv file for the new election.  We would also  update the file path for the text file where we would write our analysis to.  

<img width="547" alt="Screen Shot 2021-10-30 at 2 27 44 PM" src="https://user-images.githubusercontent.com/87248687/139554242-650d73a8-19b5-4387-9a03-70a962f6bf89.png">

Once that has been updated, the last thing we would have to do is to check the csv file in order to see which column contained the county names and which column contained the candidates name.  Once we do that, we can simply update our script to extract the candidate name and county from each row by changing the index number inside row[] to correspond with the column that contain those values.

<img width="994" alt="Screen Shot 2021-10-30 at 2 39 48 PM" src="https://user-images.githubusercontent.com/87248687/139554901-b4896926-064d-4050-bec3-fa94eaf5cc8b.png">


## Resources
 * Data Source: elections_results.csv
 * Software: Python and Visual Studio Code
