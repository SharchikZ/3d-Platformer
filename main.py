#Импортируем модуль ursina, random  и с ним камеру игрока от первого лица
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform
# Задаём значение app как Usina
app = Ursina()

# Создаем блоки для игры
ground = Entity(model = 'plane', texture= 'grass', collider = 'mesh', scale = (100, 1, 100))
goal = Entity(color = color.gold, model = 'cube', texture ='white_cube', position = (0, 11, 55), scale = (10, 1, 10), collider = 'box')
pillar = Entity(color.green, model = 'cube', position = (0, 36, 58), scale = (1, 50, 1))

# Все объекты игры
blocks = []
direction = []
# Открываем игру в полноэкранном режиме
window.fullscreen = True

# Задаём рандомное положение блоков
for i in range(10):
	r = uniform(-2, 2)
	block = Entity(model = 'cube', color = color.azure, texture = 'white_cube', position = (r, 1+i, 3+i*5), scale = (3, 0.5, 3), collider= 'box')
	if r < 0:
		direction.append(1)
	else:
		direction.append(-1)
	blocks.append(block)
# Если игрок прыгнет, тогда пол пропадёт :D
def update():
	if player.y > 1:
		destroy(ground)

player = FirstPersonController()
Sky()
app.run()
