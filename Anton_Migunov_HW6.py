"""
1. Программа должна запрашивать у пользователя сумму в гривнах (uah), и тип валюты (usd/euro) для обмена.
Если валюта не из списка, печатаем ошибку.
Если все ок, печатаем сумму в запрашиваемой валюте по курсу.
"""
CURRENCY_RATES = {
                    "usd": 0.034,
                    "eur": 0.031
                 }


def validation_currency(user_input: str) -> bool:
    return user_input.lower() in CURRENCY_RATES.keys()


def validation_value(user_input: str) -> bool:
    if user_input.count(".") <= 1:
        if user_input.replace(".", "").isdigit():
            return True
    else:
        return False


def currency_converter(value: float, currency: str) -> float:
    return round(value * CURRENCY_RATES[currency], 2)


def main():
    uah_value = input("Enter UAH amount: ")
    currency_input = input(f"Enter currency {CURRENCY_RATES.keys()} to convert: ")
    print(validation_currency(currency_input), validation_value(uah_value))
    if validation_currency(currency_input) and validation_value(uah_value):
        print(f"{uah_value} UAH equals to {currency_converter(float(uah_value), currency_input)} {currency_input.upper()}")
    else:
        raise ValueError


# if __name__ == "__main__":
#     main()


"""
2. Написать функцию, которая на вход принимает число и возвращает сумму всех его цифр. 
Операцию повторять до тех пор, пока не останется одна цифра.
Например:
дано: 5349
5 + 3 + 4 + 9 = 21 2 + 1= 3
вывод: 3
"""


def calculate_digits_sum(num: str) -> int:
    if num.isdigit():
        result = 0
        for digit in num:
            result += int(digit)

        if len(str(result)) > 1:
            result = calculate_digits_sum(str(result))
        return result

    else:
        raise ValueError


# if __name__ == "__main__":
#     assert calculate_digits_sum("5349") == 3
#
#     number = input("Enter an integer positive number: ")
#     print(calculate_digits_sum(number))

"""
3. Написать функцию для сортировки для  списка словарей.
Сортировать по ключу `name`, если такого ключа нету в словаре, то по ключу `lastname`
Пример словаря - {'name': 'Ivan', 'lastname': 'Ivanov'}
"""


if __name__ == "__main__":
    profiles = [
                {"name": "Ivan", "lastname": "Ivanov"},
                {"name": "Anton", "lastname": "Migunov"},
                {"name": "Serhiy"},
                {"lastname": "Sokolov", "phone_number": "+380662589471"},
                {"name": "Anatoliy", "lastname": "Kuzmin"},
                {"lastname": "Sidorov"}
               ]
    print(sorted(profiles, key=lambda profile: profile.get("name") or profile.get("lastname")))
