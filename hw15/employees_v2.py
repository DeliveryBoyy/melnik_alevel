from datetime import date, timedelta

class Employee:
    def __init__(self, first_name, last_name, email, phone_number, salary_rate_daily):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.salary_rate_daily = salary_rate_daily

    def work(self):
        return "I come to the office."

    def check_salary(self, days_worked):
        return self.salary_rate_daily * days_worked

    def __str__(self):
        return "{0}: {1} {2}".format(self.__class__.__name__, self.first_name, self.last_name)

    def __eq__(self, other):
        return self.salary_rate_daily == other.salary_rate_daily

    def __ne__(self, other):
        return self.salary_rate_daily != other.salary_rate_daily

    def __gt__(self, other):
        return self.salary_rate_daily > other.salary_rate_daily

    def __lt__(self, other):
        return self.salary_rate_daily < other.salary_rate_daily

    def __ge__(self, other):
        return self.salary_rate_daily >= other.salary_rate_daily

    def __le__(self, other):
        return self.salary_rate_daily <= other.salary_rate_daily


class Programmer(Employee):
    def __init__(self, first_name, last_name, email, phone_number, salary_rate_daily, tech_stack, closed_this_month):
        super().__init__(first_name, last_name, email, phone_number, salary_rate_daily)
        self.tech_stack = tech_stack
        self.closed_this_month = closed_this_month

    def work(self):
        return "{0} {1}".format(super().work()[:-1], "and start programming.")

    def __add__(self, other):
        # create an "alpha" programmer object by combining salaries, tech stacks and number of issues closed this month
        alpha_programmer = Programmer(
            'Alpha', 'Programmer', 'alpha@beta.com', '+380696661337',
            self.salary_rate_daily + other.salary_rate_daily,
            set(self.tech_stack + other.tech_stack),
            self.closed_this_month + other.closed_this_month)
        return alpha_programmer

    # calculate the total salary for this month so far, including today
    # don't include saturdays/sundays
    def current_salary(self):
        iter_date = date(date.today().year, date.today().month, 1)
        current_salary = self.salary_rate_daily
        while iter_date != date.today():
            if iter_date.weekday() < 5:
                current_salary += self.salary_rate_daily
            iter_date = date(iter_date.year, iter_date.month, iter_date.day + 1)
        return current_salary

    # methods for comparing two programmers by the number of the technologies they can work with
    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)


class Recruiter(Employee):
    def __init__(self, first_name, last_name, email, phone_number, salary_rate_daily, hired_this_month):
        super().__init__(first_name, last_name, email, phone_number, salary_rate_daily)
        self.hired_this_month = hired_this_month

    def work(self):
        return "{0} {1}".format(super().work()[:-1], "and start hiring.")


def run():
    # create two Programmer objects and a single Recruiter object, populate their property values
    programmer = Programmer('Dmitriy', 'Miller', 'melniknc@gmail.com', '+380956666969', 200,
                            ['Python', 'Django', 'PSQL', 'Linux', 'Bash'], 17)
    programmer2 = Programmer('Guy', 'Fieri', 'guy@fieri.com', '+3806798766990', 130, ['JS', 'HTML', 'CSS', 'PSQL'], 13)
    recruiter = Recruiter('Anna', 'Bee', 'anemailaddress@email.com', '+380956667777', 100, 3)

    # various test for the existing methods:
    # print out a string indicating that the employee is working
    print(programmer.work())
    # print out the string representation of this Employee object
    print(programmer.__str__())
    # print out the number of people the recruiter hired this month
    print(recruiter.hired_this_month)
    # print out the tech stack and the number of closed issues for the first programmer
    print("Tech Stack: {}.\nClosed this month: {}.".format(", ".join(programmer.tech_stack),
                                                           programmer.closed_this_month))
    # create an "alpha" Programmer object and print out its properties along with values
    print(vars(programmer + programmer2))
    # compare two programmers by the numbers of the technologies they can work with
    # this one returns True
    print(programmer >= programmer2)
    print(programmer.current_salary())


run()
