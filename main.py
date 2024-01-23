import openpyxl
book =openpyxl.open('ТАКСИ ЗАДАНИЕ 1.xlsx',read_only=True)
sheet = book.active
for row in range(1,17):
    driver = sheet[row][0].value
    car = sheet[row][1].value
    raiting = sheet[row][2].value
    category = sheet[row][3].value
    print (driver,car,raiting,category)
