import HelperFunctions as hf

class FrontalLobe(object):

    def __init__(self):
        self


    def execute_function(self, u):
        command = u.command
        class_name = u.class_name
        plural = u.plural
        system_command = u.system_command
        og_class_name = u.og_class_name
        if command == 'add':
            s = 'add_' + class_name + '_to_meta'
            add_class = getattr(hf, s)
            l = []
            if not plural:
                l.append(add_class())
            else:
                x = int(input('How many ' + og_class_name + ' would you like to add?\n'))
                for f in range(x):
                    print(class_name + ' ' + str(f+1) + ':')
                    l.append(add_class())
                    print('\n')
            return l

        elif command == 'view':
            print('\nHere are your ' + class_name + 's:\n')
            a = []
            s = 'get_all_' + class_name + 's_as_list'
            list_getter = getattr(hf, s)
            l = list_getter()
            print('----------------------------------------------')
            for thing in l:
                print(thing.name)
                a.append(thing)
            print('----------------------------------------------')
            if not plural:
                print('Which ' + class_name + ' would you like to view?\n')
                t = input()
                s = 'load_' + class_name + '_from_meta'
                thing_viewer = getattr(hf, s)
                thing = thing_viewer(t)
                a = []
                a.append(thing)
                thing.to_string()
            return a

        elif command == 'remove':
            print('Here are your current ' + class_name + 's:\n')
            s = 'get_all_' + class_name + 's_as_list'
            list_getter = getattr(hf, s)
            print('----------------------------------------------')
            l = list_getter()
            a = []
            for thing in l:
                print(thing.name)
            print('----------------------------------------------')
            if not plural:
                g = input('Which ' + class_name + ' would you like to remove?\n')
                s = 'remove_' + class_name + '_from_meta'
                remove_class = getattr(hf, s)
                a.append(remove_class(g))

            else:
                x = int(input('How many ' + class_name + 's would you like to remove?\n'))
                for i in range(x):
                    g = input('Which ' + class_name + 's would you like to remove?\n')
                    s = 'remove_' + class_name + '_from_meta'
                    remove_class = getattr(hf, s)
                    a.append(remove_class(g))

            return a
        elif command == 'change':
            a = []
            print('\nHere are your ' + class_name + 's:\n')
            s = 'get_all_' + class_name + 's_as_list'
            list_getter = getattr(hf, s)
            print('----------------------------------------------')
            l = list_getter()
            for thing in l:
                print(thing.name)
            print('\n')
            print('----------------------------------------------')
            og = input('Which ' + class_name + ' would you like to change? ')

            if class_name == 'ingredient':
                con = hf.change_ingredient_in_meta(og)

            elif class_name == 'recipe':
                con = hf.change_recipe_in_meta(og)

            elif class_name == 'assignment':
                con = hf.change_assignment_in_meta(og)


            elif class_name == 'courselist':
                l = ['name', 'courses']
                for i in l:
                    print(i)
                member = input('\n')
                con = hf.change_courselist_in_meta(og, member)
            return con

        elif system_command == 'help':
            hf.load_bot_from_meta('Mia')
