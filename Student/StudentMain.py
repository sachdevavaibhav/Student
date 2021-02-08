from StudentFunc import *


def main_func():
    global user_input, path_to_file
    while True:
        try:
            user_input = int(input('PRESS 1 TO LOG DATA\nPRESS 2 TO RETRIEVE DATA: '))

            if user_input == 1:

                file = int(input('PRESS 1 TO OPEN EXISTING FILE\nPRESS 2 TO CREATE A NEW FILE: '))
                if file == 1:
                    path_to_file = input('Enter file path: ')
                    break
                elif file == 2:
                    path_to_file = input('Enter file path: ')
                    create_new_file(path_to_file)
                    break
                else:
                    raise ValueError

            elif user_input == 2:
                path_to_file = input('Enter file path: ')
                break

            else:
                raise ValueError

        except ValueError:
            print('PLEASE ENTER A VALID INPUT!')

    while True:
        try:

            if user_input == 1:

                roll_num = int(input('Enter roll number: '))
                name = input('Enter  name: ')
                stream_select = input('Enter C for Commerce\nS for Science\nA for Arts: ').upper()

                if stream_select == 'C':
                    stream = 'commerce'
                    personal_data(roll_num, name, stream)
                elif stream_select == 'S':
                    stream = 'science'
                    personal_data(roll_num, name, stream)
                elif stream_select == 'A':
                    stream = 'arts'
                    personal_data(roll_num, name, stream)
                else:
                    raise ValueError

                print('************ENTER YOUR MARKS BELOW ACCORDING TO THE SUBJECT CODE************')
                subject_marks()
                student.cal_percentage()
                student.cal_division()
                student.grade_gen()
                csv_write(path_to_file)
                exit_loop = int(input('PRESS 1 TO CONTINUE\nPRESS 2 TO EXIT: '))

                if exit_loop == 1:
                    continue
                elif exit_loop == 2:
                    break
                else:
                    raise ValueError

            elif user_input == 2:
                csv_read(path_to_file)
                exit_loop = int(input('PRESS 1 TO CONTINUE\nPRESS 2 TO EXIT: '))

                if exit_loop == 1:

                    user_input = int(input('PRESS 1 TO LOG DATA\nPRESS 2 TO RETRIEVE DATA: '))
                    if user_input == 1:

                        file = int(input('PRESS 1 TO OPEN EXISTING FILE\nPRESS 2 TO CREATE A NEW FILE: '))
                        if file == 1:
                            path_to_file = input('Enter file path: ')
                        elif file == 2:
                            path_to_file = input('Enter file path: ')
                            create_new_file(path_to_file)
                        else:
                            print('Invalid Input!\nRestart the program.')

                    elif user_input == 2:
                        path_to_file = input('Enter file path: ')

                elif exit_loop == 2:
                    break
                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print('PLEASE ENTER A VALID INPUT!')
            continue


if __name__ == '__main__':
    main_func()
