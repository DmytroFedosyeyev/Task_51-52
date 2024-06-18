
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
        self.engine_capacity = new_capacity

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
            self.update_year('Enter new year: ')
        elif choice == '4':
            self.update_capacity('Enter new engine capacity: ')
        elif choice == '5':
            self.update_color('Enter new color: ')
        elif choice == '6':
            self.update_price('Enter new price: ')
        print('Data changed!')



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