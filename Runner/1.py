class Data_test2(object):
    day=0
    month=0
    year=0

    def __init__(self,year=0,month=0,day=0):
        self.day=day
        self.month=month
        self.year=year

    @classmethod
    def get_date(cls,string_date):
    #这里第一个参数是cls， 表示调用当前的类名
    	year,month,day=map(int,string_date.split('-'))
    	date1=cls(year,month,day)
    	#返回的是一个初始化后的类
    	return date1
    def out_date(self):
        print ("year :")
        print (self.year)

a = Data_test2.get_date('2017-12-02')
a.out_date()