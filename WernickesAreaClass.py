class WernickesArea(object):

    def __init__(self):
        self.u_stack = []


    def remember_short_term(self, u):
        self.u_stack.append(u)
