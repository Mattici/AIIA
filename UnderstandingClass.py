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
        self.og_class_name = og_class_name
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

        self.get_command(h)
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
            self.for_context = prev_u.for_context
        # might need to be put i else statement
        else:
            self.get_class_name()
            self.get_plural_bool()
            self.get_system_commands()
            self.send_to_frontal_lobe(u=self)

        u_stack.append(self)  ## adds understanding to wernickes area. Make sure to save bots brain (sleep) to
        # bot.

    def send_to_frontal_lobe(self, u):
        bot = hf.load_current_bot()
        fl = bot.frontal_lobe
        h = bot.hippocampus
        l = []
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
            h.to_string()

        self.for_context = l

    def get_verbs(self):
        l = nltk.word_tokenize(self.s)
        verbs = []
        for i in range(len(l)):
            if (nltk.pos_tag(l)[i][1][0] == 'V'):
                verbs.append(l[i])
        return verbs

    def get_command(self, h):
        sentence = self.s
        l = nltk.word_tokenize(sentence)
        for word in l:
            for i in h.commands:
                for j in h.commands[i]:
                    if word == j:
                        self.command = i

    def get_class_name(self):

        h = hf.load_current_bot().hippocampus
        sentence = self.s
        l = nltk.word_tokenize(sentence)
        for word in l:
            if word == 'all':
                self.plural = True
            for i in h.classes:
                for j in h.classes[i]:
                    if word == j:
                        self.class_name = i
                        self.og_class_name = word
        if self.class_name == 'ingredient':
            self.container = 'pantry'
        elif self.class_name == 'recipe':
            self.container = 'cookbook'
        elif self.class_name == 'assignment':
            self.container = 'agenda'
        elif self.class_name == 'courselist':
            self.container = 'semesters'

    def get_plural_bool(self):
        s = self.og_class_name
        self.plural = hf.is_plural(s)

    def get_system_commands(self):
        bot = hf.load_current_bot()
        h = bot.hippocampus
        sentence = self.s
        l = nltk.word_tokenize(sentence)
        for word in l:
            for i in h.system_commands:
                for j in h.system_commands[i]:
                    if word == j:
                        self.system_command = i