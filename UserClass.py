import pickle

from IngredientClass import Ingredient
import os
from HelperFunctions import set_current_user

from RecipeClass import Recipe


class User(object):

    def __init__(self, name='', pantry=None, cookbook=None, agenda=None, semesters=None):
        self.name = name

        if pantry is None:
            self.pantry = []
        if cookbook is None:
            self.cookbook = []
        if agenda is None:
            self.agenda = []
        if semesters is None:
            self.semesters = []

    def to_string(self):
        print('User name: ' + self.name)
        print('---------------------Your Pantry-------------------------')
        for i in self.pantry:
            print(i.name)
        print('----------------------Your Cookbook------------------------')
        for r in self.cookbook:
            print(r.name)
        print('----------------------Your Agenda------------------------')
        for a in self.agenda:
            print(a.name)
        print('----------------------Your Semesters------------------------')
        for s in self.semesters:
            print(s.name)
        print('----------------------------------------------')

    # def add_new_ingredient_to_pantry(self):
    #     i = Ingredient(
    #         name=input('What is the ingredient? '), serving_size=float(input('Serving size? ')),
    #         cal=float(input('How many calories? ')), tot_fat=float(input('What is the total fat? ')),
    #         sat_fat=float(input('What is the saturated fat? ')), trans_fat=float(input('What is the trans fat? ')),
    #         sodium=float(input('How much sodium? ')), carbs=float(input('How many carbs? ')),
    #         fiber=float(input('How much fiber? ')),
    #         sugar=float(input('How much sugar? ')), protein=float(input('How much protein? '))
    #     )
    #
    #     self.pantry.append(i)
    #     self.save_user_data()
    #     return i

    # def add_new_recipe_to_pantry(self):
    #     r = Recipe(
    #         name=input('What is the recipe(no spaces)? ')
    #     )
    #     ingredients_string = input('Enter the ingredients of the recipe followed by spaces: ')
    #     s = ingredients_string.split()
    #     print('For each ingredient listed, enter the amount of servings for recipe. ')
    #     for i in s:
    #         x = float(input('How many ' + i + "'s: "))
    #         r.rr.update({i: x})
    #         ingredient = load_ingredient_from_meta(i) ####### change to load ingredient from pantry
    #         r.cal += x * ingredient.cal
    #         r.tot_fat += x * ingredient.tot_fat
    #         r.sat_fat += x * ingredient.sat_fat
    #         r.trans_fat += x * ingredient.trans_fat
    #         r.sodium += x * ingredient.sodium
    #         r.carbs += x * ingredient.carbs
    #         r.fiber += x * ingredient.fiber
    #         r.sugar += x * ingredient.sugar
    #         r.protein += x * ingredient.protein

    # self.cookbook.append(r)

    def add_ingredient_to_pantry(self, i):
        self.pantry.append(i)
        self.save_user_data()
        return i

    def add_recipe_to_cookbook(self, r):
        self.cookbook.append(r)
        self.save_user_data()
        return r

    def add_assignment_to_agenda(self, a):
        self.agenda.append(a)
        self.save_user_data()
        return a

    def add_semester_to_semesters(self, s):
        self.semesters.append(s)
        self.save_user_data()
        return s

    def save_user_data(self):
        root = os.getcwd()
        filename = root + '/UserMeta/' + self.name
        pickle_out = open(filename, 'wb')
        pickle.dump(self, pickle_out)
        pickle_out.close()
        set_current_user(self)
