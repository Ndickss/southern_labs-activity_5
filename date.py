#Author: Ndivhuwo

def is_leap_year(year):
    """Returns True if leap year"""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100!= 0)

def get_day_of_the_week(month, day, year):
    month_codes = {1:1,2:4,3:4,4:0,5:2,6:5,7:0,8:3,9:6,10:1,11:4,12:6}
    yy = year % 100
    num_12s = yy // 12
    remainder = yy % 12
    num_4s = remainder // 4
    month_code = month_codes[month]

    offset = 0
    # Branching for leap Jan/Feb
    if month in (1, 2) and is_leap_year(year):
        offset += 6
    # Branching for century
    if 1600 <= year <= 1699:
        offset += 6
    elif 1700 <= year <= 1799:
        offset += 4
    elif 1800 <= year <= 1899:
        offset += 2
    elif 2000 <= year <= 2099:
        offset += 6
    elif 2100 <= year <= 2199:
        offset += 4

    total = num_12s + remainder + num_4s + day + month_code + offset
    dow = total % 7
    mapping = {0:"Saturday",1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday"}
    return mapping[dow]

def main():
    # --- Required tests ---
    print("--- Test Cases (must be True) ---")
    print("Sunday" == get_day_of_the_week(12, 25, 2022))
    print("Friday" == get_day_of_the_week(8, 26, 2022))
    print("Thursday" == get_day_of_the_week(10, 5, 1972))
    print("Wednesday" == get_day_of_the_week(2, 3, 2016))
    print("Monday" == get_day_of_the_week(12, 18, 1899))

    # --- CLI with While Loop ---
    print("\n--- CLI Day Finder (type 'q' to quit) ---")
    while True:
        try:
            user_input = input("\nEnter month day year (e.g., 12 25 2022) or q to quit: ")
            if user_input.lower() == 'q':
                print("Bye!")
                break

            parts = user_input.split()
            if len(parts)!= 3:
                print("Invalid format. Use: month day year")
                continue

            month, day, year = map(int, parts)

            # Branching validation
            if not (1 <= month <= 12):
                print("Month must be 1-12")
                continue
            if not (1 <= day <= 31):
                print("Day must be 1-31")
                continue

            result = get_day_of_the_week(month, day, year)
            leap = " (Leap Year)" if is_leap_year(year) else ""
            print(f"=> {month}/{day}/{year}{leap} is a {result}")

        except ValueError:
            print("Please enter numbers only")
        except KeyError:
            print("Invalid month")

if __name__ == "__main__":
    main()
