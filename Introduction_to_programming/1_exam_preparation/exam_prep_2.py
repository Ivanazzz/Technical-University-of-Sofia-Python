# # Task 1
# # Напишете програма, в която потребителят въвежда n-брой цели числа от клавиатурата. Да се създатат два списъка - в
# # единия да се запишат всички нечетни числа, кратни на 3, а в другия всички четни, кратни на 2.
# # За списъка, съставен от нечетни числа, да се намери минималната и максималната стойност на елементите, съставящи 
# # списъка. За списъка, съставен от четни числа, да се намери сумата и средно аритметичната стойност за елементите от списъка.

 numbers_count = int(input())
 odd_numbers_list = []
 even_numbers_list = []

 for i in range(numbers_count):
     number = int(input())

     if (number % 2 != 0) and (number % 3 == 0):
         odd_numbers_list.append(number)
     elif number % 2 == 0:
         even_numbers_list.append(number)

 min_value = min(odd_numbers_list)
 max_value = max(odd_numbers_list)

 even_numbers_total_sum = 0
 count = 0

 for num in even_numbers_list:
     even_numbers_total_sum += num
     count += 1

 average_value = even_numbers_total_sum / count

 print(min_value)
 print(max_value)
 print(even_numbers_total_sum)
 print(average_value)



# Task 2
# Да се състави програма на Python, която дефинира клас "GSM mobile devices", с полета: налично количество, единична цена, 
# година на производство, производител, модел на мобилни устройства. Да се състави:
# - метод, който сортира моделите мобилни устройства по налично количество в нарастващ ред;
# - метод, който премества всички модели мобилни устройства, произедени от един и същи производител в списък, 
# записан в JSON файл.

class GSMMobileDevices:
    def __init__(self, quantity, price, year, producer, model):
        self.quantity = quantity
        self.price = price
        self.year = year
        self.producer = producer
        self.model = model
        
    
    def quantity_sort(self):
        quantity_list = []
        quantity_list = quantity_list.sort(key = lambda x: x.quantity)
        return quantity_list

    def convert_from_json():
        list_of_devices = list()
        json_object ='[{"availableQuantity" : 150,"price": 650,"year": 2021,"manifacturer": "Xiaomi","model": "MI 11 pro"}]'
 
        json_python = json.loads(json_object)
 
        for device in json_python:
 
            new_device = GSMMobileDevices(device["availableQuantity"], device["price"],device["year"], device["manifacturer"], device["model"] )
 
            list_of_devices.append(new_device)
        return list_of_devices


phone1 = GSMMobileDevices(2, 500, 2005, "Samsung", "A5")
phone2 = GSMMobileDevices(4, 900, 2008, "Samsung", "A8")
phone3 = GSMMobileDevices(3, 1200, 2007, "Apple", "IPhone 12")


