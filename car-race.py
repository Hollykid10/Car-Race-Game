### My Car Race Code
import sys
import pygame
import random
import time
from pygame import mixer

# Clock
clock = pygame.time.Clock()


# Initialize pygame
pygame.init()

# Initialize Mixer
mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
sound = pygame.mixer.Sound("img_explosion2.wav")


# pygame.mixer.music.load("Nico Staf _ Fast and Run_320k.mp3")
# pygame.mixer.music.play()


# Create Screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))


# Caption and Icon
pygame.display.set_caption("Car Race")
icon = pygame.image.load("player_carsmwh.PNG")
pygame.display.set_icon(icon)


# Road
grass = pygame.transform.scale(pygame.image.load("grass.PNG"), (100, 600))
yellow_stripe = pygame.image.load("yellow_stripe.PNG")
white_stripe = pygame.transform.scale(pygame.image.load("white_stripe.PNG"), (5, 600))


# Road Function
def show_road():
    screen.blit(grass, (0, 0))
    screen.blit(grass, (700, 0))
    screen.blit(white_stripe, (100, 0))
    screen.blit(white_stripe, (700, 0))

# Car
car_img = pygame.image.load("player_carsmwh.PNG")
def show_car(x,y):
    screen.blit(car_img, (x, y))

# Enemy
def show_enemy(enemy_xcor, enemy_ycor, enemy):
    if enemy == 0:
        enemy_pic = pygame.image.load("enemy_car1smwh.PNG")
    elif enemy == 1:
        enemy_pic = pygame.image.load("enemy_car2smwh.PNG")
    elif enemy == 2:
        enemy_pic = pygame.image.load("enemy_car3smwh.PNG")
    elif enemy == 3:
        enemy_pic = pygame.image.load("enemy_car4smwh.PNG")
    elif enemy == 4:
        enemy_pic = pygame.image.load("enemy_car5smwh.PNG")
    elif enemy == 5:
        enemy_pic = pygame.image.load("enemy_car7smwh.png")
    screen.blit(enemy_pic, (enemy_xcor, enemy_ycor))


# Instruction
instruct_img = pygame.transform.scale(pygame.image.load("GM30jE.jpg.png"), (width, height))
def instruction():
    instruct = True
    while instruct:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(instruct_img, (0,0))
        instruct_text = pygame.font.SysFont(None, 70)
        instruct_text2 = pygame.font.SysFont(None, 30)
        instruct_text3 = pygame.font.SysFont(None, 50)


        instruct_render = instruct_text.render("INSTRUCTION", True, (0,0,0))
        screen.blit(instruct_render, (250, 100))

        instruct_render2 = instruct_text2.render("Car Game", True, (0, 0, 0))
        screen.blit(instruct_render2, (350, 180))

        instruct_render3 = instruct_text3.render("CONTROLS", True, (0, 0, 0))
        screen.blit(instruct_render3, (300, 230))


        pygame.draw.rect(screen, blue, (650, 400, 100, 50))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] > 650 and mouse[0] < 750 and mouse[1] > 400 and mouse[1] < 450:
            pygame.draw.rect(screen, light_blue, (650, 400, 100, 50))
            if click == (1,0,0):
                intro_loop()

        else:
            pygame.draw.rect(screen, blue, (650, 400, 100, 50))

        instruct_font = pygame.font.SysFont(None, 30)
        instruct_render4 = instruct_font.render("P : PAUSE", True, (0,0,0))
        instruct_render5 = instruct_font.render("ARROW-LEFT : LEFT-TURN", True, (0, 0, 0))
        instruct_render6 = instruct_font.render("ARROW-RIGHT : ARROW-TURN", True, (0, 0, 0))
        instruct_render7 = instruct_font.render("BACK", True, (0,0,0))


        screen.blit(instruct_render4, (50, 300))
        screen.blit(instruct_render5, (50, 350))
        screen.blit(instruct_render6, (50, 400))
        screen.blit(instruct_render7, (670, 415))

        pygame.display.update()

light_green = (0, 255, 0)
light_blue = (0, 0,255)
light_red = (255, 0,0)
green = (0,200, 0)
blue = (0,0,200)
red = (200, 0,0)

