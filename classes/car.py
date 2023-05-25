class Car:
    manufaturing_country = "Germany"
    def __init__(self,make,model,current_speed,year,hooting):
        self.hooting = hooting
        self.make = make
        self.model = model
        self.speed = current_speed
        self.year = year
    def dispay_details(self):
        return f"This is a {self.year} {self.make} {self.model} from {self.manufaturing_country}"
    def acceleration(self,accelerate):
        self.speed +=accelerate
        return self.speed
    def start(self):
        return f"Vrooooom"
    def hoot(self):
        return f"The car is hooting {self.hooting}"
    