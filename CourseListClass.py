import pickle

# from HelperFunctions import load_current_user


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
        # self.save_courselist()

    def add_course_to_courselist(self):
        print('\nCurrent Course:\n')
        for c in self.courses:
            print(c)
        x = str(input('\nWhich course would you like to add (example, CS4710)?\n'))
        self.courses.append(x)
        # self.save_courselist()

    # def save_courselist(self):
    #     user = load_current_user()
    #     filename = '/Users/mattcarter/Documents/UVA/Spring2021/pythonProject/CourseLists/' + self.name
    #     pickle_out = open(filename, 'wb')
    #     pickle.dump(self, pickle_out)
    #     pickle_out.close()

    def print_all_courses(self):
        for c in self.courses:
            print(c)
