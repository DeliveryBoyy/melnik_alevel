from models.positions import Programmer, Recruiter
from models.candidate import Candidate
from models.vacancy import Vacancy


# Main logic.
def main():
    # create a recruiter object and populate its properties with values
    recruiter = Recruiter('Anna', 'Bee', 'anemailaddress@email.com', '+380956667777', 100, 3)
    # create and populate 2 Programmer objects
    programmer = Programmer('Dmitriy', 'Miller', 'melniknc@gmail.com', '+380956666969', 200,
                            ['Python', 'Django', 'PSQL', 'Linux', 'Bash'], 17)
    programmer2 = Programmer('Guy', 'Fieri', 'guy@fieri.com', '+3806798766990', 130, ['JS', 'HTML', 'CSS', 'PSQL'], 13)
    # create and populate 3 Candidate objects
    candidate = Candidate('John Doe', 'johnd@email.com', ['Python', 'PSQL'], 'Python', 'Junior')
    candidate2 = Candidate('Jane Doe', 'janed@email.com', ['JS', 'HTML', 'CSS'], 'JS', 'Middle')
    candidate3 = Candidate('John Don\'t', 'janed@email.com', ['Java', 'SQL'], 'Java', 'Senior')
    # create and populate 2 Vacancy options
    vacancy = Vacancy('Junior Python Developer', 'Python', 'Junior')
    vacancy2 = Vacancy('Senior Java Developer', 'Java', 'Senior')

    """
    Tests for hw17:
    """
    # candidate3.work()

    """
    Tests for hw16 version and earlier versions:

    # Various tests for existing methods:
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
    # calculate total wages for an Employee for the current month
    print(programmer.current_salary())
    """
