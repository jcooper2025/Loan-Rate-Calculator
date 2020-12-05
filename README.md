# Loan-Rate-Calculator
 This is my initial submission for a programming assignment as a part of the interview process.
 
 The assignment was to meet a business request to dynamically generate product pricing from a set of rules defined by the finance team. The finance team has provided an initial set of rules on how to price the product, however, these rules could change at any time so you need to be able to update the rules easily and rerun these product pricing to see the new prices of the products.
 
 The main code is in python (3.8.3) with the rules and test scenarios in external json files.
 The rules have been translated into python code stored in string format in the json structures. Because the rules are dynamic and can differ with each file, there are also test scenarios for each rule contained in the same file. These tests can be run at any time from the command line when the script is invoked.
 
All of the necessary files are included in the repo. To run the program locally you will need to have python installed. This was created with version 3.8.3 on macOS but there shouldn't be problems running on earlier versions of python3 or other OS's.

To run the program, download the repo as a zip file and extract it locally.
Change to the extracted directory and run the program from the command line:

$python LoanCalculator.py -h  This will show a help screen for the command.

$python LoanCalculator.py -r RuleSet_Initial.json -T  - will run the included tests.

$python LoanCalculator.py -r RuleSet_Initial.json -d input_file.json  - will run the rulesengine on the data in input_file.json

$python LoanCalculator.py -r RuleSet_Initial.json -i   - will allow the user to enter data for the customer and product being considered.

The initial rules provided in the problem description are in RuleSet_Initial.json.
1. All products start at 5.0 interest rate.
2. If the customer lives in Florida they are disqualified from this product.
3. A credit score greater than or equal to 720 means reduce the interest rate by 0.3.
4. A credit score of less than 720 adds 0.5 to the interest rate.
5. If the customer is seeking a '7-1 ARM' loan then add a further 0.5 to the loan interest.

An sample input set for these rules would be: 
Credit Score - 725; 
Residence - New York; 
Loan Type - Standard; 
Interest Rate - 5.0

The expected results would be and interest rate of 5.4 and that the customer is not Disqualified for this product.
The expected results for the input_file.json data is a rate of 5.5 and that the customer is not Disqualified for this product.

A further requirement of the problem is to demonstrate the the ability to change the rule set and actions. These rules and the accompaning test scenarios are in the RuleSet_02.json and input_02.json files.
The rules are:
1. If a customer lives on Florida or California they are disqualified from this product.
2. If their credit score is less than 710, add 0.8 to the interest rate.
3. If their credit score is between 710 and 729, add 0.4 to the base interest rate.
4. If their credit score is 760 or above, subtract 0.3 from the base rate.
5. If the loan type is '7-1 ARM', add 0.5 to the interest rate.
6. If the loan type is '5-5 ARM', add 0.6 to the interest rate.

A sample input set for these rules would be:
Credit Score - 705;
Residence - Washington;
Loan Type - '5-5 ARM';
Interest Rate - 5.0

The expected results for this manual input with RuleSet_02.json are an interest rate of 6.4 and that the customer is not Disqualified for this product.
The expected results for input_02.json are an interest rate of 6.0 and that the customer is Disqualified from this product.
