import inflect
import pickle
import os
from IngredientClass import Ingredient
from RecipeClass import Recipe
from AssignmentClass import Assignment
from CourseListClass import CourseList


root = os.getcwd()


####################################### Adds #######################################

def add_new_ingredient_to_pantry():
    user = load_current_user()
    i = Ingredient(
        name=input('What is the ingredient? '), serving_size=float(input('Serving size? ')),
        cal=float(input('How many calories? ')), tot_fat=float(input('What is the total fat? ')),
        sat_fat=float(input('What is the saturated fat? ')), trans_fat=float(input('What is the trans fat? ')),
        sodium=float(input('How much sodium? ')), carbs=float(input('How many carbs? ')),
        fiber=float(input('How much fiber? ')),
        sugar=float(input('How much sugar? ')), protein=float(input('How much protein? '))
    )

    user.pantry.append(i)
    user.save_user_data()
    return i

def add_new_recipe_to_cookbook():
    user = load_current_user()
    r = Recipe(
        name=input('What is the recipe(no spaces)? ')
    )
    ingredients_string = input('Enter the ingredients of the recipe followed by spaces: ')
    s = ingredients_string.split()
    print('For each ingredient listed, enter the amount of servings for recipe. ')
    for i in s:
        x = float(input('How many ' + i + "'s: "))
        r.rr.update({i: x})
        ingredient = load_ingredient_from_pantry(i)
        r.cal += x * ingredient.cal
        r.tot_fat += x * ingredient.tot_fat
        r.sat_fat += x * ingredient.sat_fat
        r.trans_fat += x * ingredient.trans_fat
        r.sodium += x * ingredient.sodium
        r.carbs += x * ingredient.carbs
        r.fiber += x * ingredient.fiber
        r.sugar += x * ingredient.sugar
        r.protein += x * ingredient.protein

    user.cookbook.append(r)
    user.save_user_data()
    return r


def add_new_assignment_to_agenda():
    user = load_current_user()
    a = Assignment(
        course=str(input('What course is this for? ')),
        name=str(input('What is the name of this assignment (no spaces)? ')),
        description=str(input('What do you have to do for this assignment? ')),
        due_date=str(input('When is it due (example: Monday April 23)? '))
    )
    user.agenda.append(a)
    user.save_user_data()
    return a

def add_new_courselist_to_semesters():
    user = load_current_user()
    s = CourseList(
        name=str(input('What is the name of the course list? (example, Spring2021)? ')),
    )
    user.semesters.append(s)
    user.save_user_data()
    return s


# def add_ingredient_to_meta():
#     i = Ingredient(
#         name=input('What is the ingredient? '), serving_size=float(input('Serving size? ')),
#         cal=float(input('How many calories? ')), tot_fat=float(input('What is the total fat? ')),
#         sat_fat=float(input('What is the saturated fat? ')), trans_fat=float(input('What is the trans fat? ')),
#         sodium=float(input('How much sodium? ')), carbs=float(input('How many carbs? ')),
#         fiber=float(input('How much fiber? ')),
#         sugar=float(input('How much sugar? ')), protein=float(input('How much protein? '))
#     )
#     filename = root + '/Meta/Ingredients/' + str(i.name)
#     pickle_out = open(filename, 'wb')
#     pickle.dump(i, pickle_out)
#     pickle_out.close()
#     return i


# def add_recipe_to_meta():
#     r = Recipe(
#         name=input('What is the recipe(no spaces)? ')
#     )
#     ingredients_string = input('Enter the ingredients of the recipe followed by spaces: ')
#     s = ingredients_string.split()
#     print('For each ingredient listed, enter the amount of servings for recipe. ')
#     for i in s:
#         x = float(input('How many ' + i + "'s: "))
#         r.rr.update({i: x})
#         ingredient = load_ingredient_from_meta(i)
#         r.cal += x * ingredient.cal
#         r.tot_fat += x * ingredient.tot_fat
#         r.sat_fat += x * ingredient.sat_fat
#         r.trans_fat += x * ingredient.trans_fat
#         r.sodium += x * ingredient.sodium
#         r.carbs += x * ingredient.carbs
#         r.fiber += x * ingredient.fiber
#         r.sugar += x * ingredient.sugar
#         r.protein += x * ingredient.protein
#     filename = root + '/Meta/Recipes/' + r.name
#     pickle_out = open(filename, 'wb')
#     pickle.dump(r, pickle_out)
#     pickle_out.close()
#     return r


# def add_assignment_to_meta():
#     a = Assignment(
#         course=str(input('What course is this for? ')),
#         name=str(input('What is the name of this assignment (no spaces)? ')),
#         description=str(input('What do you have to do for this assignment? ')),
#         due_date=str(input('When is it due (example: Monday April 23)? '))
#     )
#     filename = root + '/Meta/Assignments/' + a.name
#     pickle_out = open(filename, 'wb')
#     pickle.dump(a, pickle_out)
#     pickle_out.close()
#
#     return a

