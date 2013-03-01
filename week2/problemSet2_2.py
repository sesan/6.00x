# config #########
balance = 4773
annualInterestRate = 0.2
# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 310
##################

monthlyInterestRate = annualInterestRate/12.0
month = 0
step = 10
ans = 10
remBalance = balance


while remBalance > 0:
    if month == 0:
        remBalance -= ans
        month += 1
    elif month <= 11:
        remBalance += (remBalance * monthlyInterestRate)
        remBalance -= ans
        month += 1
    else:
        remBalance = balance
        ans += step
        month = 0
print(str(ans))
