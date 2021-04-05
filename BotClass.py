import os
import sys
from datetime import datetime

import HelperFunctions as hf
from FrontalLobe import FrontalLobe
from HippocampusClass import Hippocampus
from UnderstandingClass import Understanding
from WernickesAreaClass import WernickesArea
import pickle

class Bot(object):

    # Bot born
    def __init__(self, name='', hippocampus=None, frontal_lobe=None, wernickes_area=None, birth_date=None):
        self.name = name
        if hippocampus is None:
            # self.hippocampus = hf.load_the_hippocampus()
            self.hippocampus = Hippocampus()
        if frontal_lobe is None:
            self.frontal_lobe = FrontalLobe()
        if wernickes_area is None:
            self.wernickes_area = WernickesArea()
        if birth_date is None:
            self.birth_date = datetime.now()

    def to_string(self):
        bday = self.birth_date.strftime("%m/%d/%Y, %H:%M:%S")
        print('\nHello my name is ' + self.name + ', I was born ' + bday + '\n')

    def user_request(self):
        print('\nHow may I help you? \n')
        for line in sys.stdin:
            line = line.rstrip().lower()
            u = Understanding(s=line)
            u.understand()
            print('\nHow else can I help you?\n')

    def sleep(self):
        ## bot sleeps on all info its gathered to learn
        root = os.getcwd()
        filename = root + '/BotMeta/' + self.name
        pickle_out = open(filename, 'wb')
        pickle.dump(self, pickle_out)
        pickle_out.close()
        # hf.set_current_bot(self)

    def change_name(self, name):
        self.name = name
        root = os.getcwd()
        filename = root + '/BotMeta/' + name
        pickle_out = open(filename, 'wb')
        pickle.dump(self, pickle_out)
        pickle_out.close()
        self.sleep()
        hf.set_current_bot(self)

    def remember_short_term(self, u): #remember previous understanding
        self.wernickes_area.u_stack.append(u)

