class SoftwareEngineer:
    alias = 'Scorpion King'

    def __init__(self, name, age, title):
        self.name = name
        self.age = age
        self.title = title

    def __str__(self):
        information = f'Name: {self.name}, Title: {self.title}'
        return information

    def __eq__(self, other):
        return self.name == other.name

    def get_name(self, book):
        return self.name + book

    @staticmethod
    def salary_info(salary):
        return salary


se1 = SoftwareEngineer(name='Prity', age=31, title='Junior Engineer')
se2 = SoftwareEngineer(name='Prity', age=31, title='Junior Engineer')
print(se1 == se2)
print(SoftwareEngineer.salary_info(10))
