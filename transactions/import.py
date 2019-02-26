from __future__ import absolute_import

from lib.ofxparse import OfxParser

def import_ofx(file):
    ofx = OfxParser.parse(file)
    print ("Account: ", str(ofx.account))
    
    account = ofx.account
    
    print(account.account_id)        # The account number
    print(account.routing_number)    # The bank routing number
    print(account.branch_id)   # Transit ID / branch number
    print(account.type)  # An AccountType object
    print(account.statement)  # A Statement object
    print(account.institution)  # An Institution object
    print("Institution")
    print(account.institution.organization)
    print(account.institution.fid)
    print("Statement")
    statement = account.statement
    print(statement.start_date       )   # The start date of the transactions
    print(statement.end_date         )   # The end date of the transactions
    print(statement.balance          )   # The money in the account as of the statement date
    print(statement.available_balance)   # The money available from the account as of the statement date
    print ("Transactions")
    
    for transaction in statement.transactions:
        print("T")
        print(transaction.payee)
        print(transaction.type)
        print(transaction.date)
        print(transaction.amount)
        print(transaction.id)
        print(transaction.memo)
        print(transaction.sic)
        print(transaction.mcc)
        print(transaction.checknum)

if __name__== "__main__":
    file = open('sample.ofx')
    import_ofx(file)