# code 
class Student: 
	def __init__(self, studentName, studentSurname, studentRollNo): 
		self.name = studentName 
		self.surname = studentSurname 
		self.rollNo = studentRollNo 

	def __getStudentDetails__(self,a): 
		print("The name of the student is", self.name, self.surname) 
		print("The roll no of the student is", self.rollNo) 
		print("The roll no of the student is", a.rollNo)
  
      

       
    

student1 = Student("Vivek", "Yadav", 20) 
student2 = Student("vel", "raaj" , 21)
student1.__getStudentDetails__(student2) 
