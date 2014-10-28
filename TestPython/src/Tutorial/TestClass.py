##
# Created on 14, October, 2014
# Test class
# @author: chenzhi

import logging
from types import MethodType

class Person(object):
    __slots__ = ('__name', '__sex', '__age', 'height')
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age
        
    def printInfo(self):
        print 'name =', self.__name, 'sex =', self.__sex, 'age =', self.__age
        

if __name__ == '__main__':
    person = Person('daniel', 'male', 20)
    person.printInfo()
    try:
        print person.__age
    except Exception as e:
        logging.exception(e)
        
    # test bind attribute  
    person.height = 170
    print 'height =', person.height
    try:
        person.weight = 60
        print 'weight =', person.weight
    except Exception as e:
        logging.exception(e) 
    
    # test bind method
    def printHeight(self):
        print self.height
        
    Person.printHeight = MethodType(printHeight, None, Person)
    person.printHeight()