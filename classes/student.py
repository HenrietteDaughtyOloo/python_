import datetime
#Update the Student Class to include these attributes - first_name, last_name, 
# age, country Add these methods to the Student class    - show_full_name  - year_of_birth
 #            - show_initials
 
class Student:    
    school = "AkiraChix"
    def __init__(self,first_name,last_name,age,country, ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country 
    def greet_student(self):
        return f"Hello {self.name} , from {self.country} welcome to {self.school}. "
    
    def show_full_name(self):
        return f"Hello {self.first_name} {self.last_name} welcome to class"    
    def year_of_birth(self):
        current_year = datetime.datetime.now().year
        birth_year = current_year-self.age
        # return birth_year
        return f"{self.first_name} you were born in {birth_year}"
    def initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}"
    
