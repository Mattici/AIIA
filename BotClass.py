import sys
from datetime import datetime

from HelperFunctions import *
from HippocampusClass import Hippocampus
from FrontalLobe import FrontalLobe
from UnderstandingClass import Understanding
from WernickesAreaClass import WernickesArea

class Bot(object):

    # Bot born
    def __init__(self, name='', hippocampus=None, frontal_lobe=None, wernickes_area=None, birth_date=None):
        self.name = name
        if hippocampus is None:
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
            u.understand(bot=self)


            print('\nHow else can I help you?\n')

    def sleep(self):
        ## bot sleeps on all info its gathered to learn
        root = os.getcwd()
        filename = root + '/Bots/' + self.name
        pickle_out = open(filename, 'wb')
        pickle.dump(self, pickle_out)
        pickle_out.close()


