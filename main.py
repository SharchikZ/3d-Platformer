from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform

app = Ursina()

ground = Entity(model = 'plane', texture= 'grass', collider = 'mesh', scale = (100, 1, 100))
goal = Entity(color = color.gold, model = 'cube', texture ='white_cube', position = (0, 11, 55), scale = (10, 1, 10), collider = 'box')
pillar = Entity(color.green, model = 'cube', position = (0, 36, 58), scale = (1, 50, 1))

blocks = []
direction = []
window.fullscreen = True

for i in range(10):
	r = uniform(-2, 2)
	block = Entity(model = 'cube', color = color.azure, texture = 'white_cube', position = (r, 1+i, 3+i*5), scale = (3, 0.5, 3), collider= 'box')
	if r < 0:
		direction.append(1)
	else:
		direction.append(-1)
	blocks.append(block)
def update():
	if player.y > 1:
		destroy(ground)

player = FirstPersonController()
Sky()
app.run()
