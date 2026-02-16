import datetime
CURRENT_YEAR = datetime.date.today().year

def format_title(title: str) -> str:
    title = title.strip()
    title = title.capitalize()
    return title

def format_year(year: int) -> int:
    if year < 1500 or year > CURRENT_YEAR:
        print("Year is not in a valid range")
        year = CURRENT_YEAR
    return year

def validate_isbn(isbn: str) -> bool:
    num = 0
    mult = 10
    for i in isbn:
        num = num + (int(i) * mult)
        mult = mult - 1

    return num % 11 == 0