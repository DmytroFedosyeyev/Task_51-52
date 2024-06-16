
import os
import csv

class Cars:
    def __init__(self, manu, model, year, eng_capacity, color, price):
        self.manu = manu
        self.model = model
        self.year = year
        self.engine_capacity = eng_capacity
        self.color = color
        self.price = price


    def car_info(self):
        print(f'Manufacturer: {self.manu}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')
        print(f'Engine capacity: {self.eng_capacity}')
        print(f'Color: {self.color}')
        print(f'Price: {self.price}')


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

def list_cars():
    try:
        with open('cars.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Manufacturer', 'Model', 'Year', 'Engine capacity', 'Color', 'Price'])
            writer.writeheader()
            while True:
                manu = input('Enter manufacturer: ')
                model = input('Enter model: ')
                year = input('Enter year: ')
                eng_capacity = input('Enter engine capacity (l): ')
                color = input('Enter color: ')
                price = input('Enter price: ')

                writer.writerow({
                    'Manufacturer': manu,
                    'Year': year,
                    'Model': model,
                    'Engine capacity': eng_capacity,
                    'Color': color,
                    'Price': price
                })
                a = input('Do you want to add car? (y/n): ')
                if a.lower() != 'y':
                    break
    except Exception as e:
        print(f'Ошибка создания файла: {e}')