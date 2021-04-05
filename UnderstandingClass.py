import nltk

import HelperFunctions as hf
from FrontalLobe import *


class Understanding(object):
    def __init__(self, s='', command='', class_name='', system_command='', plural=False, og_class_name='',
                 for_context=None, container=''):
        self.s = s
        self.command = command
        self.class_name = class_name
        self.system_command = system_command
        self.plural = plural
        self.og_class_name = og_class_name # for printing purposes "here are your SYN's"
        if for_context is None:
            self.for_context = []
        self.container = container

    def to_string(self):
        print('Sentence: ' + self.s)
        print('Command: ' + self.command)
        print('Class Name: ' + self.class_name)
        print('Container: ' + self.container)
        print('Plural: ' + str(self.plural))
        print('OG Class Name: ' + self.og_class_name)
        print('Context:\n')
        if self.for_context is None:
            print('')
        else:
            print(self.for_context)
            for thing in self.for_context:
                thing.to_string()

    def understand(self):
        bot = hf.load_current_bot()
        h = bot.hippocampus
        w = bot.wernickes_area
        u_stack = w.u_stack

        self.get_command()

        # has context clue
        if h.has_context_clue(self.s):  #### check wernickes area for short term memory (conversation context)
            prev_u = u_stack.pop()
            self.class_name = prev_u.class_name
            self.container = prev_u.container
            self.plural = prev_u.plural
            if self.command == 'remove':
                t = []
                for thing in prev_u.for_context:
                    s = 'remove_' + self.class_name + '_from_' + self.container
                    f = getattr(hf, s)
                    t.append(f(thing.name))
            elif self.command == 'view':
                t = []
                for thing in prev_u.for_context:
                    # prev_u.to_string()
                    t.append(thing)
                    thing.to_string()
            elif self.command == 'change':
                t = []
                for thing in prev_u.for_context:
                    s = 'change_' + self.class_name + '_in_' + self.container
                    f = getattr(hf, s)
                    t.append(f(thing.name))
            self.for_context = t
        # make understanding
        else: # doesnt have context clue
            self.get_class_name()
            self.get_plural_bool()
            self.send_to_frontal_lobe(u=self)

        bot.remember_short_term(self)
        bot.sleep()

    def send_to_frontal_lobe(self, u):
        bot = hf.load_current_bot()
        fl = bot.frontal_lobe
        h = bot.hippocampus
        l = [] #for context list
        if self.class_name != '' and self.command != '':  # knows command and class_name
            l = fl.execute_function(u)  # l is list of context items
            self.for_context = l
        elif self.class_name == '' and self.command != '':  # knows command but not class_name
            print('I know that want me to ' + self.command +
                  ' something, but I am not sure what that something is\n')
            self.s = input('What would you like to ' + self.command + ' ?\n')
            self.get_class_name()
            self.get_plural_bool()
            l = fl.execute_function(u)
            self.for_context = l
        elif self.class_name != '' and self.command == '':  # knows class_name but not command
            self.s = input('What would you like to do with this ' + self.class_name + ' ?\n')
            self.get_command(h)
            l = fl.execute_function(u)
            self.for_context = l

        elif self.system_command != '':  ##### need to fix to do exit and help, not just help. On exit, save and end main.
            # m = load_the_hippocampus_from_meta()
            # m.to_string()
            if self.system_command == 'help':
                hf.load_current_bot().hippocampus.to_string()
                # h.to_string()
            elif self.system_command == 'exit':
                quit()

        self.for_context = l

    def get_verbs(self):
        l = nltk.word_tokenize(self.s)
        verbs = []
        for i in range(len(l)):
            if (nltk.pos_tag(l)[i][1][0] == 'V'):
                verbs.append(l[i])
        return verbs

    def get_command(self): # or system command
        h = hf.load_current_bot().hippocampus
        sentence = self.s
        l = nltk.word_tokenize(sentence)
        for word in l:
            if word in h.commands.get('add'):
                self.command = 'add'
            elif word in h.commands.get('remove'):
                self.command = 'remove'
            elif word in h.commands.get('change'):
                self.command = 'change'
            elif word in h.commands.get('view'):
                self.command = 'view'
            elif word in h.commands.get('teach'):
                self.command = 'teach'
            elif word in h.system_commands.get('help'):
                self.system_command = 'help'
            elif word in h.system_commands.get('exit'):
                self.system_command = 'exit'


    def get_class_name(self):

        h = hf.load_current_bot().hippocampus
        sentence = self.s
        l = nltk.word_tokenize(sentence)

        for word in l:
            if word in h.classes.get('ingredient'):
                self.class_name = 'ingredient'
                self.og_class_name = word
            elif word in h.classes.get('recipe'):
                self.class_name = 'recipe'
                self.og_class_name = word
            elif word in h.classes.get('assignment'):
                self.class_name = 'assignment'
                self.og_class_name = word
            elif word in h.classes.get('courselist'):
                self.class_name = 'courselist'
                self.og_class_name = word
            elif word in h.classes.get('bot'):
                self.class_name = 'bot'
                self.og_class_name = word
            elif word in h.classes.get('user'):
                self.class_name = 'user'
                self.og_class_name = word

        if self.class_name == 'ingredient':
            self.container = 'pantry'
        elif self.class_name == 'recipe':
            self.container = 'cookbook'
        elif self.class_name == 'assignment':
            self.container = 'agenda'
        elif self.class_name == 'courselist':
            self.container = 'semesters'
        elif self.class_name == 'user':
            self.container = 'meta'
        elif self.class_name == 'bot':
            self.container = 'meta'
        elif self.class_name == 'synonym':
            self.container = 'hippocampus'

    def get_plural_bool(self):
        s = self.og_class_name
        self.plural = hf.is_plural(s)

    # def get_system_commands(self):
    #     bot = hf.load_current_bot()
    #     h = bot.hippocampus
    #     sentence = self.s
    #     l = nltk.word_tokenize(sentence)
    #     for word in l:
    #         for i in h.system_commands:
    #             for j in h.system_commands[i]:
    #                 if word == j:
    #                     self.system_command = i