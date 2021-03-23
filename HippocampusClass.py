import nltk
from HelperFunctions import *


class Hippocampus(object):
    def __init__(self, classes=None, commands=None, system_commands=None, context_clues=None):
        if classes is None:
            self.classes = {}  # each member: class_name: [synonyms]
        if commands is None:
            self.commands = {}  # each member: command_tag: [synonyms]
        if system_commands is None:
            self.system_commands = {}
        if context_clues is None:
            self.context_clues = {}

    def to_string(self):
        print('\nI can...\n----------------------------------------------')
        for command in self.commands.keys():
            s = ''
            for syn in self.commands.get(command):
                s += syn + ', '
            print(command + '\t\t(' + s.strip().strip(',') + ')')
        print(
            '----------------------------------------------\nTo the following things:\n----------------------------------------------')
        for class_name in self.classes.keys():
            s = ''
            for syn in self.classes.get(class_name):
                s += syn + ', '
            print(class_name + 's\t\t(' + s.strip().strip(',') + ')')
        print(
            '----------------------------------------------\nSytstem Commands:\n----------------------------------------------')
        for system_command in self.system_commands.keys():
            s = ''
            for syn in self.system_commands.get(system_command):
                s += syn + ', '
            print(system_command + '\t\t(' + s.strip().strip(',') + ')')
        print(
            '----------------------------------------------\nContext Clues:\n----------------------------------------------')
        for context_clue in self.context_clues.keys():
            s = ''
            for syn in self.context_clues.get(context_clue):
                s += syn + ', '
            print(context_clue + '\t\t(' + s.strip().strip(',') + ')')

    def add_basic_command_synonyms(self, command, syn):
        self.commands.update({command: syn})
        self.save_hippocampus()

    def add_basic_class_synonyms(self, class_name, syn):
        self.classes.update({class_name: syn})
        self.save_hippocampus()

    def save_hippocampus(self):
        filename = '/OriginalBrainFiles/TheHippocampus'
        pickle_out = open(filename, 'wb')
        pickle.dump(self, pickle_out)
        pickle_out.close()

    def has_context_clue(self, sentence):
        l = nltk.word_tokenize(sentence)
        for word in l:
            for i in self.context_clues:
                for j in self.context_clues[i]:
                    if word == j:
                        return True
        return False