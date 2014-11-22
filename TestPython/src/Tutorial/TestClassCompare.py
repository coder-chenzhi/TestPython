'''
created on 22. Nov, 2014
@author: ZhiChen
'''

class Student(object):
    def __init__(self, id, name, sex = 'M', age = 20):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return 'Student' + ' ID: ' + str(self.id) + ' Name: ' + str(self.name) + \
            ' Sex: ' + str(self.sex) +  ' Age: ' + str(self.age)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.id > other.id


a = Student(100, 'Daniel')
print a
b = Student(101, 'zhichen')
c = Student(102, 'coder')
lst = [b, a, c]
print 'before sort:'
print lst
lst.sort()
print 'after sort:'
print lst