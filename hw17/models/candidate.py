from exceptions import UnableToWorkException

class Candidate:
    """
    This class represents a person applying for a position in the company.
    """
    def __init__(self, full_name, email, tech_stack, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def work(self):
        raise UnableToWorkException('I\'m not hired yet, lol')