# Countdown
def countdown_background():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()

    x = 400
    y = 515
    screen.blit(grass, (0, 0))
    screen.blit(grass, (700, 0))
    screen.blit(white_stripe, (100, 0))
    screen.blit(white_stripe, (700, 0))
    screen.blit(yellow_stripe, (290, 10))
    screen.blit(yellow_stripe, (290, 90))
    screen.blit(yellow_stripe, (290, 180))
    screen.blit(yellow_stripe, (290, 270))
    screen.blit(yellow_stripe, (290, 360))
    screen.blit(yellow_stripe, (290, 450))
    screen.blit(yellow_stripe, (290, 540))
    screen.blit(yellow_stripe, (490, 10))
    screen.blit(yellow_stripe, (490, 90))
    screen.blit(yellow_stripe, (490, 180))
    screen.blit(yellow_stripe, (490, 270))
    screen.blit(yellow_stripe, (490, 360))
    screen.blit(yellow_stripe, (490, 450))
    screen.blit(yellow_stripe, (490, 540))
    screen.blit(car_img, (x,y))

    pygame.draw.rect(screen, (255, 100, 0), (0, 80, 100, 40))
    sl2_font = pygame.font.SysFont(None, 25)
    score1_render = sl2_font.render("score : 0", True, (255, 255, 255))
    level1_render = sl2_font.render("Level : 1", True, (255, 255, 255))
    screen.blit(score1_render, (0, 80))
    screen.blit(level1_render, (0, 100))

# CountDdown
def countdown():
    count = True
    while count:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.fill((119, 119, 119))
        countdown_background()
        count_font = pygame.font.SysFont(None, 115)
        count_render = count_font.render("3", True, (0,0,0))
        screen.blit(count_render, (380, 400))
        pygame.display.update()
        clock.tick(1)

        screen.fill((119, 119, 119))
        countdown_background()
        count_font = pygame.font.SysFont(None, 115)
        count_render = count_font.render("2", True, (0, 0, 0))
        screen.blit(count_render, (380, 400))
        pygame.display.update()
        clock.tick(1)

        screen.fill((119, 119, 119))
        countdown_background()
        count_font = pygame.font.SysFont(None, 115)
        count_render = count_font.render("1", True, (0, 0, 0))
        screen.blit(count_render, (380, 400))
        pygame.display.update()
        clock.tick(1)

        screen.fill((119, 119, 119))
        countdown_background()
        count_font = pygame.font.SysFont(None, 115)
        count_render = count_font.render("GO", True, (0, 0, 0))
        screen.blit(count_render, (380, 400))
        pygame.display.update()
        clock.tick(1)

        game_loop()
        quit()

# Game Intro
intro_img = pygame.transform.scale(pygame.image.load("toyota-supra-toyota-gazoo-racing-2018.jpeg"), (width, height))
def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(intro_img, (0,0))
        intro_text = pygame.font.SysFont(None, 100)
        intro_render = intro_text.render("CAR RACE", True, (0, 0, 0))
        screen.blit(intro_render, (200, 150))
        pygame.draw.rect(screen, green, (120, 500, 100, 50))
        pygame.draw.rect(screen, blue, (330, 500, 150, 50))
        pygame.draw.rect(screen, red, (600, 500, 100, 50))


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] > 120 and mouse[0] < 220 and mouse[1] > 500 and mouse[1] < 550:
            pygame.draw.rect (screen, light_green, (120, 500, 100, 50))
            if click == (1,0,0):
                countdown()
        else:
            pygame.draw.rect(screen, green, (120, 500, 100, 50))

        if mouse[0] > 330 and mouse[0] < 480 and mouse[1] > 500 and mouse[1] < 550:
             pygame.draw.rect (screen, light_blue, (330, 500, 150, 50))
             if click == (1,0,0):
                 instruction()

        else:
            pygame.draw.rect(screen, blue, (330, 500, 150, 50))

        if mouse[0] > 600 and mouse[0] < 700 and mouse[1] > 500 and mouse[1] < 550:
             pygame.draw.rect (screen, light_red, (600, 500, 100, 50))
             if click == (1,0,0):
                 pygame.quit()
                 quit()
        else:
            pygame.draw.rect(screen, red, (600, 500, 100, 50))

        start_font = pygame.font.SysFont(None, 30)
        start_render = start_font.render("START", True, (0, 0, 0))
        screen.blit(start_render, (135, 515))

        instruction_font = pygame.font.SysFont(None, 30)
        instruction_render = instruction_font.render("INSTRUCTION", True, (0,0,0))
        screen.blit(instruction_render, (336, 515))

        quit_font = pygame.font.SysFont(None, 30)
        quit_render = quit_font.render("QUIT", True, (0, 0, 0))
        screen.blit(quit_render, (615, 515))

        pygame.display.update()


