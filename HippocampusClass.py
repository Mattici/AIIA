import nltk
import HelperFunctions as hf


# import BotClass as B


class Hippocampus(object):
    def __init__(self, classes=None, commands=None, system_commands=None, context_clues=None,
                 class_sets=None, command_sets=None, context_clue_sets=None):
        if classes is None:
            self.classes = {'ingredient': {'ingredient'},
                            'recipe': {'recipe'},
                            'assignment': {'assignment'},
                            'courselist': {'courselist'},
                            'user': {'user'},
                            'bot': {'bot'}}
            # 'synonym': {'synonym'}}# each member: class_name: [synonyms]
        if commands is None:
            self.commands = {'add': {'add'},
                             'remove': {'remove'},
                             'change': {'change'},
                             'view': {'view'},
                             'teach': {'teach'}}  # each member: command_tag: [synonyms]
        if system_commands is None:
            self.system_commands = {'help': {'help'},
                                    'exit': {'exit'}}
        if context_clues is None:
            self.context_clues = {'that': {'that'}}


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
        self.commands.get(command).add(syn)
        self.save_hippocampus()

    def add_basic_class_synonyms(self, class_name, syn):
        self.classes.get(class_name).add(syn)
        self.save_hippocampus()

    def remember_long_term(self, key, syn):
        if key in self.classes.keys():
            self.classes.get(key).add(syn)
        elif key in self.commands.keys():
            self.commands.get(key).add(syn)
        elif key in self.system_commands.keys():
            self.system_commands.get(key).add(syn)
        elif key in self.context_clues.keys():
            self.context_clues.get(key).add(syn)
        self.save_hippocampus()

    def save_hippocampus(self):
        new_h = self
        bot = hf.load_current_bot()
        bot.hippocampus = new_h
        hf.set_current_bot(bot)
        bot.sleep()

    def has_context_clue(self, sentence):
        l = nltk.word_tokenize(sentence)
        for word in l:
            for i in self.context_clues:
                for j in self.context_clues[i]:
                    if word == j:
                        return True
        return False
