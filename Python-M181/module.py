class bankaccount:
    def __init__(self,cname,accno,balance):
        self.cname=cname
        self.accno=accno
        self.balance=balance
        print(f'Customer name is:{self.cname}')
        print(f'Account number is:{self.accno}')
        print(f'Bank balance is:{self.balance}')