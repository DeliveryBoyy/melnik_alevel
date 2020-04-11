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
    def __init__(self, first_name, last_name, email, phone_number, salary_rate_daily, stack, closed_this_month):
        super().__init__(first_name, last_name, email, phone_number, salary_rate_daily)
        self.stack = stack
        self.closed_this_month = closed_this_month

    def work(self):
        return "{0} {1}".format(super().work()[:-1], "and start programming.")


class Recruiter(Employee):
    def __init__(self, first_name, last_name, email, phone_number, salary_rate_daily, hired_this_month):
        super().__init__(first_name, last_name, email, phone_number, salary_rate_daily)
        self.hired_this_month = hired_this_month

    def work(self):
        return "{0} {1}".format(super().work()[:-1], "and start hiring.")


def run():
    programmer = Programmer('Dmitriy', 'Miller', 'melniknc@gmail.com', '+380956666969', 200, ['Python', 'Django', 'Linux'], 17)
    recruiter = Recruiter('Anna', 'Bee', 'anemailaddress@email.com', '+380956667777', 100, 3)
    print(programmer.work())
    print(programmer.__str__())
    result = programmer <= recruiter
    print(result)
    print(recruiter.hired_this_month)
    print("Stack: {}\nClosed this month: {}".format(programmer.stack, programmer.closed_this_month))

run()
