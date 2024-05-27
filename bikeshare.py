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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york', 'washington']
    while True:
        city = input("Please enter a city in list cities below: \n Chicago, New York City, Washington\n").lower()
        if city in cities:
            break
        else:
            print('Please enter exactly city name in that list!')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    # check conditon validate month
    while True:
         month = input("Please enter a following month to get the data: \n January, February, March, April, May, June\n. If you do not want a month filter, then enter 'all'. \n").lower()
         if month in months:
            break
         else:
            print("Please just enter exactly a month from January to June or enter 'all'!")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while True:
          day = input("Please enter a day of the week: \nSunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n. If you do not want to a day filter, then enter 'all'. \n").lower()
          if day in days:
             break
          else:
             print("Please just enter exactly a day of week or enter 'all'!")

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
      # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all': 
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month: ", df['month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print("The most common day of week: ", df['day_of_week'].value_counts().idxmax())
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour: ", df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station: ", df ['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("The most commonly used end station: ", df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip: ")
    most_common_start_and_end_station = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 3600.0
    print("The total travel time in hours: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 3600.0
    print("The mean travel time in hours: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("Counts of user types: ", count_user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("\nCounts of gender: ", df['Gender'].value_counts())
    else:
        print("\nGender is not available")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("The earliest year of birth: ", int(df['Birth Year'].min()))
        print("\nThe most recent year of birth: ", int(df['Birth Year'].max()))
        print("\nThe most common year of birth: ", int(df['Birth Year'].mode()[0]))
    else:
        print("\nBirth Year is not available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_index = 0
    end_index = 5
    total_rows = len(df.index)
    
    while start_index < total_rows:
        user_input = input(f"Would you like to see the {'first' if start_index == 0 else 'next'} 5 rows of data? Enter 'yes' or 'no'.\n")
        if user_input.lower() == 'yes':
            print(f"\nDisplaying {'first' if start_index == 0 else 'next'} 5 rows of data.\n")
            if end_index > total_rows:
                end_index = total_rows
            print(df.iloc[start_index:end_index])
            start_index += 5
            end_index += 5
        else:
            break

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
