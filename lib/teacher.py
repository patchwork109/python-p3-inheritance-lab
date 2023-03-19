#!/usr/bin/env python

from user import User

import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]


class Teacher(User):

    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge


    def teach(self):
        random_int = random.randint(0,7)
        self.knowledge = self.knowledge[random_int]
        print(self.knowledge)


    def print_teacher_details(self):
        print(f'''
            first_name: {self.first_name}
            last_name: {self.last_name}
            knowledge: {self.knowledge}
        ''')

my_teacher = Teacher("John", "Smith", knowledge)
my_teacher.teach()
my_teacher.print_teacher_details()
