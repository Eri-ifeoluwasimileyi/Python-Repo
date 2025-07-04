class Person:

    def __init__(self, name: str, age: int, gender: str):
        self.name = name

        self.age = age

        self.gender = gender

        self.problems = []


    def add_problem(self, problem):

            self.problems.append(problem)


p1 = Person('John', 24, "Male")
p1.