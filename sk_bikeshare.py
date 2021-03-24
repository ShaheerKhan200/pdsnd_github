import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city ='error'
    month ='error'
    day ='error'

    while city == 'error' or month == 'error' or day == 'error':
        city = (input("Please provide a city (Chicago, New York City or Washington): ")).lower()
        city_list = ['chicago', 'Chicago', 'new york city', 'New York City','washington', 'Washington']
        if city not in city_list:
            city = 'error'
            print("please enter a valid entry")
            continue


# TO DO: get user input for month (all, january, february, ... , june)
        month = (input("Please provide a month in full for ex (All, January, February, March, April, May or June): ")).title()
        month_list = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
        if month not in month_list:
            month = 'error'
            print("please enter a valid entry")
            continue


# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = (input("Please provide a day of week single entry only (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday): ")).title()
        day_list = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if day not in day_list:
            day = 'error'
            print("please enter a valid entry")
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, hour day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name#day_name()

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month ]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is {}".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day of week is {}".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print("The most common start hour is {}".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used end station is {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station is {}".format((df['Start Station'] + df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is {}".format((df['Trip Duration']).sum()))

    # TO DO: display mean travel time
    print("The mean travel time is {}".format((df['Trip Duration']).mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types is \n{}".format((df['User Type']).value_counts()))

    # TO DO: Display counts of gender
    try:
        print("\nThe counts of gender is \n{}".format((df['Gender']).value_counts()))
    except:
        print("\nNo Data Is Available For Gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("\nThe earliest year of birth is {}\n".format(int((df['Birth Year']).min())))
        print("\nThe most recent year of birth is {}\n".format(int((df['Birth Year']).max())))
        print("\nThe most common year of birth is {}\n".format(int((df['Birth Year']).mode()[0])))
    except:
        print("\nNo Data Is Available For Birth Year")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    display_input = (input("Would you like to view 5 rows of individual trip data? Enter yes or no?: ")).lower()
    tracker = 5
    while display_input == 'yes':
        output = df.iloc[tracker-5:tracker]
        print(output)
        tracker +=5
        display_input = (input("Would you like to view 5 rows of individual trip data? Enter yes or no?: ")).lower()
    return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
