#Import  library
from ursina import *
from ursina import collider
from ursina.prefabs.first_person_controller import *
from ursina.prefabs.first_person_controller import camera
from ursina.shaders import lit_with_shadows_shader
from ursina import curve

import time
#load window
app = Ursina()
#Baldski texture
BTexture = "Barski_text"
WallB = "WallTexture.jpg"
#Entity
map = Entity(model = 'maze.blend'
,texture = BTexture
, scale = 2
, collider = 'mesh'
, shader = lit_with_shadows_shader) #Set model

#Walls
wall = Entity(model = "cube"
, position = Vec3(1.39086, 0.752942, 23.2763)
, scale = (80,70,1)
, collider = "mesh"
, texture = WallB)
wall2 = Entity(model = "cube"
, position = Vec3(22.7444, 0.752942, 3.30865)
, scale = (80,70,1)
, collider = "mesh"
, rotation_y = 90
, texture = WallB)
wall3 = Entity(model = "cube"
, position = Vec3(-1.09923, 0, -21.8463)
, scale = (80,70,1)
, collider = "mesh"
, texture = WallB)
wall4 = Entity(model = "cube"
, position = Vec3(-22.9727, 0, 3.39197)
, scale = (80,70,1)
, collider = "mesh"
, rotation_y = 90
, texture = WallB)
wall5 = Entity(model = "cube"
, position = Vec3(2.38985, 30, -0.799802)
, scale = (80,70,1)
, collider = "mesh"
, rotation_x =90     
, texture =WallB)

#player
player = FirstPersonController(model = 'player',speed=30)
player.scale = 2
baldski_pos = player.position + (3,3,0) 

# other entities
amogus = Entity(model = "amogus.blend"
,texture =BTexture, scale = 4,collider = 'mesh', shader = lit_with_shadows_shader)

amogus.position = Vec3(2,5,0)
amogus.add_script(SmoothFollow(target = player, offset =[0,5,0], speed = 4))

def attack():
    pass

#Base
base = Entity(model = "base.blend"
, texture = "water.png", scale = 20,collider = 'mesh', shader = lit_with_shadows_shader)
baldski = Entity(model = "baldski.blend"
, texture = BTexture, scale = 1, shader = lit_with_shadows_shader)
baldski.position = (2,5,0)

#Weapon
basic_gun = "source/Pistol.fbx"
baldski_face = "baldski.blend"
weapon = Entity(parent = camera,model = basic_gun, scale = 0.05
,position = Vec3(2,-2,-0.5), rotation = Vec3(2,0,8), texture = "textures/PistolTexture.png")

weapon2 = Entity(model = basic_gun, scale = 0.05
,position = Vec3(2,5,0), rotation = Vec3(2,0,8), texture = "textures/PistolTexture.png")

#Weapon animations

#Environment
sky = Sky()


def update(): #upate function
    # print(player.position)
    # if player.y < -1: 
    # player.position = Vec3(0,3,0)
    if held_keys["2"]:
        weapon.model = baldski_face
        weapon.texture = BTexture
        weapon.position = Vec3(2,-0.25,2.5)
        weapon.rotation = rotation = Vec3(0,90,0)
        weapon.scale = 0.25
    elif held_keys["1"]:
        weapon.model = basic_gun
        weapon.texture = "textures/PistolTexture.png"
        weapon.position = Vec3(-0.5,-2,-1)
        weapon.rotation =Vec3(0,0,0)
        weapon.scale = 0.05

    elif held_keys["q"]:
        weapon.model = basic_gun
        weapon.texture = "textures/PistolTexture.png"
        weapon.position = Vec3(-0.5,-2,-1)
        weapon.rotation =Vec3(0,0,0)
        weapon.scale =  0.05

    elif held_keys["e"]:
        weapon.model = basic_gun
        weapon.texture = "textures/PistolTexture.png"
        weapon.position =Vec3(2,-2,-0.5)
        weapon.rotation =Vec3(2,0,8)
        weapon.scale =  0.05

#run window
app.run()
