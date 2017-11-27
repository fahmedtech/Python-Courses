'''
Lab 4.5 Pre-Midterm
SOLUTIONS
'''

#Problem 1: class Worker(), HourlyWorker() & SalariedWorker()

class Worker(object):

    def __init__(self, str_name):
        self.name = str_name

class HourlyWorker(Worker):

    def __init__(self, name, rate):
        Worker.__init__(self, name)
        self.rate = rate

    def pay(self, hours):
        if(hours > 40):
            return 40 * self.rate + (hours -40) * 1.5 * self.rate
        else:
            return hours * self.rate

class SalariedWorker(Worker):

    def __init__(self, name, salary):
        super(self.__class__, self).__init__(name)
        self.salary = salary

    def pay(self):
        return self.salary

#Problem 2: myList() extends list - overriding

class myList(list):

    def sort(self):
        print('You wish..')

    def __len__(self):
        return sum(self)
