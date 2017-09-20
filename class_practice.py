class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last


    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    def __init__(self,first,last,pay):
        Person.__init__(self,first,last)
        self.pay="     "+str(pay)

    def desc(self):
        return self.Name()+(self.pay)
p=Person("Balaswamy","Addagatla")
e=Employee("raj","Krishna",50000)
f=Employee("Siva","Satya",50000)

print(p.Name())
print(f.desc())
