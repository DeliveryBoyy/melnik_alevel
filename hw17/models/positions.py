from datetime import date

from .employee import Employee


class Programmer(Employee):
    """
    This class represents any particular Employee that is a programmer.
    Has attributes and methods specific only to Programmers.
    """
    def __init__(self, first_name, last_name, email, phone_number, salary_rate_daily, tech_stack, closed_this_month):
        super().__init__(first_name, last_name, email, phone_number, salary_rate_daily)
        self.tech_stack = tech_stack
        self.closed_this_month = closed_this_month

    """
    Finalize the representation of the working process based on the Employees position.
    """
    def work(self):
        return "{0} {1}".format(super().work()[:-1], "and start programming.")

    """
    Create an "alpha" programmer object by combining salaries, tech stacks and number of issues closed this month.
    """
    def __add__(self, other):
        alpha_programmer = Programmer(
            'Alpha', 'Programmer', 'alpha@beta.com', '+380696661337',
            self.salary_rate_daily + other.salary_rate_daily,
            set(self.tech_stack + other.tech_stack),
            self.closed_this_month + other.closed_this_month)
        return alpha_programmer

    """
    Calculate the total salary for this month so far, including today. Don't include saturdays/sundays.
    """
    def current_salary(self):
        iter_date = date(date.today().year, date.today().month, 1)
        current_salary = 0
        while iter_date <= date.today():
            if iter_date.weekday() < 5:
                current_salary += self.salary_rate_daily
            iter_date = date(iter_date.year, iter_date.month, iter_date.day + 1)
        return current_salary

    """
    Methods for comparing two programmers by the number of the technologies they can work with.
    """
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
    """
    This class represents any particular Employee that is a Recruiter.
    Has attributes and methods specific only to Recruiters.
    """
    def __init__(self, first_name, last_name, email, phone_number, salary_rate_daily, hired_this_month):
        super().__init__(first_name, last_name, email, phone_number, salary_rate_daily)
        self.hired_this_month = hired_this_month

    def work(self):
        """
        Finalizes the representation of the working process based on the Employees position.
        """
        return "{0} {1}".format(super().work()[:-1], "and start programming.")
