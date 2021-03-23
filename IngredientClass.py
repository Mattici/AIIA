
class Ingredient(object):
    def __init__(self, name='', serving_size=0.0, cal=0.0, tot_fat=0.0, sat_fat=0.0,
                 trans_fat=0.0, sodium=0.0, carbs=0.0, fiber=0.0, sugar=0.0, protein=0.0):
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
        print('Ingredient: ' + self.name)
        print('Serving size: ' + str(self.serving_size))
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