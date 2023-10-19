import time
import pandas as pd
import statistics

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """ Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter"""
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city \n (type either chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("Which city should investigate? (Chicago, New York City or Washington): \n")).lower()
    # get user input for month \n (type either all, january, february, ... , june)
    month = str(input("Which month should investigate? (all, January, February ... or until December)): \n")).lower()
    # get user input for day of week \n (type either all, monday, tuesday, ... sunday)
    day = str(input("Which day should investigate? (all, Monday, Tuesday ... or until Sunday)): \n")).lower()    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """ Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day """
    filename = CITY_DATA[city]
    # load data file into a dataframe
    df = pd.read_csv(filename)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 
                  'july', 'august', 'september', 'october', 'november','december']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # capitalize the day parameter to match the title case used in the day_of_week column
        day = day.title()
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    timespans=['month', 'day', 'hour']

    for i in timespans:
        if i == 'month':
            # display the most common month
            # Create a dictionary mapping month numbers to month names
            month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
                           6: 'June', 7: 'July', 8: 'August', 9: 'September',
                           10: 'October', 11: 'November', 12: 'December'}
            df[i] = df['Start Time'].dt.month.map(month_names)
            
        # display the most common day of week
        elif i == 'day':
            df[i] = df['Start Time'].dt.day_name()
            
        # display the most common start hour
        elif i == 'hour':
            df[i] = df['Start Time'].dt.hour 

        popular_time = df[i].mode()[0]
        print(f"most common {i:>8} is {popular_time:>9}.")
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()
    stations=['Start Station', 'End Station']

    for i in stations:
        # display most commonly used start station
        # display most commonly used end station
        print('The most common ' + str(i).lower() + ' is: ' + df[i].mode()[0])

    # display most frequent combination of start station and end station trip
    combination_counts = df.groupby([stations[0], stations[1]]).size().reset_index(name='Count')
    most_frequent_combination = combination_counts[combination_counts['Count'] == combination_counts['Count'].max()]
    most_frequent_combination_string = most_frequent_combination[stations[0]] + ' -> ' + most_frequent_combination[stations[1]]
    print('\nmost frequent combination of start station and end station trip is:\n'
           + most_frequent_combination_string.values[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    traveltime = df['Trip Duration']

    # display total travel time
    # display mean travel time
    # display median travel time
    calcs = [sum, statistics.mean, statistics.median]

    for i in calcs:
        traveltime_calc = i(traveltime)
        print('The {:>7} travel time is: {:>9} sec'.format(i.__name__, int(traveltime_calc)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    users = ['User Type', 'Gender', 'Birth Year']

    for i in users:
        # Display counts of user types
        # Display counts of gender
        if i in df.columns and i != 'Birth Year':
            user = df[i]
            value_counts_user = user.value_counts()
            for index, value in value_counts_user.items():
                print('total no. of ' + str(index) + ' are ' + str(value))
        # Display earliest, most recent, and most common year of birth
        elif i in df.columns and i == 'Birth Year':
            # earliest year of birth
            print('The oldest users are born ', int(df[i].min()))
            # most recent year of birth
            print('The youngest users are born ',  int(df[i].max()))
            # most common year of birth
            print('The most common ' + str(i).lower() + ' is: ', int(df[i].mode()[0]))
            # mean birth year
            print('The mean ' + str(i).lower() + ' is: ', int(df[i].mean()))
            # median birth year
            print('The median ' + str(i).lower() + ' is: ', int(df[i].median()))
        # Displays if no column named 'Gender' or 'Birth year'
        else:
            print("there is no column called '"+ i + "' in the data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    '''shows the frst 5 Rows and followed the next each 5 rows after each query until interruption or end of dataframe'''
    start = 0
    user_input = str(input("Do you wnat to see the raw data of chosen city? Press enter! If not, type 'no' to go back to statistics query.")).lower()
    pd.set_option('display.max_columns', None)  # Set the option to display all columns
    while True:
        if user_input == "":
            print(df[start:start+5])
            start += 5
            user_input = str(input("Type 'stop' to break. Press Enter to continue...")).lower()
            if start > df.index[-1] or user_input == "stop":
                break
        else:
            break
    pd.set_option('display.max_columns', 0)

def main():
    while True:
        # catches any error
        while True:
            try:
                city, month, day = get_filters()
                df = load_data(city, month, day) 
                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df)
                show_raw_data(df)
                break
            except:
                print('An error occured. Type correctly!')
                cancel = input("if you want to cancel the program enter 'yes', else just enter for continuing:\n").lower()
                if cancel == 'yes':
                    exit()
                continue

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
exit()