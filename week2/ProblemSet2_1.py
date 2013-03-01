# config ########
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
##################

monthNum = 0
monthlyInterestRate = annualInterestRate/12.0
paidTot = 0

while balance >= 0:
    monthNum += 1
    minPayment = balance * monthlyPaymentRate
    balance = balance - minPayment
    balance += balance*monthlyInterestRate
    paidTot += minPayment
    print('Month: ' + str(monthNum))
    print('Minimum monthly payment: ' + str(round(minPayment, 2)))
    print('Remaining balance: ' + str(round(balance, 2)))
    if monthNum == 12:
          break
print('Total paid: ' + str(round(paidTot, 2)))
print('Remaining balance: ' + str(round(balance, 2)))
