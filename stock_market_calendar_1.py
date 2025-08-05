import datetime
import json

def read_trading_holidays(file_name):
    try:
        with open(file_name, "r") as file:
            holidays = file.read().splitlines()
        holidays = [datetime.datetime.strptime(date, "%Y-%m-%d").date() for date in holidays]
        return set(holidays)
    except Exception as e:
        print(f"Error reading the holidays file: {e}")
        return set()

def create_stock_market_calendar(start_date, end_date, holidays):
    calendar = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() in (5, 6) or current_date in holidays:
            calendar.append({"date": current_date.strftime("%Y-%m-%d"), "is_working_day": 0})  # Weekend/Holiday
        else:
            calendar.append({"date": current_date.strftime("%Y-%m-%d"), "is_working_day": 1})  # Working day
        current_date += datetime.timedelta(days=1)
    return calendar

def save_to_json_file(data, file_name):
    try:
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Stock market calendar saved to {file_name}")
    except Exception as e:
        print(f"Error saving the JSON file: {e}")

def main():
    holidays_file = "trading_holidays.txt"
    json_output_file = "stock_market_calendar.json"
    
    trading_holidays = read_trading_holidays(holidays_file)
    
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 12, 31)
    
    stock_market_calendar = create_stock_market_calendar(start_date, end_date, trading_holidays)
    
    save_to_json_file(stock_market_calendar, json_output_file)

if __name__ == "__main__":
    main()
