# revrse a string

text="python"
print(text[::-1])

# student marks Analzer

students=[]

global student_Name
global student_Marks

def Analyzer():
        student_Name=input("Enter student name: ")
        student_Marks= int(input("Enter Student marks: "))

        students.append(student_Name,student_Marks)
        return student_Marks

while True:
        Analyzer()




