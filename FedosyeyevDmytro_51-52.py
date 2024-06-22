# Ссылка на Git Hub: https://github.com/DmytroFedosyeyev/Task_51-52

# Завдання 1
# Реалізуйте клас «Автомобіль». Збережіть у класі: назву
# моделі, рік випуску, виробника, об’єм двигуна, колір машини,
# ціну. Реалізуйте методи класу для введення-виведення даних
# та інших операцій.

import os
import csv
from tabulate import tabulate

class Cars:
    def __init__(self, car_id, manu, model, year, eng_capacity, color, price):
        self.car_id = car_id
        self.manu = manu
        self.model = model
        self.year = year
        self.eng_capacity = eng_capacity
        self.color = color
        self.price = price


    def car_info(self):
        return {
            'ID': self.car_id,
            'Manufacturer': self.manu,
            'Model': self.model,
            'Year': self.year,
            'Engine capacity': self.eng_capacity,
            'Color': self.color,
            'Price': self.price
        }

    def edit_car(self):
        print('Car:')
        print(f'1. Manufacturer: {self.manu}')
        print(f'2. Model: {self.model}')
        print(f'3. Year: {self.year}')
        print(f'4. Engine capacity: {self.eng_capacity}')
        print(f'5. Color: {self.color}')
        print(f'6. Price: {self.price}')

        choice = input('Enter number what you want to edit: ')
        if choice == '1':
            self.manu = input('Enter new manufacturer: ').strip()
        elif choice == '2':
            self.model = input('Enter new model: ').strip()
        elif choice == '3':
            self.year = input('Enter new year: ').strip()
        elif choice == '4':
            self.capacity = input('Enter new engine capacity: ').strip()
        elif choice == '5':
            self.color = input('Enter new color: ').strip()
        elif choice == '6':
            self.price = input('Enter new price: ').strip()


def found_car():
    try:
        car_id = input('Enter ID which car you want to edit: ').strip()

        with open('cars.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            all_cars = list(reader)

        for i, j in enumerate(all_cars):
            if j['ID'].strip() == car_id:
                car = Cars(
                    j['ID'],
                    j['Manufacturer'],
                    j['Model'],
                    j['Year'],
                    j['Engine capacity'],
                    j['Color'],
                    j['Price']
                )
                car.edit_car()
                all_cars[i] = car.car_info()

                with open('cars.csv', 'w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file,
                                            fieldnames=['ID', 'Manufacturer', 'Model', 'Year', 'Engine capacity', 'Color',
                                                        'Price'])
                    writer.writeheader()
                    writer.writerows(all_cars)
                print('Data updated!')
                break
        else:
            print('Car not found')
    except FileNotFoundError:
        print('File cars.csv not found.')
    except Exception as e:
        print(f'Unexpected error: {e}')


def list_cars():
    try:
        file_exist = os.path.isfile('cars.csv')
        with open('cars.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ID', 'Manufacturer', 'Model', 'Year', 'Engine capacity', 'Color', 'Price'])
            if not file_exist or os.path.getsize('cars.csv') == 0:
                writer.writeheader()
            while True:
                card_id = input('Enter ID number: ')
                manu = input('Enter manufacturer: ')
                model = input('Enter model: ')
                year = input('Enter year: ')
                eng_capacity = input('Enter engine capacity (l): ')
                color = input('Enter color: ')
                price = input('Enter price: ')

                car = Cars(card_id, manu, model, year, eng_capacity, color, price)
                writer.writerow(car.car_info())

                a = input('Do you want to add car? (y/n): ')
                if a.lower() != 'y':
                    break
    except Exception as e:
        print(f'Mistake of creature file: {e}')


