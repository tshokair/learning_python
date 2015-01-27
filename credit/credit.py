balance= input("Initial Balance?")
interest_rate= input("Annual Interest Rate?")
min_pay_rate=input("Minimum Monthly Payment Rate?")

def calc_min_pay(bal):
    return round(float(bal),2)*round(float(min_pay_rate),2)
def interest_paid(bal):
    return round(float(interest_rate)/12*float(bal),2)
def principal_paid(paid,bal):
    return round(float(paid)-interest_paid(bal),2)
def remaining_balance(bal, paid):
    return round(float(bal)-principal_paid(paid, bal),2)
total,k=0,1
while k<=12:
    print("Month ",k)
    min_payment=calc_min_pay(balance)
    total+=round(min_payment,2)
    print("Minimum Monthly Payment ",min_payment)
    principal=principal_paid(min_payment,balance)
    print("Principal Paid ",principal)
    balance=remaining_balance(balance,min_payment)
    print("Remaining Balance ",balance)
    
    k=k+1

print ("Total paid ", round(total,2))
print("Remaining balance ", balance)