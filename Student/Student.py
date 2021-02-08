"""
NAME - Vaibhav Sachdeva
Roll No. - 2038106
Semester - 1
Paper Name - Problem Solving Using Computers
"""


class Student:
    def __init__(self):
        print('This program only supports 5 subjects with maximum marks 100 in each subject.')
        self.roll_num = None
        self.name = None
        self.marks_list = None
        self.obtained_marks = None
        self.stream = None
        self.percentage = None
        self.grade = None
        self.division = None
        self.total_marks = 500

    def __str__(self):
        return str(self.__dict__)

    def details(self, roll_num, name, stream):
        try:
            self.roll_num = roll_num
            self.name = name
            stream = stream.lower()
            self.stream = stream
            return None
        except Exception:
            print('SOMETHING WENT WRONG!')

    def set_marks(self, sub1, sub2, sub3, sub4, sub5):
        try:
            marks_list = [sub1, sub2, sub3, sub4, sub5]
            self.marks_list = marks_list
            return None
        except Exception:
            print('SOMETHING WENT WRONG!')

    def cal_percentage(self):
        try:
            if self.marks_list is None:
                return 'Please call the method to set marks first.'
            marks = sum(self.marks_list)
            self.obtained_marks = marks
            percentage = (marks / self.total_marks) * 100
            self.percentage = percentage
            return None
        except Exception:
            print('SOMETHING WENT WRONG!')

    def cal_division(self):
        try:
            if self.percentage is None:
                return 'Please call the method to calculate percentage first.'
            if self.percentage >= 60:
                self.division = '1st Division'
            elif 50 <= self.percentage < 60:
                self.division = '2nd Division'
            elif 35 <= self.percentage < 50:
                self.division = '3rd Division'
            else:
                self.division = 'FAIL'
            return None
        except Exception:
            print('SOMETHING WENT WRONG!')

    def grade_gen(self):
        try:
            if self.marks_list is None:
                return 'Please call the method to set marks first.'
            sub_grade = {}
            grade = None
            for i in range(len(self.marks_list)):
                marks = self.marks_list[i]
                subject = 'sub0' + str(i + 1)
                if 90 <= marks <= 100:
                    grade = 'A'
                elif 80 <= marks < 90:
                    grade = 'B'
                elif 65 <= marks < 80:
                    grade = 'C'
                elif 40 <= marks < 65:
                    grade = 'D'
                elif marks < 40:
                    grade = 'E'

                sub_grade[subject] = grade
            self.grade = sub_grade
            return sub_grade
        except Exception:
            print('SOMETHING WENT WRONG!')

    def get_details(self):
        return self


if __name__ == '__main__':
    Vaibhav = Student()
    Vaibhav.details(2038106, 'Vaibhav', 'Science')
    Vaibhav.set_marks(95, 78, 55, 62, 99)
    Vaibhav.cal_percentage()
    print(Vaibhav.cal_division())
    Vaibhav.grade_gen()
    print(Vaibhav.get_details())
