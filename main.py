#   Start Date: 3/7


from HelperFunctions import *
from HippocampusClass import Hippocampus
from UserClass import User

if __name__ == '__main__':
    #    next need to add more data to Hippocampus:
    #     * same_command: [again, another]  do the command of previous understanding

    #
    # for x in range (10):
    #     print(x)



    ######### left at working on change container methods in helperfunctions

    # user = load_user_from_meta(input('Who am I helping?\n'))
    user = load_user_from_meta('Matt')
    set_current_user(user)

    # bot = load_bot_from_meta(input('Which bot?\n'))
    bot = load_bot_from_meta('Mia')
    set_current_bot(bot)

    bot.user_request()

    # h.classes.update({'bot': ['bot']})
    # h.classes.update({'user': ['user']})
    # save_thing_somewhere(h)
    # new_user()

    # bot = load_bot_from_meta(input('Which bot?\n'))
    # set_current_bot(bot)
    # bot.user_request()








#   Later add: serving sizes, vitamins, other nutrients
