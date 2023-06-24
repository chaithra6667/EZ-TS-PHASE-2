'''append elements(key,value),
key:priority
value: element in queue
and sort the list every time in element
is append'''
stu_grade=[]

stu_grade.append((1,'Klaus'))
stu_grade.append((4,'Noah'))
stu_grade.sort(reverse=True)
print('Yes')
print(stu_grade)
stu_grade.append((3,'damon'))
stu_grade.sort(reverse=True)
stu_grade.append((2,'Nick'))
stu_grade.sort(reverse=True)
print('Prioritie wise sorted')
print(stu_grade)
print('Original queue')
while stu_grade:
    print(stu_grade.pop())



