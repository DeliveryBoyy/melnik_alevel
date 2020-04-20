class Employee:
    """
    This class represents any and all employees in the company and has attributes and methods applicable to all of them.
    """

    """
    Create an object of the Employee class and populate it with values.
    
    Additionally, write the email attribute to the file emails.txt, via the save_email method.
    """

    def __init__(self, first_name, last_name, email, phone_number, salary_rate_daily):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.validate_email()
        self.save_email()
        self.phone_number = phone_number
        self.salary_rate_daily = salary_rate_daily

    """
     Represent the working process of an Employee. The result is finalized by the work() method of child classes.
    """

    def work(self):
        return "I come to the office."

    """
    Check the size of the salary payment for a set number of days.
    """

    def check_salary(self, days_worked):
        return self.salary_rate_daily * days_worked

    """
    String representation of the employee object in the format like "Position: FirstName LastName"
    """

    def __str__(self):
        return "{0}: {1} {2}".format(self.__class__.__name__, self.first_name, self.last_name)

    """
    Write the email address of the Employee to the emails.txt file
    """

    def save_email(self):
        with open('emails.txt', 'a') as f:
            f.write(self.email)
            f.write("\n")

    """
    Check whether the email attribute of the object is present in the emails.txt file.
    """

    def validate_email(self):
        try:
            with open('emails.txt', 'r') as f:
                if self.email in f.read():
                    raise ValueError
        # If emails.txt doesn't exist it means that no emails have been written to it, so any email address is free.
        # So, pass the validation.
        except FileNotFoundError:
            pass
        print("Email is validated!")

    """
    Comparisons of Employees by their daily salary rate.
    """

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
