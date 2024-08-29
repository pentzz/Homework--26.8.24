def int_days_to_str(day: int) -> str:
    '''
    :param day: number of day (1-7)

    :return: "Sunday" if day == 1
             "Monday" if day == 2
             "Tuesday" if day == 3
             "Wednesday" if day == 4
             "Thursday" if day == 5
             "Friday" if day == 6
             "Saturday" if day == 7
             "Invalid input" if day is not an int
             any other input (int) "Invalid day" (-1, 0, 100 ....)


    '''
    try:
        day = int(day)
    except ValueError:
        return "Invalid input"


    if day == 1:
        return "Sunday"
    elif day == 2:
        return "Monday"
    elif day == 3:
        return "Tuesday"
    elif day == 4:
        return "Wednesday"
    elif day == 5:
        return "Thursday"
    elif day == 6:
        return "Friday"
    elif day == 7:
        return "Saturday"
    else:
        return "Invalid day"


def get_day_of_week():
    try:
        while True:
            day_input = input(
                "Please enter a number between 1-7 to get string of the day, type 'exit' to quit: ")

            if day_input.lower() == 'exit':
                print("Bye Bye!")
                break
            try:
                day_number = int(day_input)
            except ValueError:
                print("Invalid input. must be an integer!")
                continue

            feedback = int_days_to_str(day_number)
            print(feedback)

    except Exception as ex:
        print(ex)
