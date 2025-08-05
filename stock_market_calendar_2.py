import datetime
import json

# Function to read trading holidays from a text file
def read_trading_holidays(file_name):
    try:
        with open(file_name, "r") as file:
            holidays = file.read().splitlines()
        # Parse holidays into datetime objects
        holidays = [datetime.datetime.strptime(date, "%Y-%m-%d").date() for date in holidays]
        return set(holidays)
    except Exception as e:
        print(f"Error reading the holidays file: {e}")
        return set()

# Function to create the stock market calendar
def create_stock_market_calendar(start_date, end_date, holidays):
    calendar = []
    current_date = start_date
    while current_date <= end_date:
        # Check if the current date is a weekend or a holiday
        if current_date.weekday() in (5, 6) or current_date in holidays:
            calendar.append({"date": current_date.strftime("%Y-%m-%d"), "is_working_day": 0})  # Weekend/Holiday
        else:
            calendar.append({"date": current_date.strftime("%Y-%m-%d"), "is_working_day": 1})  # Working day
        current_date += datetime.timedelta(days=1)
    return calendar

# Function to save the calendar to a JSON file
def save_to_json_file(data, file_name):
    try:
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Stock market calendar saved to {file_name}")
    except Exception as e:
        print(f"Error saving the JSON file: {e}")

# Main function
def main():
    holidays_file = "trading_holidays.txt"
    json_output_file = "stock_market_calendar.json"

    # Read trading holidays from the file
    trading_holidays = read_trading_holidays(holidays_file)

    # Set the date range for 2025
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 12, 31)

    # Generate the stock market calendar
    stock_market_calendar = create_stock_market_calendar(start_date, end_date, trading_holidays)

    # Save the stock market calendar to a JSON file
    save_to_json_file(stock_market_calendar, json_output_file)

# Run the main function
if __name__ == "__main__":
    main()
