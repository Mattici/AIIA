class Assignment(object):
    def __init__(self, course='', name='', description='', due_date=''):
        self.course = course
        self.name = name
        self.due_date = due_date
        self.description = description

    def to_string(self):
        print('\n')
        print('----------------------------------------------')
        print('Course: ' + self.course)
        print('Assignment: ' + self.name)
        print('Description: ' + self.description)
        print('Due: ' + self.due_date)
        print('----------------------------------------------')

