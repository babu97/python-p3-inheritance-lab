#!/usr/bin/env python

from user import User

import random


class Teacher(User):
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

    def teach(self):
        if not self.knowledge:
            print(f"{self.first_name} {self.last_name} has no knowledge to share.")
            return None
        else:
            random_topic = random.choice(self.knowledge)
            return random_topic
