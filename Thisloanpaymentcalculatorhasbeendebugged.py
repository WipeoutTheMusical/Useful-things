print("Hello, today we're going to calculate your auto loan payment.")
print("This calculator will also determine if you can afford the car based in 10% of your monthly income.")
print("Let's get started.")

class autoLoan:
    def __init__(self, principle, rate, income, term):
        self.principle = principle
        self.rate = rate
        self.income = income
        self.term = term

    def calculateAutoLoan(self):
        termMonths = term * 12
        monthPercent = rate / 12
        decimalRate = (monthPercent / 100)
        decimalRatePlusOne = decimalRate + 1
        newDecimalRate = (decimalRatePlusOne ** termMonths) - 1
        newNewDecimalRate = decimalRate/newDecimalRate
        almostPayment = newNewDecimalRate + decimalRate
        carPayment = almostPayment * principle
        if carPayment > (income / 12) / 10:
            print("Your payment is ", carPayment , " per month.")
            print("You cannot afford the payment on this car")
        else:
            print("Your payment is ", carPayment , " per month.")
            print("You can afford the payment on this car.")

principle = int(input("How much are you financing?"))
rate = float(input("What is the annual rate on your loan?"))
income = int(input("How much do you make in a year, rounded to the nearest dollar?"))
term = int(input("How many years are you going to finance for?"))
loan = autoLoan(principle, rate, income, term)

loan.calculateAutoLoan()
