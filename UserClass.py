import pickle

import os
# from HelperFunctions import set_current_user
import HelperFunctions as hf


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

    def add_courselist_to_semesters(self, s):
        self.semesters.append(s)
        self.save_user_data()
        return s

    def save_user_data(self):
        root = os.getcwd()
        filename = root + '/UserMeta/' + self.name
        pickle_out = open(filename, 'wb')
        pickle.dump(self, pickle_out)
        pickle_out.close()
        hf.set_current_user(self)
