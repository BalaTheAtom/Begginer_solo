class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    def __init__(self,first,last,pay):

        self.pay=pay
        return '{} {} and his pay is {}'.format(Person.first,Person.last,pay)
p=Person("Balaswamy","Addagatla")
# e=Employee("raj","Krishna",50000)

print(p.Name())
