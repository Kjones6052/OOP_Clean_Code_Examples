
# Basic class structure
class PastaCooker:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def cook_pasta(self):
        # Cooking pasta
        pass

    def prepare_sauce(self):
        # Preparing sauce
        pass

    def serve_dish(self):
        # Serving the dish
        pass

# Refactored class structure
class PastaChef:
    def __init__(self, pasta_type):
        self.pasta_type = pasta_type

    def cook_pasta(self):
        # Focuses solely on cooking pasta perfectly
        pass

class SauceChef:
    def __init__(self, sauce_recipe):
        self.sauce_recipte = sauce_recipe

    def prepare_sauce(self):
        # Specializing in making the sauce
        pass

class Server:
    def serve_dish(self, pasta, sauce):
        # Expert in plating and serving the dish
        pass