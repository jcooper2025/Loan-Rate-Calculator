import PersonProduct
import RulesEngine

from optparse import OptionParser
import json



def person_prompt():
    """
    Prompt the user to enter the customer credit score and state where they live.
    :return:
        an integer and a string in a tuple.
    """
    score = int(input("Enter value for credit score (300-850): "))
    state = input("Enter the full name of the state of residence for the borrower: ")
    return score, state


def product_prompt():
    """
    Prompt the user to enter the loan type and initial interest rate percentage for the loan.
    :return:
        a string and a float in a tuple.
    """
    loan = input("Enter the name of the type of mortgage: ")
    rate = float(input("Enter a floating point value for the initial interest rate percentage: "))
    return loan, rate


def read_inputfile(datafile):
    """
    Reads in person and product data in from an input file. The expected format is json.
    :return:
        a tuple of newly created person and product objects.
    """
    datain = open(datafile)
    initial = json.load(datain)
    cust = PersonProduct.Person(initial["credit"], initial["state"])
    prod = PersonProduct.Product(initial["loan"], initial["rate"])
    return cust, prod


def main():

    actionrules = RulesEngine.RulesEngine()
    customer = None
    loansought = None

    # setup command line options
    usage = """
    Usage: %prog -r <rule json file> -T -i -d <data file input>
    Load the json file with the rules and action definitions. This file also holds the automated test
    data for the -T option. 
    For the input customer and product data, select the -i option to enter data at the prompts or -d
    and a file name for the input file (json format).
    """
    parser = OptionParser(usage=usage)

    parser.add_option("-r", action="store", type="string", dest="rulesfile",
                      help="Filename of rule set and actions to load.")
    parser.add_option("-T", action="store_true", dest="runtests", help="Run automated rule set tests.")
    parser.add_option("-i", action="store_true", dest="interactive",
                      help="Enter person and product information at the prompt.")
    parser.add_option("-d", action="store", type="string", dest="datafile",
                      help="Name of the file containing person and product data in json format.")

    (options, args) = parser.parse_args()

    if options.rulesfile:
        actionrules.load_ruleset(options.rulesfile)

    if options.interactive:
        (score, state) = person_prompt()
        (loantype, rate) = product_prompt()
        customer = PersonProduct.Person(score, state)
        loansought = PersonProduct.Product(loantype, rate)

    if options.datafile:
        (customer, loansought) = read_inputfile(options.datafile)

    if options.runtests:
        actionrules.test_rules()

    if customer:
        actionrules.run_rules(customer, loansought)

    if loansought:
        print("The interest rate for a " + loansought.loan + " loan is: " + str(loansought.interest))
        if loansought.disqualified:
            availability = "Disqualified"
        else:
            availability = "Qualified"
        print("This loan is " + availability + " in the state of " + customer.residence)


if __name__ == "__main__":
    main()
