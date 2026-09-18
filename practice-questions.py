# revrse a string

text="python"
print(text[::-1])

# student marks Analzer

students=[]


def Analyzer():
    student_Name=input("Enter student name: ")
    student_Marks= int(input("Enter Student marks: "))

    
    print("student_Marks")

    if student_Marks>=90:
        return "A" 
    elif student_Marks>=75:
        grade ="B"
    elif student_Marks>=60:
        grade ="C"    
    elif student_Marks>= 40:
        grade ="D" 
    else:
        grade="Fail"

    students.append({
        "name": student_Name,
        "marks": student_Marks,
        "grade": grade
    })    
           
    return student_Marks


while True:
        Analyzer()
        



        

