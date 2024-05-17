# HW2
# Date: 09/25/2021
# Ryan Talalai

import random

class Course:
    def __init__(self, cid, cname, credits):
        self.cid = cid
        self.cname = cname
        self.credits = credits
               


    def __str__(self):
        return f'{self.cid}({self.credits}): {self.cname}'

    __repr__ = __str__

    def __eq__(self, other):
        if other != None:    
            if self.cid == other.cid:
                return True
            else:
                return False
        else:
            return False



class Catalog:
    def __init__(self):
        self.courseOfferings = dict()


    def addCourse(self, cid, cname, credits, capacity):
        self.cid = cid
        self.cname = cname
        self.credits = credits
        self.capacity = capacity
        
        if self.cid in self.courseOfferings:
            return 'Course already added'
        else:
            self.courseOfferings[self.cid] = Course(self.cid, self.cname, self.credits), self.capacity
            return 'Course added successfully'


    def removeCourse(self, cid):
        self.cid = cid

        if self.cid in self.courseOfferings:
            del self.courseOfferings[self.cid]
            return 'Course removed successfully'
        else:
            return 'Course not found'


class Semester:
    def __init__(self, sem_num):
        self.sem_num = sem_num
        self.courses = dict()
        self.total_credits = 0
        self.cid_lst = []



    def __str__(self):
        if self.courses == {}:
            return 'No courses'
        else:            
            cids = ', '.join(self.cid_lst)
            return cids


    __repr__ = __str__


    def addCourse(self, course):
        self.course = course
        if self.course.cid in self.courses:
            return 'Course already added'
        else:
            self.courses[self.course.cid] = self.course
            self.total_credits += self.course.credits
            self.cid_lst.append(self.course.cid)



    def dropCourse(self, course):
        self.course = course
        if self.course.cid in self.courses:
            del self.courses[self.course.cid]
            self.total_credits -= self.course.credits
            self.cid_lst.remove(self.course.cid)
        else:
            return 'No such course'
    


    @property
    def totalCredits(self):
        return self.total_credits


    @property
    def isFullTime(self):
        if self.total_credits >= 12:
            return True
        else:
            return False


    
class Loan:
    def __init__(self, amount):
        self.amount = amount
        self.loan_id = self.__getloanID
        


    def __str__(self):
        return f'Balance: ${self.amount}'

    __repr__ = __str__


    @property
    def __getloanID(self):
        loan_id = random.randint(10000,99999)
        return loan_id



class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn


    def __str__(self):
        return f'Person({self.name}, ***-**-{self.get_ssn()})'

    __repr__ = __str__


    def get_ssn(self):
        lst = list(self.ssn)
        ssn_lst = [lst[7], lst[8], lst[9], lst[10]]
        self.last_four = ''.join(ssn_lst)
        return self.last_four


    def __eq__(self, other):
        if isinstance(other, Person) == True:
            if self.ssn == other.ssn:
                return True
            else:
                return False
        else:
            return False



class Staff(Person):
    def __init__(self, name, ssn, supervisor=None):
        self.supervisor = supervisor
        Person.__init__(self, name, ssn)


    def __str__(self):
        return f'Staff({self.name}, {self.id})'
        

    __repr__ = __str__


    @property
    def id(self):
        lst = self.name.split()
        lst2 = []
        for num in range(0,len(lst)):
            name = lst[num]
            name = list(name)
            lst2.append(name[0].lower())
        initials = ''.join(lst2)
        
        return f'905{initials}{self.get_ssn()}'
        

    @property   
    def getSupervisor(self):
        return self.supervisor


    def setSupervisor(self, new_supervisor):
        if isinstance(new_supervisor, Staff):
            self.supervisor = new_supervisor
            return 'Completed!'


    def applyHold(self, student):
        self.student = student
        if isinstance(self.student, Student):
            self.student.hold = True
            return 'Completed!'


    def removeHold(self, student):
        self.student = student
        if isinstance(self.student, Student):
            self.student.hold = False
            return 'Completed!'


    def unenrollStudent(self, student):
        self.student = student
        if isinstance(self.student, Student):
            self.student.active = False
            return 'Completed!'


    def createStudent(self, person):
        self.person = person
        return Student(self.person.name, self.person.ssn, 'Freshman')




class Student(Person):
    def __init__(self, name, ssn, year):
        random.seed(1)
        Person.__init__(self, name, ssn)
        self.year = year
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()
        self.count = 0
        self.sem = ''

    def __str__(self):
        return f'Student({self.name}, {self.id}, {self.year})'


    __repr__ = __str__

    def __createStudentAccount(self):
        if self.active == True:
            return StudentAccount(self)



    @property
    def id(self):
        lst = self.name.split()
        lst2 = []
        for num in range(0,len(lst)):
            name = lst[num]
            name = list(name)
            lst2.append(name[0].lower())
        initials = ''.join(lst2)
        
        return f'{initials}{self.get_ssn()}'



    def registerSemester(self):
        if self.active == True and self.hold == False:
            self.count += 1
            self.sem = Semester(self.count)
            self.semesters[self.count] = self.sem
            if self.count > 0 and self.count < 3:
                self.year = 'Freshman'
            elif self.count > 2 and self.count < 5:
                self.year = 'Sophomore'
            elif self.count > 4 and self.count < 7:
                self.year = 'Junior'
            elif self.count > 6:
                self.year = 'Senior'
        else:
            return 'Unsuccessful operation'



    def enrollCourse(self, cid, catalog, semester):
        self.cid = cid
        self.catalog = catalog
        self.semester = semester

        if self.active == True and self.hold == False:
            if self.cid in self.catalog.courseOfferings:
                course_obj = self.catalog.courseOfferings[self.cid][0]
                if self.cid in self.sem.courses:
                    return 'Course already enrolled'
                else:
                    self.sem.addCourse(course_obj)
                    self.account.balance += StudentAccount.CREDIT_PRICE * course_obj.credits
                    return 'Course added successfully'
            else:
                return 'Course not found'

        else:
            return 'Unsuccessful operation'



    def dropCourse(self, cid):
        self.cid = cid

        if self.active == True and self.hold == False:
            if self.cid in self.sem.courses:
                course_obj = self.catalog.courseOfferings[self.cid][0]
                self.sem.dropCourse(course_obj)
                self.account.balance -= 0.5 * StudentAccount.CREDIT_PRICE * course_obj.credits
                return 'Course dropped successfully'
            else:
                return 'Course not found'

        else:
            return 'Unsuccessful operation'


    def getLoan(self, amount):
        self.amount = amount
        if self.active == False:
            return 'Unsuccessful operation'
        if self.sem.isFullTime == False:
            return 'Not full-time'
        
        loan_obj = Loan(self.amount)
        self.account.loans[loan_obj.loan_id] = loan_obj
        self.account.makePayment(self.amount)



class StudentAccount:    
    CREDIT_PRICE = 1000

    def __init__(self, student):
        self.student = student
        self.balance = 0
        self.loans = {}


    def __str__(self):
        return f'Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}'

    __repr__ = __str__


    def makePayment(self, amount):
        self.amount = amount
        self.balance -= self.amount
        return self.balance
        

    def chargeAccount(self, amount):
        self.amount = amount
        self.balance += self.amount
        return self.balance