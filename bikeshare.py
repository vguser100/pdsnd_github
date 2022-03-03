import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITY_LIST = ['chicago','new york city','washington']
MONTHS_LIST = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS_OF_WEEK_LIST = ['monday', 'tuesday', 'wednesday', 'thusday', 'friday', 'saturday', 'sunday']

# Websites visited:
# moonbooks.org
# stackoverflow.com
# pandas.pydata.org
# datatofish.com
# pythonexamples.org

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    month = "all"
    day = "all"

    # User options:
    # 1. Would you like to see data for Chicago, New York, or Washington?
    # 2. Would you like to filter the data by month, day, or not at all?
    # 3. (If they chose month) Which month - January, February, March, April, May, or June?
    # 4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?
            
    while True:
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input("Enter the city name (Chicago, New York City, or Washington): ")
        city = city.lower()
        if city in CITY_LIST:
            break
            

    # Check to see if user would like to filter the data by month, day, or not at all?
    while True:
        filter_method = input("Would you like to filter the data by month, day, or not at all (none)? ")
        filter_method = filter_method.lower()
        if filter_method in ['month', 'day', 'none']:
            break

    # Check to see if user would like to filter by month or day   
    if filter_method != "none":
        if filter_method.lower() == "month":
            while True:
                # get user input for month (all, january, february, ... , june)
                month = input("Enter the month name (january, february, ... , june): ")
                month = month.lower()
                if month in MONTHS_LIST:
                    break

        elif filter_method.lower() == "day":
            while True:
                # get user input for day of week (all, monday, tuesday, ... sunday)
                day = input("Enter the day of week (monday, tuesday, ... sunday): ")
                day = day.lower()
                if day in DAYS_OF_WEEK_LIST:
                    break

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

    try:
        # load data file into a Pandas dataframe (df)
        df = pd.read_csv(CITY_DATA[city.lower()])

        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month and day_of_week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        # filter by month, if applicable
        if month != 'all':
            # use the index of the months list to get the corresponding month number
            month = MONTHS_LIST.index(month) + 1
  
            # filter by month to create the new dataframe
            df = df[df['month'] == month]

        # filter by day of week if applicable
        if day != 'all':
            # filter by day_of_week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]

        return df
    except Exception as e:
        print('\nError Loading Data\n')
        print(e)


def time_stats(df):
    try:
        """
        Displays statistics on the most frequent times of travel.
        Args:
            df - Pandas DataFrame containing city data filtered by month and day
        """

        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time']) 

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        #####################################
        # display the most common month
        ##################################### 

        # extract month from the Start Time column to create a month column
        df['month'] = df['Start Time'].dt.month

        # find the most common month
        common_month_val = df['month'].mode()[0]
        common_month_str = MONTHS_LIST[common_month_val - 1].title()
        print('Most Common Start Month:', common_month_str)

        #####################################
        # display the most common day of week
        #####################################    

        # extract day from the Start Time column to create a day column
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        # find the most common month
        common_day_of_week = df['day_of_week'].mode()[0]
        print('Most Common Start Day of Week:', common_day_of_week)    

        #####################################
        # display the most common start hour
        #####################################

        # extract hour from the Start Time column to create an hour column
        df['hour'] = df['Start Time'].dt.hour

        # find the most common hour
        common_hour = df['hour'].mode()[0]
        print('Most Common Start Hour:', common_hour)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
        print('\nError Calculating The Most Frequent Times of Travel...\n')
        print(e)


def station_stats(df):
    try:
        """
        Displays statistics on the most popular stations and trip.
        Args:
            df - Pandas DataFrame containing city data filtered by month and day
        """

        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        ##############################################
        # display most commonly used start station
        ##############################################
    
        # find the most common start station
        common_start_station = df['Start Station'].mode()[0]
        print('Most Common Start Station:', common_start_station)

        ##############################################
        # display most commonly used end station
        ############################################## 
    
        # find the most common end station
     
        common_end_station = df['End Station'].mode()[0]
        print('Most Common End Station:', common_end_station)

        #############################################################################
        # display most frequent combination of start station and end station trip
        #############################################################################

        df['start_end_station'] = df['Start Station'] + "/" + df['End Station']    
        common_start_end_station = df['start_end_station'].mode()[0]    
        print('Most Common Start/End Station:', common_start_end_station)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
        print('\nError Calculating The Most Popular Stations and Trip...\n')
        print(e)


def trip_duration_stats(df):
    try:
        """Displays statistics on the total and average trip duration.
           Args:
                df - Pandas DataFrame containing city data filtered by month and day
        """

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()
    
        ##########################################################
        # display total travel time
        ##########################################################    

        total_travel_time = df['Trip Duration'].sum()
        print('Total Travel Time:', total_travel_time) 
    
        ##########################################################
        # display mean travel time
        ##########################################################  
    
        mean_travel_time = df['Trip Duration'].mean()
        print('Mean Travel Time:', mean_travel_time)     

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
        print('\nError Calculating Trip Duration...\n')
        print(e)    


def user_stats(df):
    try:
        """Displays statistics on bikeshare users.
           Args:
                df - Pandas DataFrame containing city data filtered by month and day
        """

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print("Counts of User Types: ")
        print(user_types,"\n")

        # Display counts of gender
        if "Gender" in df:
            gender_types = df['Gender'].value_counts()
            print("Counts of Gender: ")
            print(gender_types, "\n")

        # Display earliest, most recent, and most common year of birth
        if "Birth Year" in df:
            print("Earliest Birth Year: ",df['Birth Year'].min())
            print("Most Recent Birth Year: ", df['Birth Year'].max())
            print("Most Common Birth Year: ", df['Birth Year'].mode()[0])    

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
        print('\nError Calculating User Stats...\n')
        print(e)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Save the original Pandas dataframe
        df_org = df.copy()
        df_org.pop('month')
        df_org.pop('day_of_week')

        if df.empty:
            print("No data found for selected city, month, and day. Please try again ",city, month, day)
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            
            # Set the width for later printing of raw data
            pd.options.display.width = 0

            # Allow the user to view the raw data
            index = df_org.index
            number_of_rows = len(index)
            for x in range(0, number_of_rows, 5):
                raw_data = input('\nWould you like to see 5 lines of the raw data (individual trip data)? Enter yes or no.\n')
                if raw_data.lower() in ['yes', 'y']:
                    print(df_org[x:x+5])
                else:
                    break    

        restart = input('\nWould you like to restart? Enter yes or no.\n')        
        if restart.lower() not in ['yes', 'y']:
           break


if __name__ == "__main__":
	main()
