# # revrse a string

# text="python"
# print(text[::-1])

# # student marks Analzer

# students=[]
# attempt=0

# def Analyzer():
#     student_Name=input("Enter student name: ")
#     student_Marks= int(input("Enter Student marks: "))

    
#     print("student_Marks")

#     if student_Marks>=90:
#         grade= "A" 
#     elif student_Marks>=75:
#         grade ="B"
#     elif student_Marks>=60:
#         grade ="C"    
#     elif student_Marks>= 40:
#         grade ="D" 
#     else:
#         grade="Fail"


#     students.append({
#         "name": student_Name,
#         "marks": student_Marks,
#         "grade": grade
#     })    

#     total = 0

#     for student in students:
#         total= total+ student["marks"]

    
#     average= total/len(students)
           
    
#     print("total: ",total)
#     print("average: ",average)

    

    

# while True:
#         Analyzer()
#         attempt+=1
#         if attempt==3:
#              highest_student= max(students, key= lambda student: student["marks"])
#              print(highest_student)     
#              break  
        

# list

numbers=[10,25,7,40,15,30]

print(max(numbers))