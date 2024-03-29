import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.INFO, filename='application.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age
        logging.info(f'Created person: {self.full_name()}')

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1
        logging.info(f'{self.full_name()} had a birthday, new age: {self._age}')

    def get_age(self):
        return self._age

class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary
        logging.info(f'Created employee: {self.full_name()} ({self.position})')

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)
        logging.info(f'{self.full_name()} ({self.position}) salary raised by {percent}% to {self.salary}')

    def __str__(self):
        return f'{self.full_name()} ({self.position})'

# Command-line argument parsing
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--last_name', type=str, help='Last name of the person')
parser.add_argument('--first_name', type=str, help='First name of the person')
parser.add_argument('--patronymic', type=str, help='Patronymic of the person')
parser.add_argument('--age', type=int, help='Age of the person')
parser.add_argument('--position', type=str, help='Position of the employee')
parser.add_argument('--salary', type=float, help='Salary of the employee')

args = parser.parse_args()

# Example usage
if args.last_name and args.first_name and args.patronymic and args.age:
    person = Person(args.last_name, args.first_name, args.patronymic, args.age)
    if args.position and args.salary:
        employee = Employee(args.last_name, args.first_name, args.patronymic, args.age, args.position, args.salary)
        employee.raise_salary(10)

