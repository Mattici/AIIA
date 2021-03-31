import HelperFunctions


class Recipe(object):
    def __init__(self, name='', serving_size=0.0, cal=0.0, tot_fat=0.0, sat_fat=0.0,
                 trans_fat=0.0, sodium=0.0, carbs=0.0, fiber=0.0, sugar=0.0, protein=0.0, rr=None):
        if rr is None:
            self.rr = {}
        self.name = name
        self.serving_size = serving_size
        self.cal = cal
        self.tot_fat = tot_fat
        self.sat_fat = sat_fat
        self.trans_fat = trans_fat
        self.sodium = sodium
        self.carbs = carbs
        self.fiber = fiber
        self.sugar = sugar
        self.protein = protein

    def to_string(self):
        print('\n')
        print('----------------------------------------------')
        print('Recipe name: ' + self.name)
        print(self.rr)
        print('Calories: ' + str(self.cal))
        print('Total fat: ' + str(self.tot_fat))
        print('Saturated fat: ' + str(self.sat_fat))
        print('Trans fat: ' + str(self.trans_fat))
        print('Sodium: ' + str(self.sodium))
        print('Carbs: ' + str(self.carbs))
        print('Fiber: ' + str(self.fiber))
        print('Sugar: ' + str(self.sugar))
        print('Protein: ' + str(self.protein))
        print('----------------------------------------------')

    def remove_ingredient_from_recipe(self, ingredient):
        self.rr.pop(ingredient)
        self.to_string()
        return self

    def add_new_ingredient_to_recipe(self, ingredient):
        x = input('How many ' + ingredient + "'s do you want to add?\n")
        self.rr.update({ingredient: float(x)})
        self.to_string()
        return self

    def alter_ingredient_of_recipe(self, ingredient):
        x = float(input('What is the new amount of ' + ingredient + "'s ?\n"))
        old_val = float(self.rr.get(ingredient))
        new_val = x
        self.rr.update({ingredient: new_val})
        self.update_macros()
        self.to_string()
        return self

    def update_macros(self):
        self.cal = 0.0
        self.tot_fat = 0.0
        self.sat_fat = 0.0
        self.trans_fat = 0.0
        self.sodium = 0.0
        self.carbs = 0.0
        self.fiber = 0.0
        self.sugar = 0.0
        self.protein = 0.0
        for i in self.rr.keys():
            ingredient = HelperFunctions.load_ingredient_from_pantry(i)
            x = float(self.rr.get(i))
            self.cal += x * ingredient.cal
            self.tot_fat += x * ingredient.tot_fat
            self.sat_fat += x * ingredient.sat_fat
            self.trans_fat += x * ingredient.trans_fat
            self.sodium += x * ingredient.sodium
            self.carbs += x * ingredient.carbs
            self.fiber += x * ingredient.fiber
            self.sugar += x * ingredient.sugar
            self.protein += x * ingredient.protein