# def add_courselist_to_meta():
#     cs = CourseList(
#         name=str(input('What is the name of the course list? (example, Spring2021)? ')),
#     )
#     filename = root + '/Meta/CourseLists/' + cs.name
#     pickle_out = open(filename, 'wb')
#     pickle.dump(cs, pickle_out)
#     pickle_out.close()
#
#     return cs


####################################### Loads #######################################
def load_ingredient_from_pantry(ingredient):
    user = load_current_user()
    for i in user.pantry:
        if i.name == ingredient:
            return i
    else:
        print('There are no ' + ingredient + 's in your pantry')

def load_recipe_from_cookbook(recipe):
    user = load_current_user()
    for r in user.cookbook:
        if r.name == recipe:
            return r
    else:
        print("You don't have " + recipe + "in your cookbook")

def load_assignment_from_agenda(assignment):
    user = load_current_user()
    for a in user.agenda:
        if a.name == assignment:
            return a
        else:
            print(assignment + ' is not in your agenda')

def load_courselist_from_semesters(courselist):
    user = load_current_user()
    for cs in user.semesters:
        if cs.name == courselist:
            return cs
        else:
            print(courselist + ' is not one of your semesters')



# def load_ingredient_from_meta(ingredient):
#     filename = '/Users/mattcarter/Documents/UVA/Spring2021/pythonProject/Ingredients/' + ingredient
#     pickle_in = open(filename, 'rb')
#     i = pickle.load(pickle_in)
#     return i


# def load_recipe_from_meta(recipe):
#     filename = root + '/Meta/Recipes/' + recipe
#     pickle_in = open(filename, 'rb')
#     r = pickle.load(pickle_in)
#     return r
#
#
# def load_assignment_from_meta(assignment):
#     filename = root + '/Meta/Assignments/' + assignment
#     pickle_in = open(filename, 'rb')
#     a = pickle.load(pickle_in)
#     return a
#
#
# def load_courselist_from_meta(course):
#     filename = root + '/Meta/CourseLists/' + course
#     pickle_in = open(filename, 'rb')
#     cs = pickle.load(pickle_in)
#     return cs


# def load_the_hippocampus_from_meta():
#     filename = '/Users/mattcarter/Documents/UVA/Spring2021/pythonProject/OriginalBrainFiles/TheHippocampus'
#     pickle_in = open(filename, 'rb')
#     h = pickle.load(pickle_in)
#     return h




####################################### Get Lists #######################################
def return_pantry():
    l = []
    for i in load_current_user().pantry:
        l.append(i)
    return l

def return_cookbook():
    l = []
    for r in load_current_user().cookbook:
        l.append(r)
    return l

def return_agenda():
    l = []
    for a in load_current_user().agenda:
        l.append(a)
    return l

def return_semesters():
    l = []
    for cs in load_current_user().semesters:
        l.append(cs)
    return l


####################################### List Dumps #######################################
def pantry_dump():
    print('\nHere is your pantry:\n----------------------------------------------')
    for i in return_pantry():
        print(i.name)
    print('----------------------------------------------')

def cookbook_dump():
    print('\nHere is your cookbook:\n----------------------------------------------')
    for r in return_cookbook():
        print(r.name)
    print('----------------------------------------------')


def agenda_dump():
    print('\nHere is your agenda:\n----------------------------------------------')
    for a in return_agenda():
        print(a.name)
    print('----------------------------------------------')

def semesters_dump():
    print('\nHere are your semesters:\n----------------------------------------------')
    for cs in return_semesters():
        print(cs.name)
    print('----------------------------------------------')



# def get_all_ingredients_as_list():
#     directory = root + '/Meta/Ingredients/'
#     l = []
#     for entry in os.scandir(directory):
#         l.append(load_ingredient_from_meta(str(entry).strip("<>").split()[1].strip("'")))
#     return l

#
# def get_all_recipes_as_list():
#     directory = root + '/Meta/Recipes/'
#     l = []
#     for entry in os.scandir(directory):
#         l.append(load_recipe_from_meta(str(entry).strip("<>").split()[1].strip("'")))
#     return l
#
#
# def get_all_assignments_as_list():
#     directory = root + '/Meta/Assignments/'
#     l = []
#     for entry in os.scandir(directory):
#         l.append(load_assignment_from_meta(str(entry).strip("<>").split()[1].strip("'")))
#     return l
#
#
# def get_all_courselists_as_list():
#     directory = root + '/Meta/CourseLists/'
#     l = []
#     for entry in os.scandir(directory):
#         l.append(load_courselist_from_meta(str(entry).strip("<>").split()[1].strip("'")))
#     return l


