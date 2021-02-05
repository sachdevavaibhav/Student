from Student import Student
import csv

student = Student()


def personal_data(roll_num, name, stream):
    student.roll_num = roll_num
    student.name = name
    student.stream = stream
    return None


def subject_marks():
    subject_code = {'Commerce':
                        {'01': 'English', '02': 'Accounts', '03': 'Mathematics', '04': 'Business Studies',
                         '05': 'Economics'},
                    'Science': {'01': 'English', '02': 'Physics', '03': 'Chemistry', '04': 'Mathematics',
                                '05': 'Computer Science'},
                    'Arts': {'01': 'English', '02': 'History', '03': 'Pol Science', '04': 'Mathematics',
                             '05': 'Geography'}
                    }
    if student.stream == 'commerce':
        print('subject codes are:', subject_code['Commerce'])
    elif student.stream == 'science':
        print('subject codes are:', subject_code['Science'])
    elif student.stream == 'arts':
        print('subject codes are:', subject_code['Arts'])

    subject1 = int(input('subject01: '))
    if subject1 < 0 or subject1 > 100:
        raise ValueError
    subject2 = int(input('subject02: '))
    if subject2 < 0 or subject2 > 100:
        raise ValueError
    subject3 = int(input('subject03: '))
    if subject3 < 0 or subject3 > 100:
        raise ValueError
    subject4 = int(input('subject04: '))
    if subject4 < 0 or subject4 > 100:
        raise ValueError
    subject5 = int(input('subject05: '))
    if subject5 < 0 or subject5 > 100:
        raise ValueError
    student.set_marks(subject1, subject2, subject3, subject4, subject5)


def create_new_file(file):
    print('********FILES WILL BE CREATED IN CSV FORMAT********')
    with open(f'{file}.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = ['ROLL NO.', 'NAME', 'STREAM', 'MARKS LIST', 'OBTAINED MARKS', 'PERCENTAGE', 'DIVISION', 'GRADE']
        csv_writer.writerow(header)
        print('File Created!')
    return None


def csv_write(file):
    with open(f'{file}.csv', mode='a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        details = [student.roll_num, student.name, student.stream, student.marks_list, student.obtained_marks,
                   student.percentage, student.division, student.grade]
        csv_writer.writerow(details)
    return None


def csv_read(file):
    try:
        with open(f'{file}.csv', mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',', quotechar='"')
            for row in csv_reader:
                print(row)
            return None
    except FileNotFoundError:
        print('FILE DOES NOT EXIST')
