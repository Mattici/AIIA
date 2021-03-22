import nltk

from HelperFunctions import *
from FrontalLobe import *

### could hold possible context for next line

class Understanding(object):
    def __init__(self, s='', command='', class_name='', system_command='', plural=False, og_class_name='', for_context=None):
        self.s = s
        self.command = command
        self.class_name = class_name
        self.system_command = system_command
        self.plural = plural
        self.og_class_name = og_class_name
        if for_context is None:
            self.for_context = []

    def to_string(self):
        print('Sentence: ' + self.s)
        print('Command: ' + self.command)
        print('Class Name: ' + self.class_name)
        print('Plural: ' + str(self.plural))
        print('OG Class Name: ' + self.og_class_name)
        print('Context:\n')
        if self.for_context is None:
            print('')
        else:
            print(self.for_context)
            for thing in self.for_context:
                thing.to_string()

    def understand(self, bot):
        h = bot.hippocampus
        #fl = bot.frontal_lobe
        w = bot.wernickes_area

        # if self.s contain context identifier, execute_context
        u_stack = w.u_stack
        self.get_command(h)
        if h.has_context_clue(self.s): #### check wernickes area for short term memory (conversation context)
            # could slide in an again conditional to set command if contains again.
            prev_u = u_stack.pop()
            self.class_name = prev_u.class_name
            #self.plural = prev_u.plural
            if self.command == 'remove':
                for thing in prev_u.for_context:
                    s = 'remove_' + self.class_name + '_from_meta'
                    f = getattr(hf, s)
                    t = f(thing.name)
            elif self.command == 'view':
                for thing in prev_u.for_context:
                    thing.to_string()
            elif self.command == 'change':
                for thing in prev_u.for_context:
                    s = 'change_' + self.class_name + '_in_meta'
                    f = getattr(hf, s)
                    t = f(thing.name)


            self.for_context = prev_u.for_context
            #u_stack.append(t)





        # might need to be put i else statement
        else:
            self.get_class_name(h=h)
            self.get_plural_bool()
            self.get_system_commands(h=h)
            self.send_to_frontal_lobe(u=self, bot=bot)

        u_stack.append(self) ## adds understanding to wernickes area. Make sure to save bots brain (sleep) to
        # bot.
    def send_to_frontal_lobe(self, u, bot):
        fl = bot.frontal_lobe
        h = bot.hippocampus
        l = []
        if self.class_name != '' and self.command != '':  # knows command and class_name
            l = fl.execute_function(u) # l is list of context items
            self.for_context = l
        elif self.class_name == '' and self.command != '':  # knows command but not class_name
            print('I know that want me to ' + self.command +
                  ' something, but I am not sure what that something is\n')
            self.s = input('What would you like to ' + self.command + ' ?\n')
            self.get_class_name()
            self.get_plural_bool()
            l = fl.execute_function(u)
            self.for_context = l
        elif self.class_name != '' and self.command == '': # knows class_name but not command
            self.s = input('What would you like to do with this ' + self.class_name + ' ?\n')
            self.get_command(h)
            l = fl.execute_function(u)
            self.for_context = l

        elif self.system_command != '':  ##### need to fix to do exit and help, not just help. On exit, save and end main.
            # m = load_the_hippocampus_from_meta()
            # m.to_string()
            h.to_string()

        self.for_context = l

        # system commands (exit, help)

        # unsure what to do
        # command == '' and/or class_name == ''

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

    def get_class_name(self, h):
        #h = load_the_hippocampus_from_meta()
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

    def get_plural_bool(self):
        s = self.og_class_name
        self.plural = is_plural(s)

    def get_system_commands(self, h):
        #h = load_the_hippocampus_from_meta()
        sentence = self.s
        l = nltk.word_tokenize(sentence)
        for word in l:
            for i in h.system_commands:
                for j in h.system_commands[i]:
                    if word == j:
                        self.system_command = i