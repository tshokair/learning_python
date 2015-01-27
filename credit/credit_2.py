balance_in= input("Initial Balance?")
balance=float(balance_in)
interest_rate_in= input("Annual Interest Rate?")
interest_rate=float(interest_rate_in)
monthly_interest=float(interest_rate)/12


def updated_balance(bal,payment):
    return round((bal*(1+monthly_interest)-payment),2)

l=1
up_bal=balance
while up_bal>0:
    up_bal=balance
    num_Months, k=0, 1
    min_payment=l*10
    while k<=12:
        up_bal=updated_balance(up_bal,min_payment)
        k=k+1
        num_Months+=1
        if up_bal<=0:
            print(up_bal)
            paid_in=num_Months
            final_balance=up_bal
            final_payment=min_payment
            k=13

    l=l+1
print("Remaining balance ", final_balance, "paid in ", paid_in, "months with a payment of",final_payment)