####################################### Removes #######################################

def remove_ingredient_from_pantry(ingredient):
    user = load_current_user()
    for i in user.pantry:
        if i.name == ingredient:
            copy = i
            user.pantry.remove(i)
            user.save_user_data()
            return copy

def remove_recipe_from_cookbook(recipe):
    user = load_current_user()
    for r in user.cookbook:
        if r.name == recipe:
            copy = r
            user.cookbook.remove(r)
            user.save_user_data()
            return copy


def remove_assignment_from_agenda(assignment):
    user = load_current_user()
    for a in user.agenda:
        if a.name == assignment:
            copy = a
            user.agenda.remove(a)
            user.save_user_data()
            return copy


def remove_courselist_from_semesters(courselist):
    user = load_current_user()
    for cs in user.semesters:
        if cs.name == courselist:
            copy = cs
            user.semesters.remove(cs)
            user.save_user_data()
            return copy










# def remove_ingredient_from_meta(name):
#     filename = root + '/Meta/Ingredients/' + name
#     copy = load_ingredient_from_meta(name)
#     os.remove(filename)
#     return copy


# def remove_recipe_from_meta(name):
#     filename = root + '/Meta/Recipes/' + name
#     copy = load_recipe_from_meta(name)
#     os.remove(filename)
#     return copy
#
#
# def remove_assignment_from_meta(name):
#     filename = root + '/Meta/Assignments/' + name
#     copy = load_assignment_from_meta(name)
#     os.remove(filename)
#     return copy
#
#
# def remove_courselist_from_meta(name):
#     filename = root + '/Meta/CourseLists/' + name
#     copy = load_courselist_from_meta(name)
#     os.remove(filename)
#     return copy
#

####################################### Changes #######################################


def change_ingredient_in_pantry(ingredient):
    user = load_current_user()
    i = load_ingredient_from_pantry(ingredient)
    og_i = i.name
    new_i = i

    print("Which part of this ingredient am I changing?\n")
    l = ['name', 'serving_size', 'cal', 'tot_fat', 'sat_fat', 'trans_fat',
         'sodium', 'carbs', 'fiber', 'sugar', 'protein']
    for i in l:
        print(i)
    member = input('\n')
    new_data = input('What is the new ' + member + '?\n')


    if member == 'name':
        # og_name = i.name
        new_i.name = str(new_data)

    else:
        new_data = float(new_data)
        if member == 'serving_size':
            new_i.serving_size = new_data
        elif member == 'cal':
            new_i.cal = new_data
        elif member == 'tot_fat':
            new_i.tot_fat = new_data
        elif member == 'sat_fat':
            new_i.sat_fat = new_data
        elif member == 'trans_fat':
            new_i.trans_fat = new_data
        elif member == 'sodium':
            new_i.sodium = new_data
        elif member == 'carbs':
            new_i.carbs = new_data
        elif member == 'sugar':
            new_i.sugar = new_data
        elif member == 'protein':
            new_i.protein = new_data
    remove_ingredient_from_pantry(og_i)
    load_current_user().add_ingredient_to_pantry(new_i)
    load_current_user().save_user_data()
    return new_i

def change_recipe_in_cookbook(recipe):  # og, member

    user = load_current_user()
    r = load_recipe_from_cookbook(recipe)
    og_r = r.name
    new_r = r

    print("Which part of this recipe am I changing?\n")
    l = ['name', 'ingredients_list']
    for i in l:
        print(i)
    member = input('\n')
    # new_data = input('What is the new ' + member + '?\n')

    if member == 'name':
        new_r.name = input('What is the new ' + member + '?\n')
        remove_recipe_from_cookbook(og_r)
    else:
        x = input('Am I adding, removing, or changing an ingredient of this recipe?\n')
        i = input('Which ingredient am I ' + x + '\n')
        if x == 'adding':
            return new_r.add_new_ingredient_to_recipe(i)
        elif x == 'removing':
            return new_r.remove_ingredient_from_recipe(i)
        elif x == 'changing':
            return new_r.alter_ingredient_of_recipe(i)

    remove_recipe_from_cookbook(og_r)
    load_current_user().add_recipe_to_cookbook(new_r)
    load_current_user().save_user_data()

    return new_r

    ###### left here







