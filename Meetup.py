import calendar

descriptorList = ['first', 'second', 'third', 'last', 'teenth']


def meetupDate(year, month, weekday, descriptor):
    dow = dict(zip(list(calendar.day_name), range(7)))

    c = calendar.Calendar()

    # Get all days with the correct month and weekday
    days = [d for d in c.itermonthdates(year, month) if d.weekday() == dow[weekday] and d.month == month]

    if descriptor == 'teenth':
        meetup = [d for d in days if d.day >= 13 and d.day <= 19][0]
    elif descriptor == 'first':
        meetup = days[0]
    elif descriptor == 'second':
        meetup = days[1]
    elif descriptor == 'third':
        meetup = days[2]
    elif descriptor == 'last':
        meetup = days[3]

    return meetup


def main():  # define main function

    meetup = "The Wednesteenth of June 2019"

    year = meetup[len(meetup) - 4:len(meetup)] # year

    try:
        year = int(year)
    except ValueError:
        raise Exception("There is no valid year in the meetup")

    for i in range(1, 13):
        if calendar.month_name[i] in meetup:
            month = calendar.month_name[i]
            break

    try:
        monthNumber = list(calendar.month_name).index(month) # month
    except UnboundLocalError:
        raise Exception("There is no valid month in the meetup")

    for j in range(0, 7):
        if calendar.day_abbr[j] in meetup:
            weekday = calendar.day_name[j] # day
            break

    try:
        weekday
    except NameError:
        raise Exception("There is no valid day in the meetup")

    for descrip in descriptorList:
        if descrip in meetup:
            descriptor = descrip # descriptor
            break

    try:
        descriptor
    except NameError:
        raise Exception("There is no valid descriptor in the meetup")

    print(meetupDate(year, monthNumber, weekday, descriptor))


if __name__ == '__main__':
    main()  # call main() function


