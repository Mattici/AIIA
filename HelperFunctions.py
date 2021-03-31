import functools
import operator

import inflect
import pickle
import os

from BotClass import Bot
from IngredientClass import Ingredient
from RecipeClass import Recipe
from AssignmentClass import Assignment
from CourseListClass import CourseList
from UserClass import User

root = os.getcwd()


####################################### Adds #######################################

#####                Adds class_name to container. Saves user                  #####

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
    semesters_dump()
    sem = input('Which semester is this assignment for?')
    s = load_courselist_from_semesters(sem)
    for c in s.courses:
        print(c)
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


####################################### Loads #######################################

#####                     Loads class_name from container                       #####

####################################### Loads #######################################


def load_ingredient_from_pantry(ingredient):
    user = load_current_user()
    for i in user.pantry:
        if i.name == ingredient:
            return i
            break
    else:
        print('There are no ' + ingredient + 's in your pantry')


def load_recipe_from_cookbook(recipe):
    user = load_current_user()
    for r in user.cookbook:
        if r.name == recipe:
            return r
            break
    else:
        print("You don't have " + recipe + "in your cookbook")


def load_assignment_from_agenda(assignment):
    user = load_current_user()
    for a in user.agenda:
        if a.name == assignment:
            return a
            break
    else:
        print(assignment + ' is not in your agenda')


def load_courselist_from_semesters(courselist):
    user = load_current_user()
    for cs in user.semesters:
        if courselist == cs.name:
            return cs
            break
    else:
        print(courselist + ' is not one of your semesters')


####################################### Get Lists #######################################

#####                Returns class_names from container as list                     #####

####################################### Get Lists #######################################

def return_pantry():
    l = []
    for i in load_current_user().pantry:
        l.append(i)
    # sorted_l = l.sort(key=lambda i: i.name)
    # print(l)
    # print(sorted_l)
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

#####                               Prints container                                 #####

####################################### List Dumps #######################################


def pantry_dump():
    print('\nHere is your pantry:\n----------------------------------------------')
    l = return_pantry()
    sorted_l = sorted(l, key=lambda i: i.name)
    for i in sorted_l:
        print(i.name)
    print('----------------------------------------------')


def cookbook_dump():
    print('\nHere is your cookbook:\n----------------------------------------------')
    l = return_cookbook()
    sorted_l = sorted(l, key=lambda r: r.name)
    for r in sorted_l:
        print(r.name)
    print('----------------------------------------------')


def agenda_dump():
    print('\nHere is your agenda:\n----------------------------------------------')
    l = return_agenda()
    sorted_l = sorted(l, key=lambda a: a.name)
    for a in sorted_l:
        print(a.name)
    print('----------------------------------------------')


def semesters_dump():
    print('\nHere are your semesters:\n----------------------------------------------')
    l = return_semesters()
    sorted_l = sorted(l, key=lambda cs: cs.name)
    for cs in sorted_l:
        print(cs.name)
    print('----------------------------------------------')


####################################### Removes #######################################

#####                    Removes class_name from container                        #####

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


####################################### Changes #######################################

#####                       Changes class_name in container                       #####

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
            new_r = new_r.add_new_ingredient_to_recipe(i)
            remove_recipe_from_cookbook(og_r)
            load_current_user().add_recipe_to_cookbook(new_r)
            load_current_user().save_user_data()
            return new_r
            # return new_r.add_new_ingredient_to_recipe(i)
        elif x == 'removing':
            new_r = new_r.remove_ingredient_from_recipe(i)
            remove_recipe_from_cookbook(og_r)
            load_current_user().add_recipe_to_cookbook(new_r)
            load_current_user().save_user_data()
            return new_r
            # return new_r.remove_ingredient_from_recipe(i)
        elif x == 'changing':
            new_r = new_r.alter_ingredient_of_recipe(i)
            remove_recipe_from_cookbook(og_r)
            load_current_user().add_recipe_to_cookbook(new_r)
            load_current_user().save_user_data()
            return new_r
            # return new_r.alter_ingredient_of_recipe(i)



    return new_r


