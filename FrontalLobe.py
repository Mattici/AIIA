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
        container = u.container

        if command == 'add':
            if (class_name == 'bot') or (class_name == 'user'):
                s = 'new_' + class_name
            else:
                s = 'add_new_' + class_name + '_to_' + container
            add_class = getattr(hf, s)
            l = []
            if not plural:
                l.append(add_class())
            else:
                x = int(input('How many ' + og_class_name + ' would you like to add?\n'))
                for f in range(x):
                    print(class_name + ' ' + str(f + 1) + ':')
                    l.append(add_class())
                    print('\n')
            return l


        elif command == 'view':
            f = 'return_' + container
            loader = getattr(hf, f)
            a = loader()  # return list set to whole container
            s = container + '_dump'
            dumper = getattr(hf, s)
            dumper()  # dump list
            if not plural:  # specify the class_name in singular
                t = input('Which ' + class_name + ' would you like to view?\n')
                s = 'load_' + class_name + '_from_' + container
                thing_viewer = getattr(hf, s)
                thing = thing_viewer(t)
                a = []  # reset return list
                a.append(thing)
                thing.to_string()
            return a

        elif command == 'remove':

            s = container + '_dump'
            dumper = getattr(hf, s)
            dumper()  # dump list

            a = []
            if not plural:
                g = input('Which ' + class_name + ' would you like to remove?\n')
                s = 'remove_' + class_name + '_from_' + container
                remove_class = getattr(hf, s)
                a.append(remove_class(g))

            else:
                x = int(input('How many ' + class_name + 's would you like to remove?\n'))
                for i in range(x):
                    g = input('Which ' + class_name + 's would you like to remove?\n')
                    s = 'remove_' + class_name + '_from_' + container
                    remove_class = getattr(hf, s)
                    a.append(remove_class(g))
            return a

        elif command == 'change':
            s = container + '_dump'
            dumper = getattr(hf, s)
            dumper()  # dump list

            a = []
            og = input('Which ' + class_name + ' would you like to change? ')

            if class_name == 'ingredient':
                ret = hf.change_ingredient_in_pantry(og)

            elif class_name == 'recipe':
                ret = hf.change_recipe_in_cookbook(og)

            elif class_name == 'assignment':
                ret = hf.change_assignment_in_agenda(og)

            elif class_name == 'courselist':
                ret = hf.change_courselist_in_semesters(og)
            a.append(ret)
            return a

        elif system_command == 'help':
            hf.load_current_bot()
            # hf.load_bot_from_meta('Mia')