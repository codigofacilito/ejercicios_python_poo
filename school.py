from abc import ABC, abstractmethod
class Person(ABC):
  def __init__(self):
    self.person_id = 0
    self.name = ""
    self.address = ""
    self.email = ""
    self.phone_number = ""
  
  @abstractmethod  
  def getBasicDetails(self):
    pass  

class Teacher(Person):
  def __init__(self, salary,specialty,start_time):
    self.salary = salary
    self.specialty = specialty
    self.__start_time = start_time

  def getBasicDetails(self):
    print("El profesor: ",self.name, "Tiene un salario de: ",self.salary)

  def canRetire(self):
    return self.__year_of_service() >= 30

  def __year_of_service(self):
    return 2025 - self.__start_time

class Student(Person):
  def __init__(self,parent_name="", parent_contact="",status=""):
    self.parent_name = parent_name
    self.parent_contact = parent_contact
    self.__status = status
    
  def getBasicDetails(self):
    print("El alumno: ",self.name, " su tutor es: ",self.parent_name)  
  
  def get_tutor_details(self):
      print("Nombre del tutor: ",self.parent_name, "Conatcto: ",self.parent_contact) 


class Course:
  def __init__(self,course_id,name,requisite,min_credit):
    self.course_id = course_id
    self.name = name
    self.requisite = requisite
    self.__min_credit = min_credit

  def hasMinCredit(self,grade):
    return grade > self.__min_credit

class Grades:
  def __init__(self,grade_id,grade,student,course):
    self.grade_id = grade_id
    self.grade = grade
    self.student = student
    self.course = course 

  def passedCourse(self):
    if self.course.hasMinCredit(self.grade):
      print(self.student.name, " paso ", self.course.name)
    else:
      print(self.student.name, " reprobo ",self.course.name)       


#Ejecutar en main
'''
from school import Teacher,Student,Grades, Course

teacher = Teacher(10000,"Idiomas", 2000)
print(teacher.canRetire())


teacher.email = "marines@codigofacilito.com"
teacher.name = "Jose"
print(teacher.getBasicDetails())

student = Student("Karla","1234567","Activo")
student.name = "Luis"
print(student.getBasicDetails())


student = Student()
student.name = "Pedro"
course = Course(1,"Ingles","Tener el libro de inles 2", 6)
grade = Grades(1,8,student,course)
grade.passedCourse()

'''               