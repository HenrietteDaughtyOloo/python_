class Car:
    manufaturing_country = "Germany"
    def __init__(self,make,model,speed,year):
        self.make = make
        self.model = model
        self.speed = speed
        self.year = year
    def dispay_details(self):
        return f"This is a {self.year} {self.make} {self.model} from {self.manufaturing_country}"
    def acceleration(self,accelerate):
        self.speed +=accelerate
        return self.speed
    def start(self):
        return f"Vrooooom"
    