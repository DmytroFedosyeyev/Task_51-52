
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

def edit_car():
    car_data = input('Enter manufacturer car which you want to edit: ').strip().lower()
    all_cars =[]
    with open('cars.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for i in reader:
            all_cars.append(i)
    found_car = False
    for j in all_cars:
        if j[0].strip().lower() == car_data:
            found_car = True
            print(f'Manufacturer: {j[0].capitalize()}')
            print(f' Model: {j[1].capitalize()}')
            print(f'Year: {j[2].capitalize()}')
            print(f'Engine capacity: {j[3].capitalize()}')
            print(f'Color {j[4].capitalize()}')
            print(f'Price: {j[5].capitalize()}')

            user_choice = input('Enter the number what you want to edit: ')
            if user_choice == '1':
                j[2] = input('Enter new year: ')
            elif user_choice == '2':
                j[3] = input('Enter new engine capacity: ')
            elif user_choice == '3':
                j[4] = input('Enter new color: ')
            elif user_choice == '4':
                j[5] = input('Enter new price: ')
    return print(all_cars)

edit_car()



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