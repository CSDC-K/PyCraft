from pyexpat import model
from sre_constants import JUMP
from turtle import position
from ursina import *
from ursina.shaders import basic_lighting_shader
from ursina.prefabs.first_person_controller import FirstPersonController
import threading
import random
import time
from numpy import floor
from perlin_noise import PerlinNoise

ascii_banner = """

                                    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
                                    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
                                    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
                                    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
                                    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
                                     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                                                                                

"""

print(ascii_banner)
print("Connecting Api...")
time.sleep(2)
os.system("cls")

menu_ui = """
[=================================]
[         --PyCraft--         ]
[  Play Game: /play               ]
[                                 ]
[  1.10 Full News: New Jump Sound.]
[  New Hand Texture And Animation.]
[                                 ]
[=================================]
"""
print(menu_ui)

selection = input("Select -> ")




if selection == "/play" or selection == "/PLAY" or selection == "/Play":

    app = Ursina()
    #seed
    seed = random.randint(9999, 1881193819401945)
    noise = PerlinNoise(octaves=2, seed=seed)
    amp = 3
    freq = 12
    #seed
    window.title = "PyCraft"
    window.exit_button = True
    window.fullscreen = False
    window.vsync = True
    camera.fov = 90
    

    craft_music = Audio(
        "assest/sounds/music.mp3",
        loop = True,
        autoplay = True
    )


    #-------------------- Grass -------------------

    grass_one = Audio(
        "assest/sounds/grass_one.mp3",
        loop = False,
        autoplay= False

    )

    grass_two = Audio(
        "assest/sounds/grass_two.mp3",
        loop = False,
        autoplay= False

    )

    grass_three = Audio(
        "assest/sounds/grass_three.mp3",
        loop = False,
        autoplay= False

    )

    #-------------------- Grass -------------------

    #-------------------- Stone -------------------

    stone_one = Audio(
        "assest/sounds/stone_one.mp3",
        loop = False,
        autoplay = False
    )


    stone_two = Audio(
        "assest/sounds/stone_two.mp3",
        loop = False,
        autoplay = False
    )


    stone_three = Audio(
        "assest/sounds/stone_three.mp3",
        loop = False,
        autoplay = False
    )

    #-------------------- Stone -------------------

    plank_sound = Audio(
        "assest/sounds/plank.mp3",
        loop = False,
        autoplay= False
    )


    jump = Audio(
        "assest/sounds/jumping_one.mp3",
        loop = False,
        autoplay= False
    )


    #----------------- Zarilyum Sounds ---------------------

    zarilyum_one = Audio(
        "assest/sounds/zarilyum_one.mp3",
        loop = False,
        autoplay = False
    ) 


    zarilyum_two = Audio(
        "assest/sounds/zarilyum_two.mp3",
        loop = False,
        autoplay = False
    ) 



    zarilyum_three = Audio(
        "assest/sounds/zarilyum_three.mp3",
        loop = False,
        autoplay = False
    ) 



    zarilyum_four = Audio(
        "assest/sounds/zarilyum_four.mp3",
        loop = False,
        autoplay = False
    ) 


    #----------------- Zarilyum Sounds ---------------------


    iron = Audio(
        "assest/sounds/iron.mp3",
        loop = False,
        autoplay = False
    )

    


    ChosenBlock = 1

    menu_txt = Text(text="1: Grass\n2: Wood\n3: Stone Bricks\n4: Stone\n5: Zarilyum\n\nV 1.10 FULL",background = color.white , color=color.red, scale=0.8,x= -.87, y = .5)

    arm = Entity(
            parent = camera.ui,
            model = "cube",
            position = (0.75, -0.6),
            rotation = (150, -10, 6),
            scale = (0.2, 0.2, 0.9),
            texture = "assest/texture/arm"
    )

    test_menu = Entity(
        parent = camera.ui,
        model = "cube",
        position = (0.75, 0.6),
        scale = (0.2, 0.2, 0.9),
        texture = "assest/texture/menu"
    )



    def update():


        if held_keys["left mouse"] or held_keys["right mouse"]:
            
            arm.position = position = Vec2(0.4,-0.5)



        else:
            arm.position = Vec2(0.4,-0.6)


        if held_keys["q"] or held_keys["escape"]:
            exit()


        if held_keys["space"]:
            if not jump.playing:
                jump.play()

        
        if held_keys["c"]:
            EditorCamera()
        



        global ChosenBlock
        if held_keys["1"]:
            main_block(position = (0.75, -0.6), texture="assest/texture/grass.png")
            ChosenBlock = 1

        if held_keys["2"]:
            ChosenBlock = 2

        if held_keys["3"]:
            ChosenBlock = 3

        if held_keys["4"]:
            ChosenBlock = 4

        if held_keys["5"]:
            ChosenBlock = 5

        



    #main commands


    class main_block(Button):

        def __init__(self, position=(0,-10,0), texture = "assest/texture/grass"):
            super().__init__(
                parent = scene,
                position = position,
                model = "cube",
                texture = texture,
                color = color.white,
                origin_y = 0.5,
                highlight_color = color.white,
                shader = basic_lighting_shader
        )


        class Sky(Entity):
            def __init__(self):
                super().__init__(

                    parent = scene,
                    model = "sphere",
                    texture = "sky_sunset",
                    double_sided = True,
                    scale = 200


                )



        def input(self, key):
            if self.hovered:

                if key == "right mouse down":

                    if ChosenBlock == 1:

                            def play_sound():
                                
                                sound_selection = random.randint(1, 3)

                                if sound_selection == 1:
                                    grass_one.play()

                                if sound_selection == 2:
                                    grass_two.play()

                                if sound_selection == 3:
                                    grass_three.play()
                            
                            def add_grass():
                                grass_block_texture = "grass"
                                block = main_block(position = self.position + mouse.normal, texture=grass_block_texture)

                            t1 = threading.Thread(target=play_sound)
                            t2 = threading.Thread(target=add_grass)

                            t1.start()
                            t2.start()

                    if ChosenBlock == 2:

                            def play_sound():

                                plank_sound.play()
                            
                            def add_plank():
                                block = main_block(position = self.position + mouse.normal, texture="assest/texture/plank")
                            t1 = threading.Thread(target=play_sound)
                            t2 = threading.Thread(target=add_plank)

                            t1.start()
                            t2.start()
                #------------------------------------------------------------------------------------------------------------


                    if ChosenBlock == 3:

                            def play_sound():
                                sound_selection = random.randint(1, 3)

                                if sound_selection == 1:
                                    stone_one.play()

                                if sound_selection == 2:
                                    stone_two.play()

                                if sound_selection == 3:
                                    stone_three.play()
                            
                            def add_stone():
                                block = main_block(position = self.position + mouse.normal, texture="brick")

                            t1 = threading.Thread(target=play_sound)
                            t2 = threading.Thread(target=add_stone)

                            t1.start()
                            t2.start()

                    if ChosenBlock == 4:

                            def play_sound():
                                sound_selection = random.randint(1, 3)

                                if sound_selection == 1:
                                    stone_one.play()

                                if sound_selection == 2:
                                    stone_two.play()

                                if sound_selection == 3:
                                    stone_three.play()
                            

                            def add_stone():
                                block = main_block(position = self.position + mouse.normal, texture="assest/texture/stone")
                            t1 = threading.Thread(target=play_sound)
                            t2 = threading.Thread(target=add_stone)

                            t1.start()
                            t2.start()
                
                    if ChosenBlock == 5:

                        def play_sound():

                            sound_selection = random.randint(1, 4)

                            if sound_selection == 1:
                                zarilyum_one.play()

                            if sound_selection == 2:
                                zarilyum_two.play()
                                
                            
                            if sound_selection == 3:
                                zarilyum_three.play()

                            if sound_selection == 4:
                                zarilyum_four.play()


                        def add_zarilyum():
                            block = main_block(position = self.position + mouse.normal, texture = "assest/texture/zarilyum")

                        t1 = threading.Thread(target=play_sound)
                        t2 = threading.Thread(target=add_zarilyum)

                        t1.start()
                        t2.start()

                    
                    if ChosenBlock == 6:

                        def play_sound():
                            iron.play()

                        def add_iron():
                            block = main_block(position=self.position + mouse.normal, texture="assest/texture/iron")

                        t1 = threading.Thread(target=play_sound)
                        t2 = threading.Thread(target=add_iron)

                        t1.start()
                        t2.start()


                    if ChosenBlock == 6:

                        def play_sound():
                            ultimate_block.play()

                        def add_ultimate():
                            block = main_block(position=self.position + mouse.normal, texture="assest/texture/ultimate")

                        
                        t1 = threading.Thread(target=play_sound)
                        t2 = threading.Thread(target=add_iron)

                        t1.start()
                        t2.start()

                    

                if key == "left mouse down":
                    destroy(self)




    #high_grass = load_texture(name = "new_grass",path="resource/textures/grass_block.jpg")
    first_person_user = FirstPersonController(model="cube", texture="assest/texture/steve_head")
    first_person_user.mouse_sensitivity = Vec2(70, 70)

    first_person_user.gravity = 0.7
    first_person_user.speed = 10
    first_person_user.jump_height = 1
    first_person_user.jump_up_duration = 1
    first_person_user.fov = 90

    #menu_txt = Text(text="1: Grass\n2: Wood\n3: Stone Bricks\n4: Stone\n\nV 1.3 Beta", color=color.black, scale=1,x= -.88, y = .5)
    sky = Sky(texture="sky_sunset")

    for x in range(20):
        for y in range(20):
            z = math.floor(y * 7.5)
            z = .25 + floor(noise([y/25, x/25]))
            block = main_block(position=(x,z,y))

    app.run()
