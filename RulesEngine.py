import json


class RulesEngine:
    def __init__(self):
        self.testCases = None
        self.actionRules = None

    def load_ruleset(self, jsonfile):
        rulesfile = open(jsonfile)
        actiontests = json.load(rulesfile)
        self.actionRules = actiontests["ActionRules"]
        self.testCases = actiontests["TestData"]

    def run_rules(self, person, product):
        exec(self.actionRules['Qualify'].format(), globals())
        product.disqualified = productQualify(person.residence)
        exec(self.actionRules['Interest']['RateCal'].format(InitialRate=self.actionRules['Interest']['Initial']), globals())
        product.interest = rateCalculation(person.credit, product.loan)

    def test_rules(self):
        success = 0
        fail = 0
        exec(self.actionRules['Qualify'].format(), globals())
        exec(self.actionRules['Interest']['RateCal'].format(InitialRate=self.actionRules['Interest']['Initial']), globals())

        # Test the final rate calculation based on credit score
        for each in self.testCases['CreditScores']:
            fr = rateCalculation(each['Credit'], each['LoanType'])
            if fr != each['ExpectedRate']:
                print("Test failed for scenario \n" + str(each) + "\nCalculated rate is " + str(fr))
                fail += 1
            else:
                print('Scenario Pass ' + str(each))
                success += 1
        print("Pass: {} \tFail: {}".format(success, fail))

        # Test the disqualification of loan based on state residency
        for each in self.testCases['Qualified']:
            pq = productQualify(each['Residence'])
            if pq != bool(each['ExpectedQual']):
                print("Test failed for scenario \n" + str(each))
                fail += 1
            else:
                print('Scenario Pass ' + str(each))
                success += 1
        print("Pass: {} \tFail: {}".format(success, fail))

        # Test the final interest rate based on the loan type and credit score.
        for each in self.testCases['LoanType']:
            fr = rateCalculation(each['Credit'], each['LoanType'])
            if fr != each['ExpectedRate']:
                print("Test failed for scenario \n" + str(each) + "\nCalculated rate is " + str(fr))
                fail += 1
            else:
                print('Scenario Pass ' + str(each))
                success += 1
        print("Pass: {} \tFail: {}".format(success, fail))
