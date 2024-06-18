# Завдання 1
# Реалізуйте клас «Автомобіль». Збережіть у класі: назву
# моделі, рік випуску, виробника, об’єм двигуна, колір машини,
# ціну. Реалізуйте методи класу для введення-виведення даних
# та інших операцій.
import os
import csv

class Cars:
    def __init__(self, manu, model, year, eng_capacity, color, price):
        self.manu = manu
        self.model = model
        self.year = year
        self.eng_capacity = eng_capacity
        self.color = color
        self.price = price


    def car_info(self):
        return {
            'Manufacturer': self.manu,
            'Model': self.model,
            'Year': self.year,
            'Engine capacity': self.eng_capacity,
            'Color': self.color,
            'Price': self.price
        }


    def update_manu(self, new_manu):
        self.manu = new_manu

    def update_model(self, new_model):
        self.model = new_model

    def update_year(self, new_yar):
        self.year = new_yar

    def update_capacity(self, new_capacity):
        self.eng_capacity = new_capacity

    def update_color(self, new_color):
        self.color = new_color

    def update_price(self, new_price):
        self.price = new_price



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
            self.update_manu(input('Enter new manufacturer: ').strip())
        elif choice == '2':
            self.update_model(input('Enter new model: ').strip())
        elif choice == '3':
            self.update_year(input('Enter new year: ').strip())
        elif choice == '4':
            self.update_capacity(input('Enter new engine capacity: ').strip())
        elif choice == '5':
            self.update_color(input('Enter new color: ').strip())
        elif choice == '6':
            self.update_price(input('Enter new price: ').strip())


def found_car():
    car_manufac = input('Enter manufacturer which car you want to edit: ').strip().lower()

    with open('cars.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        all_cars = list(reader)

    for j in all_cars:
        if j['Manufacturer'].strip().lower() == car_manufac:
                car = Cars(
                    j['Manufacturer'],
                    j['Model'],
                    j['Year'],
                    j['Engine capacity'],
                    j['Color'],
                    j['Price']
                )
                car.edit_car()
                j.

                with open('cars.csv', 'w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file,
                                            fieldnames=['Manufacturer', 'Model', 'Year', 'Engine capacity', 'Color',
                                                        'Price'])
                    writer.writeheader()
                    writer.writerows(all_cars)
                print('Data updated!')
                break
        else:
            print('Car not found')



def list_cars():
    try:
        file_exist = os.path.isfile('cars.csv')
        with open('cars.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Manufacturer', 'Model', 'Year', 'Engine capacity', 'Color', 'Price'])
            if not file_exist or os.path.getsize('cars.csv') == 0:
                writer.writeheader()
            while True:
                manu = input('Enter manufacturer: ')
                model = input('Enter model: ')
                year = input('Enter year: ')
                eng_capacity = input('Enter engine capacity (l): ')
                color = input('Enter color: ')
                price = input('Enter price: ')

                car = Cars(manu, model, year, eng_capacity, color, price)
                writer.writerow(car.car_info())

                a = input('Do you want to add car? (y/n): ')
                if a.lower() != 'y':
                    break
    except Exception as e:
        print(f'Ошибка создания файла: {e}')
#
# while True:
#     print("\n1. Add new car")
#     print("2. Edit car data")
#     print("3. Compare cars")
#     print("4. Save and exit")
#
#     choice = input('Enter your choice: ')
#
#     if choice == '1':
#         list_cars()
#     elif choice == '2':


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
        print(f"Название: {self.name}")
        print(f"Год издания: {self.year}")
        print(f"Издатель: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price}")

    def update_name(self, new_name):
        self.name = new_name

    def update_year(self, new_year):
        self.year = new_year

    def update_publisher(self, new_publisher):
        self.publisher = new_publisher

    def update_genre(self, new_genre):
        self.genre = new_genre

    def update_author(self, new_author):
        self.author = new_author

    def update_price(self, new_price):
        self.price = new_price

    def input_book_info(self):
        self.name = input("Введите название книги: ")
        self.year = input("Введите год издания: ")
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = input("Введите цену: ")

    def save_to_file(self, filename):
        with open('books.csv', 'a', encoding='utf-8') as file:
            file.write(f"{self.name},{self.year},{self.publisher},{self.genre},{self.author},{self.price}\n")