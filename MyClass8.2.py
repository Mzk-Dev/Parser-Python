class Transaction:
    def __init__(self,amount,date,currency='USD',usd_conv_rate=1,desc=None):
        self.__amount=amount
        self.__date=date
        self.__currency=currency
        self.__usd_conv_rate= usd_conv_rate
        self.__desc=desc

        @property
        def amount(self) :
            return self.__amound

        @property
        def date(self) :
            import datetime
            self.__date=datetime.date.today()
            return self
        
        @property
        def currency(self):
            return self.__currency

        @property
        def usd_conv_rate(self) :
            return self.__usd_conv_rate

        @property
        def desc(self):
            return self.__desc

        @property
        def usd(self):
            return (self.__amound*self.__usd_conv_rate)

class Account :
    def __init__ (self,number,name,Transaction_list=None):
        self.__number=number
        self.__name=name
        if not Transaction_list:
            Transaction_list=[]
        if all([isinstance(trans,Transaction) for trans in Transaction_list]):
            self.trans_list=Transaction_list
        else:
            raise TypeError


    @property
    def number(self):
        return self.__number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        assert len(name) >= 4
        self.__name = name


    def __len__(self, Transaction_list):
        return len(Transaction_list)

    @property
    def all_usd(self):
        b=True
        for i in self.__Transaction_list:
            if i.currency != 'USD':
                return False
        return b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
