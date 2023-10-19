# Udacity_bike_project_file
Project: Explore US Bikeshare Data in Course: Introduction to Python

Bikeshare Data Analysis
This program analyzes bikeshare data for different cities. It provides various statistics and allows users to explore the raw data.

Prerequisites
To run this program, you need to have the following installed:
- Python 3.x
- pandas library

Getting Started
1. Clone or download the project repository to your local machine.
2. Open the terminal or command prompt and navigate to the project directory.

Usage
To run the program, follow these steps:
1. Make sure you are in the project directory in the terminal or command prompt.
2. Run the command python bikeshare.py to start the program.
3. The program will prompt you to specify the city, month, and day to analyze.
4. Enter the city name (either "chicago", "new york city", or "washington") and press Enter.
5. Enter the month name (either "all" or a specific month from January to December) and press Enter.
6. Enter the day name (either "all" or a specific day of the week) and press Enter.
7. The program will display the bikeshare data based on your input.
8. After displaying the statistics, the program will ask if you want to see the raw data of the chosen city.
9. If you choose to see the raw data, the program will display the first 5 rows of the dataframe. You can then choose to see the next 5 rows by pressing Enter. You can continue to see more rows until you decide to stop or reach the end of the dataframe.
10. To exit the program, choose not to restart when prompted or press Ctrl+C.

Functions
The code contains the following functions:

get_filters()
    This function asks the user to specify a city, month, and day to analyze. It returns the city, month, and day as strings.

load_data(city, month, day)
    This function loads the data for the specified city and filters it by month and day if applicable. It returns a Pandas DataFrame containing the filtered data.

time_stats(df)
    This function displays statistics on the most frequent times of travel. It calculates and prints the most common month, day of the week, and start hour based on the provided dataframe.

station_stats(df)
    This function displays statistics on the most popular stations and trip. It calculates and prints the most commonly used start station, end station, and the most frequent combination of start station and end station trip based on the provided dataframe.

trip_duration_stats(df)
    This function displays statistics on the total and average trip duration. It calculates and prints the total travel time, mean travel time, and median travel time based on the provided dataframe.

user_stats(df) - Displays statistics on bikeshare users.
    This function calculates and prints the following information:
    - Counts of user types
    - Counts of gender
    - The earliest, most recent, and most common year of birth
    - The mean and median birth year

show_raw_data(df) - Shows raw data of the chosen city.
    This function displays the first 5 rows of the dataframe. It then asks if you want to see the next 5 rows. You can continue to see more rows until you choose to stop or reach the end of the dataframe.

These are the main functions in the code that perform different analyses on the bikeshare data. You can call these functions after loading the data using the load_data() function.


Main Function
    The program includes a main() function that serves as the entry point of the program. It contains a loop that allows the program to run continuously until the user decides to exit. The main() function calls various other functions to perform different tasks.

Data Files
The program uses the following CSV data files for each city:
    chicago.csv
    new_york_city.csv
    washington.csv
Make sure these files are located in the appropriate directory as specified in the CITY_DATA dictionary in the code.