# Pause
pause_img = pygame.transform.scale(pygame.image.load("gray-sport-car-racing-in-rain-wallpaper-800x600_17.jpg"), (width, height))
def paused():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(pause_img, (0,0))

        pygame.draw.rect(screen, green, (100, 400, 100, 50))
        pygame.draw.rect(screen, red, (320, 400, 150, 50))
        pygame.draw.rect(screen, blue, (600, 400, 100, 50))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] > 100 and mouse[0] < 200 and mouse[1] > 400 and mouse[1] < 450:
            pygame.draw.rect(screen, light_green, (100, 400, 100, 50))
            if click == (1,0,0):
                pause = False
        else:
            pygame.draw.rect(screen, green, (100, 400, 100, 50))

        if mouse[0] > 320 and mouse[0] < 470 and mouse[1] > 400 and mouse[1] < 450:
            pygame.draw.rect(screen, light_red, (320, 400, 150, 50))
            if click == (1,0,0):
                intro_loop()
        else:
            pygame.draw.rect(screen, red, (320, 400, 150, 50))
        if mouse[0] > 600 and mouse[0] < 700 and mouse[1] > 400 and mouse[1] < 450:
            pygame.draw.rect(screen, light_blue, (600, 400, 100, 50))
            if click == (1,0,0):
                game_loop()
                quit()
        else:
            pygame.draw.rect(screen, blue, (600, 400, 100, 50))


        pause_text = pygame.font.SysFont(None, 30)
        resume_render = pause_text.render("RESUME", True, (0,0,0))
        menu_render = pause_text.render("MAIN-MENU", True, (0,0,0))
        restart_render = pause_text.render("RESTART", True, (0,0,0))

        screen.blit(resume_render, (110, 415))
        screen.blit(menu_render, (335, 415))
        screen.blit(restart_render, (605, 415))
        pygame.display.update()


