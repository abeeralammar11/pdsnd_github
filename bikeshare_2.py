import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        c = input(
            "\nwhat is the city you want to filter by ? pleace write one of 'New York City', 'Chicago', 'Washington'\n")
        if c.lower() not in ('new york city', 'chicago', 'washington'):
            print("please enter vaild city.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        m = input(
            "\nwhat is the month you want to filter by?,please write one of January, February, March, April, 'May', 'June', if you dont have a specific month please write 'all' \n")
        if m.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("please enter vaild month or write all.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        d = input(
            "\n if you have a specific day please write it Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday if you dont have please write 'all'.\n")
        if d.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("please enter vaild day.")
            continue
        else:
            break

    print('-' * 40)
    return c.lower(),m.lower(),d.lower()


def loadingdata(c, m, d):
    df = pd.read_csv(CITY_DATA[c])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['the month'] = df['Start Time'].dt.month
    df['the_day_of_the_week'] = df['Start Time'].dt.day_name()
    if m != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        m = months.index(m) + 1
        df = df[df['the month'] == m]
    if d != 'all':
        df = df[df['the_day_of_the_week'] == d.title()]

    return df


def time_stat(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['the month'].mode()[0]
    print(' the most popular month is:', common_month)

    # TO DO: display the most common day of week

    pd = df['the_day_of_the_week'].mode()[0]
    print('most popular day is:', pd)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    ph = df['hour'].mode()[0]
    print('the most popular hour is:', ph)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stat(df):
    print('\nCalculation of the most common trips & stations\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    ss = df['Start Station'].value_counts().idxmax()
    print('the most popular start station is:', ss)

    # TO DO: display most commonly used end station

    es = df['End Station'].value_counts().idxmax()
    print('\nthe most popular end station is :', es)

    # TO DO: display most frequent combination of start station and end station trip

    sc = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', ss, " and ", es)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_stat(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    ttt = sum(df['Trip Duration'])
    print('the total travel time is:',df['Trip Duration'].sum())

    # TO DO: display mean travel time

    mtt = df['Trip Duration'].mean()
    print('the mean travel time is:', mtt)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stat(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    ut = df['User Type'].value_counts()
    print(' the user types:\n', ut)

    # TO DO: Display counts of gender

    try:
        gt = df['Gender'].value_counts()
        print('\nthe gender types::\n', gt)
    except KeyError:
        print("\ngeder types : no reachable data for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        ey = df['Birth Year'].min()
        print('\nthe earliest year is:', ey)
    except KeyError:
        print("\nthe earliest year :no reachable data for this month.")

    try:
        mry = df['Birth Year'].max()
        print('\n the most recent year is:', mry)
    except KeyError:
        print("\n the most recent year : no reachable data for this month.")

    try:
        py = df['Birth Year'].value_counts().idxmax()
        print('\nthe popular year is  :', py)
    except KeyError:
        print("\npopular year : no reachable data for this month")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        c, m, d = get_filters()
        df = loadingdata(c,m,d) 
        trip_stat(df)
        user_stat(df)
        counter = 0
        while True:
            d = input('would tou like too see some data? yes or no?')
            if d.lower()!='yes':
                break
            else:
                print(df[counter:counter+5])
            counter=counter+5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
