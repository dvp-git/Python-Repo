""" Map , zip , filter"""

"""
1. map(function, iterable,..) 
   map() is very useful when you have to apply the same function to one or more collections of objects.

2. zip(*iterables)

3. filter(function, iterable)
"""

"""Example of map"""
print(list(map(lambda *a: a, range(0,20),"abcde",{'a':1,'b':32}.values())))
# [(0, 'a', 1), (1, 'b', 32)]



""" Sort the marks by sum of scores"""
# from operator import itemgetter, attrgetter
# from pprint import pprint as pp
# students = [
#     dict(id=0, credits=dict(math=9, physics=6, history=7)),
#     dict(id=1, credits=dict(math=6, physics=7, latin=10)),
#     dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
#     dict(id=3, credits=dict(math=5, physics=5, geography=7)),
# ]

# # add a sum attribute for each student
# for student in students:
#     student['scores_sum'] = sum(student['credits'].values())

# # Sort by the sum attribute
# sorted_student = sorted(students,key=lambda student: student['scores_sum'], reverse=True)
# pp(sorted_student) 
# for student in sorted_student:
#     del student['scores_sum']

# pp(sorted_student)

"""Using map() to sort the students by sum of scores"""
# students = [
#     dict(id=0, credits=dict(math=9, physics=6, history=7)),
#     dict(id=1, credits=dict(math=6, physics=7, latin=10)),
#     dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
#     dict(id=3, credits=dict(math=5, physics=5, geography=7)),
# ]
# def decorate(student):
#     # create a 2-tuple (sum of credits, student) from student dict
#     return (sum(student['credits'].values()), student)

# def undecorate(student):
#     # Return only first value
#     return student[1]

# students = sorted(map(decorate, students), reverse=True)

# students = list(map(undecorate, students))
# pp(students)

""" Equivaltent zip and map"""
# grades = [18, 23, 30, 27]
# avgs = [22, 21, 29, 24]

# list(zip(avgs, grades))

# list(map(lambda *a: a, avgs, grades))  # equivalent to zip

