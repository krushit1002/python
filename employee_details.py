class employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)

e1 = employee("accountant","finance","60,000")
e1.showdetails()
