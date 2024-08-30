def  search_by_date(transactions):
    date=input("enter date: ")
    for transaction in transactions:
        if transaction['date']==date:
            return transaction
    return "Transaction Not Found"

def sort_amount (transactions):
    n=len(transactions)
    for i in range(n):
        for j in range(n-1):
            if transactions[j]["amount"]>transactions[j+1]["amount"]:
                transactions[j],transactions[j+1]=transactions[j+1],transactions[j]
    return transactions

def add_data(transactions):
  dic={"date": input("enter the date: "),
       "amount": int(input("enter amount: ")),
       "desc":input("enter the desc: ")}
  transactions.append(dic)
  return transactions

def delet_date(transactions):
    date=input("enter date: ")
    for transaction in transactions:
        if date in transaction["date"]:
            transactions.remove(transaction)
    return transactions
    
def sum_amount(transactions):
    sum=0
    year=input("enter the year:")
    for transaction in transactions:
        if transaction['date'][0:4]== year:
            sum+=transaction['amount']
    return sum
