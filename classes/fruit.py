class Fruits:
    nutrients = "Vitamins"

    def __init__(self, name,colour,number_of_seeds,fruit_texture):
        self.colour = colour
        self.name = name
        self.number_of_seeds = number_of_seeds
        self.fruit_texture = fruit_texture
    
    
    def make_juice(self):        
        return f"When blended makes {self.name} juice that is {self.colour} in color"
    def remove_seeds(self):
        return f"Cut the fruit to remove {self.number_of_seeds} seeds"
    
        
    
