import requests
import json

URL = 'https://www.cbr-xml-daily.ru/latest.js'
request = requests.get(URL)
request = request.text
data_dict = json.loads(request)
EXCHANGE_RATES = data_dict['rates']




def get_exchange_rates():  # Реализовать получение курсов по API
    return EXCHANGE_RATES


def main():
    exchange_rates = get_exchange_rates()
    base_currency = input(f'Введите валюту, которую хотите обменять {",".join(list(exchange_rates))}\n').strip().upper()
    if base_currency not in list(exchange_rates):
        return print('Данная валюта отсутствует')
    target_currency = input(f'Введите валюту, на которую хотите обменять {",".join(list(exchange_rates))}\n').strip().upper()
    if target_currency not in list(exchange_rates):
        return print('Данная валюта отсутствует')
    currency_amount = float(input('Введите количество валюты\n'))
    if currency_amount < 0:
        return print('Введено отрицательное значение!')

    cross_course = exchange_rates[base_currency] / exchange_rates[target_currency]
    result = round(cross_course * currency_amount, 2)
    print(result, target_currency)  # добавить валюту в вывод


main()







    # Исправить отображение списка валют
    # Проверять, действительную ли валюту ввел пользователь и отрицательные значения
    # Обрезать лишние пробелы при вводе, проверять регистр ввода

    # Исправить отображение списка валют
    # Проверять, действительную ли валюту ввел пользователь и отрицательные значения
    # Обрезать лишние пробелы при вводе, проверять регистр ввода


