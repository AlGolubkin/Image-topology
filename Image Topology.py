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

if width > height:
    area = height
elif width < height:
    area = width

for i in range(0, area-1):
    li = []
    for j in range(0, area-1):
        li.append(pix[i,j][0])
    pixel_list.append(li)
pix_ar = np.array(pixel_list)


def f(x, y):
    a = [] # Лист для листов значений пикселей
    for i in range(len(x)):
        b = []
        for j in range(len(y)):
            b.append(pixel_list[i,j])
        a.append(b)
    return a

def l(a, b):    # Тестовая функция
    return np.sin(a) + np.cos(b)

x = [i for i in range(0, area-1)]
y = [i for i in range(0, area-1)]
z = pix_ar

X, Y = np.meshgrid(x, y)
#z = f(X,Y)



fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, z, cmap='Spectral')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

print(z)
