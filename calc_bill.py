DAY_RATE_DEFAULT = 0.5123
NIGHT_RATE_DEFAULT = 0.2240
STANDING_CHARGE_DEFAULT = 0.3858
CALENDAR_DAYS = 30
CURRENCY = "\u00A3"

def run():
    day_rate = float(input(f"Enter day rate (in {CURRENCY}), default {DAY_RATE_DEFAULT}: ") or DAY_RATE_DEFAULT)
    night_rate = float(input(f"Enter night rate (in {CURRENCY}), default {NIGHT_RATE_DEFAULT}: ") or NIGHT_RATE_DEFAULT)
    standing_charge = float(input(f"Enter standing charge (in {CURRENCY}), default {STANDING_CHARGE_DEFAULT}: ") or STANDING_CHARGE_DEFAULT)

    print(f"You gave me {day_rate}, {night_rate}, {standing_charge}")

    most_recent_day_reading = float(input("Give me the most recent day reading: "))
    most_recent_night_reading = float(input("Give me the most recent night reading: "))

    previous_day_reading = float(input("Give me the previous day reading: "))
    previous_night_reading = float(input("Give me the previous night reading: "))

    diff_day = abs(most_recent_day_reading - previous_day_reading)
    diff_night = abs(most_recent_night_reading - previous_night_reading)

    print("Based on your information, you used:")
    print(f"{diff_day} Units in the day")
    print(f"{diff_night} Units in the night")

    print(f"Assuming {CALENDAR_DAYS} days of standing charge, your bill should be:")

    day_bill = diff_day * day_rate
    night_bill = diff_night * night_rate
    standing_bill = standing_charge * CALENDAR_DAYS

    print(f"Day: {CURRENCY}{day_bill}")
    print(f"Night: {CURRENCY}{night_bill}")
    print(f"Standing charge: {CURRENCY}{standing_bill}")

    total = day_bill + night_bill + standing_bill

    print(f"TOTAL: {CURRENCY}{total}")
    print("Thanks for playing. I do not take responsibility if this gives you a heart attack.")
    print("-------------------------")


if __name__ == '__main__':
    run()
