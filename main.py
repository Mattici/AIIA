#   Start Date: 3/7


from HelperFunctions import *
from UserClass import User

if __name__ == '__main__':

    #    next need to add more data to Hippocampus:
    #     * same_command: [again, another]  do the command of previous understanding



######### left at working on change container methods in helperfunctions


    name = name=input('Who am I helping?\n')
    user = load_user_from_meta(name)
    set_current_user(user)

    # for thing in return_pantry():
    #     print(thing)
    # for thing in return_cookbook():
    #     print(thing)
    # for thing in return_agenda():
    #     print(thing)
    # for thing in return_semesters():
    #     print(thing)



    mia = load_bot_from_meta('Mia')
    mia.user_request()

    user.to_string()










#   Later add: serving sizes, vitamins, other nutrients