# def change_ingredient_in_meta(ingredient):
#     print("Which part of this ingredient am I changing?\n")
#     i = load_ingredient_from_meta(ingredient)
#     og = i.name
#     new_i = i
#
#     l = ['name', 'serving_size', 'cal', 'tot_fat', 'sat_fat', 'trans_fat',
#          'sodium', 'carbs', 'fiber', 'sugar', 'protein']
#     for i in l:
#         print(i)
#     member = input('\n')
#     new_data = input('What is the new ' + member + '?\n')
#
#     # new_data = float(new_data)
#     if member == 'name':
#         # og_name = i.name
#         new_i.name = str(new_data)
#
#     else:
#         new_data = float(new_data)
#         if member == 'serving_size':
#             new_i.serving_size = new_data
#         elif member == 'cal':
#             new_i.cal = new_data
#         elif member == 'tot_fat':
#             new_i.tot_fat = new_data
#         elif member == 'sat_fat':
#             new_i.sat_fat = new_data
#         elif member == 'trans_fat':
#             new_i.trans_fat = new_data
#         elif member == 'sodium':
#             new_i.sodium = new_data
#         elif member == 'carbs':
#             new_i.carbs = new_data
#         elif member == 'sugar':
#             new_i.sugar = new_data
#         elif member == 'protein':
#             new_i.protein = new_data
#     remove_ingredient_from_meta(og)
#     filename = root + '/Meta/Ingredients/' + new_i.name
#     pickle_out = open(filename, 'wb')
#     pickle.dump(new_i, pickle_out)
#     pickle_out.close()
#     return new_i


# def change_recipe_in_meta(recipe):  # og, member
#     print("Which part of this recipe am I changing?\n")
#     l = ['name', 'ingredients_list']
#     for i in l:
#         print(i)
#     member = input('\n')
#
#     r = load_recipe_from_meta(recipe)
#     og = r.name
#     new_r = r
#
#     if member == 'name':
#         new_r.name = input('What is the new ' + member + '?\n')
#         remove_recipe_from_meta(og)
#     else:
#         x = input('Am I adding, removing, or changing an ingredient of this recipe?\n')
#         i = input('Which ingredient am I ' + x + '\n')
#         if x == 'adding':
#             return new_r.add_new_ingredient_to_recipe(i)
#         elif x == 'removing':
#             return new_r.remove_ingredient_from_recipe(i)
#         elif x == 'changing':
#             return new_r.alter_ingredient_of_recipe(i)
#
#     filename = root + '/Meta/Recipes/' + new_r.name
#     pickle_out = open(filename, 'wb')
#     pickle.dump(new_r, pickle_out)
#     pickle_out.close()
#     return new_r


def change_assignment_in_meta(assignment):
    print("Which part of this assignment am I changing?\n")
    l = ['course', 'name', 'description', 'due_date']
    for i in l:
        print(i)
    member = input('\n')
    new_data = input('What is the new ' + member + '?\n')

    a = load_assignment_from_meta(assignment)
    og = a.name
    new_a = a
    if member == 'name':
        new_a.name = new_data
    elif member == 'course':
        new_a.course = new_data
    elif member == 'due_date':
        new_a.due_date = new_data
    elif member == 'description':
        new_a.description = new_data
    remove_assignment_from_meta(og)
    filename = root + '/Meta/Assignments/' + new_a.name
    pickle_out = open(filename, 'wb')
    pickle.dump(new_a, pickle_out)
    pickle_out.close()
    return new_a


def change_courselist_in_meta(courselist, member):
    cs = load_courselist_from_meta(courselist)
    og = cs.name
    new_cs = cs
    if member == 'name':
        new_cs.name = input('What is the new name?\n')
        remove_courselist_from_meta(og)
        filename = root + '/Meta/CourseLists/' + new_cs.name
        pickle_out = open(filename, 'wb')
        pickle.dump(new_cs, pickle_out)
        pickle_out.close()
        return new_cs
    else:
        x = input('Would you like to add or remove a class from this courselist?\n')
        if x == 'add':
            cs.add_new_course_to_courselist()
        elif x == 'remove':
            cs.remove_course_from_courselist()
        return cs


####################################### Helpers #######################################
def is_plural(s):
    p = inflect.engine()
    key = True
    k = p.singular_noun(s)
    if not k:
        key = False
    return key

####################################### Users/Bots #######################################


def load_bot_from_meta(bot):
    filename = root + '/Meta/Bots/' + bot
    pickle_in = open(filename, 'rb')
    b = pickle.load(pickle_in)
    return b

def load_current_user():
    filename = root + '/CurrentUser'
    pickle_in = open(filename, 'rb')
    u = pickle.load(pickle_in)
    return u

def load_user_from_meta(user):
    filename = root + '/UserMeta/' + user
    pickle_in = open(filename, 'rb')
    u = pickle.load(pickle_in)
    return u


def set_current_user(user):

    filename = root + '/CurrentUser'
    pickle_out = open(filename, 'wb')
    pickle.dump(user, pickle_out)
    pickle_out.close()

    return user
