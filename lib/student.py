#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
        print(first_name, last_name)
    
    def learn(self, more_knowledge):
        for info in more_knowledge:
            self.knowledge.append(more_knowledge)
        print(self.knowledge)


sam = Student("Sam", "G")
sam.learn("SO much knowledge")




        