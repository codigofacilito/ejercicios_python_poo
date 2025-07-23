from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self):
        self.person_id =0
        self.name =""
        self.address="" 
        self.email =""
        self.phone_number =""

    @abstractmethod
    def getBasicDetails(self):
        pass


class Teacher(Person):
    def __init__(self, salary,specialty,start_time):
        self.salary = salary
        self.specialty = specialty
        self.__start_time = start_time 

    def getBasicDetails(self):
        print("Nombre: ",self.name,"\nDireccion: ",self.address,"\nCorreo:"
              ,self.email,"\nNumero: ", self.phone_number)    

    def canRetire(self):
        return (self.__yearOfService() >= 30)

    def __yearOfService(self):
        return 2025 - self.__start_time

class Student(Person):   
    def __init__(self, parent_name="",parent_contact="",status=""):
        self.parent_name = parent_name
        self.parent_contact = parent_contact 
        self.__status = status 
    def getBasicDetails(self):
        print("Nombre: ",self.name,"\nDireccion: ",self.address,"\nCorreo:"
              ,self.email,"\nNumero: ", self.phone_number)    

    def getTutorDetails():
        pass    

class Course:   
    def __init__(self, course_id,name,requisite,min_credit):
        self.course_id = course_id
        self.name = name
        self.requisite = requisite 
        self.__min_credit = min_credit 

    def hasMinCredit(self,grade):
        return grade > self.__min_credit

class Grades:   
    def __init__(self, grade_id,grade,student,course):
        self.course_id = grade_id
        self.grade = grade
        self.student = student
        self.course = course

    def passedCourse(self):
        if(self.course.hasMinCredit(self.grade)):
            print(self.student.name, " paso ",self.course.name) 
        else:
            print(self.student.name, " reprobo ",self.course.name)   



'''
from school import Teacher
#1999 - 1990
teacher = Teacher(1000,"Matematicas", 1990)  
teacher.address ="Avenida alegria"
teacher.email="jose@hotmail.com"
teacher.phone_number= "123456" 
print("teacher "+str(teacher.canRetire())) ''' 

'''
from school import Student, Grades, Course
student = Student()
student.name = "Karla"

course = Course(1,"Matematicas","Tener libro de matematicas 2",6)
grade = Grades(1,5,student,course)
grade.passedCourse()'''