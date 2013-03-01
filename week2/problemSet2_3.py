# config #########
balance = 999999
annualInterestRate = 0.18
# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 90325.07
##################

epsilon = 0.001
monthlyInterestRate = annualInterestRate/12.0
lower = balance/12.0
upper = (balance * ((1 + monthlyInterestRate)**12))/12

while True:
    ans = (lower + upper)/2
    remBalance = balance
    for month in range(12):
        remBalance = remBalance - ans
        remBalance = remBalance + (remBalance * monthlyInterestRate)
    if abs(remBalance) <= epsilon:
        break
    elif remBalance > 0:
        lower = ans
    elif remBalance < 0:
        upper = ans
print(str(round(ans, 2)))
