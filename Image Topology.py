from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np


image = Image.open('/Users/ag/Jupyter Projects/Image totology/gradient.jpg') # Загрузка фото и выгрузка информации
width = image.size[0]
height = image.size[1]
pix = image.load()

# Вытащим значения пикселей из pix
pixel_list = []     # Список для значений пикселей изображения
area = 0            # Длина области исследования

if width < height:
    area = height
elif width > height:
    area = width

for i in range(0, area):
    li = []
    for j in range(0, area):
        try:
            li.append(pix[i,j][0])
        except:
            li.append(0)
    pixel_list.append(li)
pix_ar = np.array(pixel_list)

# Создаем сетки координат
x = [i for i in range(0, area)]
y = [i for i in range(0, area)]
z = pix_ar

X, Y = np.meshgrid(x, y)


# Отрисовываем поверность
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, z, cmap='Spectral')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

print(z)
