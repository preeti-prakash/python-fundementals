def student_summary(student):
        Name, Age, Grade = student
        return f"Student Name: {Name}, Age: {Age}, Grade: {Grade}"
        
print(student_summary(('Alice', 20, 89.5)))  
#Output: "Student Name: Alice, Age: 20, Grade: 89.5"
 
print(student_summary(('Bob', 22, 75.8)))  
#Output: "Student Name: Bob, Age: 22, Grade: 75.8"
 
print(student_summary(('Charlie', 19, 92.0)))  
#Output: "Student Name: Charlie, Age: 19, Grade: 92