# # # revrse a string

# # text="python"
# # print(text[::-1])

# # # student marks Analzer

# # students=[]
# # attempt=0

# # def Analyzer():
# #     student_Name=input("Enter student name: ")
# #     student_Marks= int(input("Enter Student marks: "))

    
# #     print("student_Marks")

# #     if student_Marks>=90:
# #         grade= "A" 
# #     elif student_Marks>=75:
# #         grade ="B"
# #     elif student_Marks>=60:
# #         grade ="C"    
# #     elif student_Marks>= 40:
# #         grade ="D" 
# #     else:
# #         grade="Fail"


# #     students.append({
# #         "name": student_Name,
# #         "marks": student_Marks,
# #         "grade": grade
# #     })    

# #     total = 0

# #     for student in students:
# #         total= total+ student["marks"]

    
# #     average= total/len(students)
           
    
# #     print("total: ",total)
# #     print("average: ",average)

    

    

# # while True:
# #         Analyzer()
# #         attempt+=1
# #         if attempt==3:
# #              highest_student= max(students, key= lambda student: student["marks"])
# #              print(highest_student)     
# #              break  
        

# # list

# # numbers=[10,25,7,40,15,30]

# # print(max(numbers))

# #  string

# # text="programming"
# # count=0

# # for i in text:
# #     if "g" in i:
# #         count+=1

# # print(count)

# # #  remove duplicates
# # numbers=[10,20,10,30,20,40,10]
# # numbers=list(dict.fromkeys(numbers))
# # print(numbers)

# # vowels found
# text= "hello world"
# vowels= "aeiou"
# count=0

# for i in text:
#     if i in vowels:
#         count+=1

# print(count)        


# even numbers

# numbers=[12,5,8,21,4,16,7]

# result=[]

# for i in numbers:
#     if i%2==0:
#         result.append(i)

# print(result)

# # list sum
# numbers=[10,20,30,40,50]

# # print(sum(numbers))

# total =0
# for i in numbers:
#     total=total +i

# print(total)

# upper letter count
# text= "Hello world"

# count=0

# for i in text:
#     if i.isupper():
#         count+=1

# print(count)


# odd number
# numbers=[10,15,22,31,40,55]

# result=[]

# for i in numbers:
#     if i%2==0:
#         pass
#     else:
#         result.append(i)

# print(result)

# count string length without using len()
# text ="python"

# count=0

# for i in text:
#     count+=1

# print(count)


# count specifit list data

# numbers=[10,125,10,30,10,40]
# count=0

# for i in numbers:
#     if i==10:
#         count+=1

# print(count)

# print first character of string

# text="hello"

# for i in text:
#     print(text[0])
#     break

# negitive indexing 

# numbers=[10,20,30,40,50]

# print(numbers[-1])


# text="python"

# if "p" in text:
#     print(True)
# else:
#     print(False)  
# 

# # count number > 10
# # 
# numbers=[12,7,18,5,20,9]  
# count=0
# for i in numbers:
#     if i > 10:
#         count+=1
# print(count)     
# 
# sum 
numbers= [10,20,30,40,50]   

print(sum(numbers))

