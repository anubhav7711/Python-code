class account:
    def __init__(self,accno,accpass):
        self.accno=accno
        self.__accpass=accpass#private

    def resetpass(self):
        print(self.__accpass)

acc1=account("23964","hemant@12")
print(acc1.accno)
acc1.resetpass()