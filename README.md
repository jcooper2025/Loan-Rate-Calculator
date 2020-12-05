# Loan-Rate-Calculator
 This is my initial submission for a programming assignment as a part of the interview process.
 
 The assignment was to meet a business request to dynamically generate product pricing from a set of rules defined by the finance team. The finance team has provided an initial set of rules on how to price the product, however, these rules could change at any time so you need to be able to update the rules easily and rerun these product pricing to see the new prices of the products.
 
 The main code is in python (3.8.3) with the rules and test scenarios in external json files.
 The rules have been translated into python code stored in string format in the json structures. Because the rules are dynamic and can differ with each file, there are also test scenarios for each rule contained in the same file. These tests can be run at any time from the command line when the script is invoked.
 
All of the necessary files are included in the repo. To run the program locally you will need to have python installed. This was created with version 3.8.3 on macOS but there shouldn't be problems running on earlier verions of python3 or other OS's.