#Game Loop
def game_loop():

    car_xcor = 400
    car_ycor = 515
    car_xcor_movement = 0
    enemy_xcor = random.randrange(120, 680)
    enemy_ycor = 0
    enemy_ycor_movement = 8
    enemy = 0
    car_width = 35
    car_height = 82
    enemy_width = 36
    enemy_height = 79
    score = 0
    level = 1

    scroll_road = 540
    scroll_speed = 4
    scroll_road1 = 450
    scroll_road2 = 360
    scroll_road3 = 270
    scroll_road4 = 180
    scroll_road5 = 90
    scroll_road6 = 0
    scroll_road7 = 0 - 90


    running = True
    while running:

        screen.fill((119, 119, 119))

        screen.blit(yellow_stripe, (290, scroll_road))
        screen.blit(yellow_stripe, (290, scroll_road1))
        screen.blit(yellow_stripe, (290, scroll_road2))
        screen.blit(yellow_stripe, (290, scroll_road3))
        screen.blit(yellow_stripe, (290, scroll_road4))
        screen.blit(yellow_stripe, (290, scroll_road5))
        screen.blit(yellow_stripe, (290, scroll_road6))
        screen.blit(yellow_stripe, (290, scroll_road7))
        screen.blit(yellow_stripe, (490, scroll_road))
        screen.blit(yellow_stripe, (490, scroll_road1))
        screen.blit(yellow_stripe, (490, scroll_road2))
        screen.blit(yellow_stripe, (490, scroll_road3))
        screen.blit(yellow_stripe, (490, scroll_road4))
        screen.blit(yellow_stripe, (490, scroll_road5))
        screen.blit(yellow_stripe, (490, scroll_road6))
        screen.blit(yellow_stripe, (490, scroll_road7))

        scroll_road += scroll_speed
        scroll_road1 += scroll_speed
        scroll_road2 += scroll_speed
        scroll_road3 += scroll_speed
        scroll_road4 += scroll_speed
        scroll_road5 += scroll_speed
        scroll_road6 += scroll_speed
        scroll_road7 += scroll_speed

        if scroll_road >= 600:
            scroll_road = 600
        if scroll_road1 >= 540:
            scroll_road1 = 450
        if scroll_road2 >= 450:
            scroll_road2 = 360
        if scroll_road3 >= 360:
            scroll_road3 = 270
        if scroll_road4 >= 270:
            scroll_road4 = 180
        if scroll_road5 >= 180:
            scroll_road5 = 90
        if scroll_road6 >= 90:
            scroll_road6 = 0
        if scroll_road7 >= 0:
            scroll_road7 = 0 - 90



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Keybord Binding
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    car_xcor_movement += 10
                if event.key == pygame.K_LEFT:
                    car_xcor_movement -= 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    car_xcor_movement = 0


        car_xcor += car_xcor_movement
        enemy_ycor += enemy_ycor_movement

        show_road()
        show_enemy(enemy_xcor, enemy_ycor, enemy)
        show_car(car_xcor, car_ycor)

        pygame.draw.rect(screen, blue, (705, 0, 100, 30))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] > 705 and mouse[0] < 805 and mouse[1] > 0 and mouse[1] < 30:
            pygame.draw.rect(screen, light_blue, (705, 0, 100, 30))
            if click == (1, 0,0):
                paused()
        else:
            pygame.draw.rect(screen, blue, (705, 0, 100, 30))

        pause_text = pygame.font.SysFont(None, 30)
        pause_render = pause_text.render("PAUSE", True, (255, 255, 255))
        screen.blit(pause_render, (713, 3))

        # Enemy Movement
        if enemy_ycor > height:
            enemy_xcor = random.randrange(110,690-enemy_width)
            enemy_ycor = 0 - enemy_height
            enemy = random.randrange(0,5)
            score += 10


            if int(score) % 200==0:
                level += 1
                level_font = pygame.font.SysFont(None, 50)
                level_render = level_font.render("Level "+str(level), True, (255, 255, 255))
                screen.blit(level_render, (320, 300))
                pygame.display.update()
                time.sleep(2)
                enemy_ycor_movement += 2

        pygame.draw.rect(screen, (255, 100, 0), (0, 80, 100, 40))
        sl_font = pygame.font.SysFont(None, 25)
        score_render = sl_font.render("score : " + str(score), True, (255, 255, 255))
        level_render = sl_font.render("Level : "+ str(level), True, (255, 255, 255))
        screen.blit(score_render, (0, 80))
        screen.blit(level_render, (0, 100))
        pygame.display.update()


        # Player collision with border
        if car_xcor < 110 or car_xcor > 700-car_width:

            sound.play()
            border_font = pygame.font.SysFont(None, 50)
            border_render = border_font.render("border Accident!", True, (255, 255, 255))
            screen.blit(border_render, (300, 300))
            pygame.display.update()
            time.sleep(2)
            game_loop()
            quit()

        # Collision with enemy
        if car_ycor < enemy_ycor + enemy_height:
            if car_xcor > enemy_xcor or car_xcor + car_width > enemy_xcor:
                if car_xcor < enemy_xcor + enemy_width or  car_xcor + car_width < enemy_xcor+ enemy_width:

                    sound.play()
                    crash_font = pygame.font.SysFont(None, 50)
                    crash_render = crash_font.render("Car Crashed!", True, (255, 255, 255))
                    screen.blit(crash_render, (300, 300))
                    pygame.display.update()
                    time.sleep(2)

                    game_loop()
                    quit()



        pygame.display.update()
        clock.tick(100)


intro_loop()
game_loop()
pygame.quit()
quit()
