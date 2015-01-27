balance_in= input("Initial Balance?")
balance=float(balance_in)
interest_rate_in= input("Annual Interest Rate?")
interest_rate=float(interest_rate_in)
monthly_interest=float(interest_rate)/12


def updated_balance(bal,payment):
    return round((bal*(1+monthly_interest)-payment),2)

l=1
up_bal=balance
lower_bisect=balance/12
upper_bisect=balance*(1+monthly_interest)**12/12
epsilon=.01
done_flag=0
num_iterations=0
print("range (",lower_bisect,",",upper_bisect,")")
while done_flag==0:
    num_iterations+=1
    up_bal=balance
    num_Months, k=0, 1
    pay_guess=(upper_bisect-lower_bisect)/2+lower_bisect
    pay_guess=round(pay_guess,2)
    ###print(pay_guess)
    while k<=12:
        up_bal=updated_balance(up_bal,pay_guess)
        k=k+1
        num_Months+=1
        if up_bal>=(-1*epsilon) and up_bal<=0:
            paid_in=num_Months
            final_balance=up_bal
            final_payment=pay_guess
            done_flag=1
            k=13
    if up_bal>epsilon:
        lower_bisect=pay_guess
    else:
        upper_bisect=pay_guess
    l=l+1
print("Remaining balance is", final_balance,"months with a payment of",final_payment)
print("Answer found in",num_iterations,"iterations")