def student(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print()



student(name="vikas", age=20, marks=78)
student(name="neha", age=21, marks=81)

# student = {'name':'vivek', 'age':20, 'marks':90}
# print(student['name'])
#
# # print(student.keys())
# # print(student.values())
# print(student.items())
#
# for key,value in student.items():
#     print(key, value)
