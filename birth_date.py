from datetime import datetime

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birth_date):
    today = datetime.now()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def print_digit_with_stars(digit):
    digit_patterns = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "    *", " *** ", "*    ", " *** "],
        '3': [" *** ", "    *", " *** ", "    *", " *** "],
        '4': ["*   *", "*   *", " *** ", "    *", "    *"],
        '5': [" *** ", "*    ", " *** ", "    *", " *** "],
        '6': [" *** ", "*    ", " *** ", "*   *", " *** "],
        '7': [" *** ", "    *", "   * ", "  *  ", " *   "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " *** ", "    *", " *** "],
        ' ': ["     ", "     ", "     ", "     ", "     "],
    }
    return digit_patterns.get(digit, ["     "] * 5)

def print_date_with_stars(date_str):
    lines = ["", "", "", "", ""]
    for char in date_str:
        digit_stars = print_digit_with_stars(char)
        for i in range(5):
            lines[i] += digit_stars[i] + "  "
    for line in lines:
        print(line)

def main():
    days_of_week = {
        "Monday": "Понедельник",
        "Tuesday": "Вторник",
        "Wednesday": "Среда",
        "Thursday": "Четверг",
        "Friday": "Пятница",
        "Saturday": "Суббота",
        "Sunday": "Воскресенье",
    }

    while True:
        birth_date_input = input("Введите дату рождения (в формате ДД.ММ.ГГГГ): ")
        try:
            birth_date = datetime.strptime(birth_date_input, "%d.%m.%Y")
            break
        except ValueError:
            print("Неверный формат даты. Пожалуйста, используйте формат ДД.ММ.ГГГГ.")

    day_of_week_english = birth_date.strftime("%A")
    day_of_week_russian = days_of_week[day_of_week_english]

    year = birth_date.year
    leap_year = is_leap_year(year)
    age = calculate_age(birth_date)

    print(f"Вы родились в {day_of_week_russian}.")
    print(f"{year} год {'был' if leap_year else 'не был'} високосным.")
    print(f"Сейчас вам {age} лет.")
    
    formatted_date = birth_date.strftime("%d %m %Y")
    print("Ваша дата рождения:")
    print_date_with_stars(formatted_date)

if __name__ == "__main__":
    main()
