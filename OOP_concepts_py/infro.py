class Employee:
    'The base class class for Employee'
    #Class attributes
    #emplyoeeAge = 30
    payRate = 100
    relateives = []
    K = "K"

    #This is initializer method when a new obj is created.
    def __init__(self, emplyeeAge):
        #Declare som data attributes
        self.firstName = 'James'
        self.lastName = 'Ddd'
        self.uid = '521'
        self.employeeAge = 10

    def operation01(self):
        pass

    def operation02(self):
        pass

    def operation03(self):
        pass

def main():
    # getting values of class attributes
    print("Pay rate: {}".format(Employee.payRate))

    #creating objects
    employee_01 = Employee(56)
    #sposoby wyświetlania precyzji
    print("To jest emplyee age: '%02.2f' " % (employee_01.employeeAge))
    print("To jest emplyee age: '{:02.2f}' ".format(employee_01.employeeAge))
    print(Employee.K +'k')



main()