def compare_cars():
    try:
        with open('cars.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            all_cars = list(reader)

        found_cars = []
        car1 = input('Enter ID number of car 1: ').strip()
        car2 = input('Enter ID number of car 2: ').strip()
        for l in all_cars:
            if l['ID'] == car1 or l['ID'] == car2:
                found_cars.append(Cars(
                    l['ID'],
                    l['Manufacturer'],
                    l['Model'],
                    l['Year'],
                    l['Engine capacity'],
                    l['Color'],
                    l['Price']
                ))
        data_car = []
        for i in found_cars:
            data_car.append(i.car_info())

        headers = ['ID', 'Manufacturer', 'Model', 'Year', 'Engine capacity', 'Color', 'Price']
        print(tabulate(data_car, headers='keys', tablefmt='grid'))

    except FileNotFoundError:
        print('File cars.csv not found.')
    except Exception as e:
        print(f'Unexpected error: {e}')

while True:
    print("\n1. Add new car")
    print("2. Edit car data")
    print("3. Compare cars")
    print("4. Exit")

    choice = input('Enter your choice: ')

    if choice == '1':
        list_cars()
    elif choice == '2':
        found_car()
    elif choice == '3':
        compare_cars()
    elif choice == '4':
        break


# Завдання 2
# Реалізуйте клас «Книга». Збережіть у класі: назву книги,
# рік видання, видавця, жанр, автора, ціну. Реалізуйте методи
# класу для введення-виведення даних та інших операцій.

class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):
        print(f'The title: {self.name}')
        print(f'The year of publishing: {self.year}')
        print(f'The publisher: {self.publisher}')
        print(f'The genre: {self.genre}')
        print(f'The author: {self.author}')
        print(f'The price: {self.price}')

    def edit_book(self):
        print('Book:')
        print(f'1. Title: {self.name}')
        print(f'2. Year of publishing: {self.year}')
        print(f'3. Publisher: {self.publisher}')
        print(f'4. Genre: {self.genre}')
        print(f'5. Author: {self.author}')
        print(f'6. Price: {self.price}')

        choice = input('Enter number what you want to edit: ')
        if choice == '1':
            self.name = input('Enter new title of book: ').strip()
        elif choice == '2':
            self.year = input('Enter new year of publishing: ').strip()
        elif choice == '3':
            self.publisher = input('Enter new publisher: ').strip()
        elif choice == '4':
            self.genre = input('Enter new genre of book: ').strip()
        elif choice == '5':
            self.author = input('Enter new author: ').strip()
        elif choice == '6':
            self.price = input('Enter new price: ').strip()

    def input_book_info(self):
        self.name = input('Enter title of book: ')
        self.year = input('Enter year of publishing: ')
        self.publisher = input('Enter publisher: ')
        self.genre = input('Enter genre of book: ')
        self.author = input('Enter author: ')
        self.price = input('Enter price: ')

    def save_to_file(self, filename):
        with open('books.csv', 'a', encoding='utf-8') as file:
            file.write(f"{self.name},{self.year},{self.publisher},{self.genre},{self.author},{self.price}\n")


# Завдання 3
# Реалізуйте клас «Стадіон». Збережіть у класі: назву стаді-
# ону, дату відкриття, країну, місто, місткість. Реалізуйте методи
# класу для введення-виведення даних та інших операцій.

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):
        print(f'Name of the stadium: {self.name}')
        print(f'Opening date: {self.opening_date}')
        print(f'Country: {self.country}')
        print(f'City: {self.city}')
        print(f'Capacity: {self.capacity}')

    def edit_stadium(self):
        print('Stadium:')
        print(f'1. Name of the stadium: {self.name}')
        print(f'2. Opening date: {self.opening_date}')
        print(f'3. Country: {self.country}')
        print(f'4. City: {self.city}')
        print(f'5. Capacity: {self.capacity}')

        choice = input('Enter number what you want to edit: ')
        if choice == '1':
            self.name = input('Enter new name of the stadium: ').strip()
        elif choice == '2':
            self.opening_date = input('Enter new opening date: ').strip()
        elif choice == '3':
            self.country = input('Enter new country: ').strip()
        elif choice == '4':
            self.city = input('Enter new city: ').strip()
        elif choice == '5':
            self.capacity = input('Enter new capacity: ').strip()

    def get_info(self):
        return {
            'Name': self.name,
            'Opening data': self.opening_date,
            'Country': self.country,
            'City': self.city,
            'Capacity': self.capacity
        }

