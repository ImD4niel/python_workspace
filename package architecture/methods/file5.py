class Bank:
    @staticmethod
    def calculate_interest(principal,roi,time):
        return (principal*roi*time)/100


print(Bank.calculate_interest(1330,4,2.5))
b1=Bank()
print(b1.calculate_interest(3245,42,3))

