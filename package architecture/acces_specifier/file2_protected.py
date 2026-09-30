class BankAccount:
    bank_name="sbi"
    _interest_rate=5     #protected CV

    def __init__(self,cname,accno):
        self.cname=cname   #public
        self._accno=accno   #protected IV

    def _calculate_interest(self,amount):       #protected IM
        return (self._interest_rate*amount)/100  #access protected CV inside protected IM


class SavingsAccount(BankAccount):
    def show_interest(self,amount):
        print(self._calculate_interest(amount))  #access protected IM from the child class


sa=SavingsAccount("abc",177123)
sa.show_interest(500000)
print(sa._accno) #access protected  IV outside the class




        