from PIL import Image  #Подключим необходимые библиотеки.
image = Image.open("D:\\tumblr_lc4tpu4bkT1qztrv0o1_500.jpg") #Открываем изображение.
width = image.size[0] #Определяем ширину.
height = image.size[1] #Определяем высоту.
pix = image.load() #Выгружаем значения пикселей.
print (pix[0,0])

file = open("D:\\out.txt", "w")
file.write(str(width))
file.write(" ")
file.write(str(height))
file.write(" ")
for i in range(0, height):
    for i2 in range(0, width):
        a = pix[i2, i]
        file.write(str(a[0]) + " " + str(a[1]) + " " + str(a[2]) + " ")

file.close()