def change_assignment_in_agenda(assignment):
    a = load_assignment_from_agenda(assignment)
    og_a = a.name
    new_a = a
    print("Which part of this assignment am I changing?\n")
    l = ['course', 'name', 'description', 'due_date']
    for i in l:
        print(i)
    member = input('\n')
    new_data = input('What is the new ' + member + '?\n')

    if member == 'name':
        new_a.name = new_data
    elif member == 'course':
        new_a.course = new_data
    elif member == 'due_date':
        new_a.due_date = new_data
    elif member == 'description':
        new_a.description = new_data
    remove_assignment_from_agenda(og_a)
    load_current_user().add_assignment_to_agenda(new_a)
    load_current_user().save_user_data()
    return new_a

    ###### left here


def change_courselist_in_semesters(courselist):
    cs = load_courselist_from_semesters(courselist)
    og_cs = cs.name
    new_cs = cs
    print("Which part of this semester am I changing?\n")
    l = ['name', 'courses']
    for i in l:
        print(i)
    member = input('\n')

    if member == 'name':
        new_cs.name = input('What is the new name?\n')
        remove_courselist_from_semesters(og_cs)
        load_current_user().add_courselist_to_semesters(new_cs)
        load_current_user().save_user_data()
        return new_cs

    else:
        x = input('Would you like to add or remove a class from this semester?\n')
        if x == 'add':
            new_cs.add_course_to_courselist()
        elif x == 'remove':
            new_cs.remove_course_from_courselist()

        remove_courselist_from_semesters(og_cs)
        load_current_user().add_courselist_to_semesters(new_cs)
        load_current_user().save_user_data()
        return new_cs


####################################### Other Helpers #######################################


def is_plural(s):
    p = inflect.engine()
    key = True
    k = p.singular_noun(s)
    if not k:
        key = False
    return key


####################################### Users/Bots #######################################

#####                  All commands for the User and Bot classes                     #####

####################################### Users/Bots #######################################


def new_user():
    name = input('What is your name?\n')
    user = User(name=name)
    user.save_user_data()
    print('Switched ' + user.name + ' to current user')
    return user


def new_bot():
    name = input('What is my name?\n')
    bot = Bot(name=name)
    bot.sleep()
    return bot


def load_user_from_meta(user):
    filename = root + '/UserMeta/' + user
    pickle_in = open(filename, 'rb')
    u = pickle.load(pickle_in)
    return u


def load_bot_from_meta(bot):
    filename = root + '/BotMeta/' + bot
    pickle_in = open(filename, 'rb')
    b = pickle.load(pickle_in)
    return b


def load_current_user():
    filename = root + '/CurrentUser'
    pickle_in = open(filename, 'rb')
    u = pickle.load(pickle_in)
    return u


def set_current_user(user):
    filename = root + '/CurrentUser'
    pickle_out = open(filename, 'wb')
    pickle.dump(user, pickle_out)
    pickle_out.close()

    return user


def load_current_bot():
    filename = root + '/CurrentBot'
    pickle_in = open(filename, 'rb')
    b = pickle.load(pickle_in)
    return b


def set_current_bot(bot):
    filename = root + '/CurrentBot'
    pickle_out = open(filename, 'wb')
    pickle.dump(bot, pickle_out)
    pickle_out.close()
    return bot


def save_thing_somewhere(thing):
    filename = root + '/DefaultBotData/TheHippocampus'
    pickle_out = open(filename, 'wb')
    pickle.dump(thing, pickle_out)
    pickle_out.close()


def load_the_hippocampus():
    filename = root + '/DefaultBotData/TheHippocampus'
    pickle_in = open(filename, 'rb')
    t = pickle.load(pickle_in)
    return t
