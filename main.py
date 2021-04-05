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



    ## work list
    ## exit system
    ## context needs to get updated each request
    ## try catches for each input (thats not how i usually understand those)

    ######### left at working on change container methods in helperfunctions

    matt = load_user_from_meta('Matt')
    set_current_user(matt)

    mia = load_bot_from_meta('Mia')
    set_current_bot(mia)



    mia.user_request()










#   Later add: serving sizes, vitamins, other nutrients
