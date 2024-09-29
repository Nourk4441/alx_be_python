from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Save the current date and time inside current_date variable
    current_date = datetime.datetime.now()

    # Format and print the current date and time in "YYYY-MM-DD HH:MM:SS" format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Prompt the user to enter the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    # Calculate the future date
    future_date = datetime.datetime.now() + datetime.timedelta(days=days_to_add)

    # Print the future date in "YYYY-MM-DD" format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future_date)

# Main function to run the script
def main():
    display_current_datetime()  # Part 1: Display current date and time
    calculate_future_date()     # Part 2: Calculate and display the future date

if __name__ == "__main__":
    main()
