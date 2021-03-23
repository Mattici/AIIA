
class CourseList(object):

    def __init__(self, name='', courses=None):
        if courses is None:
            self.courses = []
        self.name = name

    def to_string(self):

        print('----------------------------------------------')

        print(self.name + ":")
        print('----------------------------------------------')

        for c in self.courses:
            print(c)
        print('----------------------------------------------\n')


    def remove_course_from_courselist(self):
        print('\nCurrent Courses:\n')
        for c in self.courses:
            print(c)
        course = str(input('\nWhich course would you like to remove?\n'))
        for c in self.courses:
            if c == course:
                self.courses.remove(c)

    def add_course_to_courselist(self):
        print('\nCurrent Course:\n')
        for c in self.courses:
            print(c)
        x = str(input('\nWhich course would you like to add (example, CS4710)?\n'))
        self.courses.append(x)

    def print_all_courses(self):
        for c in self.courses:
            print(c)
