# Inheritance (Kalıtım): Miras alma

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person created!')
    
    def who_am_i(self):
        print("I'm a person.")

    def eat(self):
        print("I'm eating.")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student created!')

    # override
    def who_am_i(self):
        print('I am a student.')

    def sayHello(self):
        print('Hello!')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher.')


p1 = Person('Mehmet', 'Derin')
s1 = Student('Yağız', 'Derin', 1234)
t1 = Teacher('Duygu', 'Koca', 'English')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))
print(t1.firstName + ' ' + t1.lastName + ' ' + t1.branch)

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()
s1.sayHello()