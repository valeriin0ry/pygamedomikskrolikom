import pygame
import sys 
import random 

#pygame.init() 
#lGreen = [153, 255, 153]
#lBlue = [153, 204, 255]
#ekraani_pind = pygame.display.set_mode( (640, 480) ) 
#ekraani_pind.fill( lGreen )
#pygame.display.set_caption("Esimene mäng")
#gameover = False 
#while not gameover:
#    youWin = pygame.image.load("win.png")
#    youWin = pygame.transform.scale(youWin, [300, 200])
#    ekraani_pind.blit(youWin,[180,100])
#    pygame.display.flip()
#    for i in pygame.event.get():
#        if i.type == pygame.QUIT:
#            sys.exit()
#pygame.quit() 




#pygame.init()
#r = random.randint(0, 255)
#g = random.randint(0, 255)
#b = random.randint(0, 255)
#varv = [r, g, b]
#lGreen = [153, 255, 153]
#pind = pygame.display.set_mode([640, 480])
#pygame.display.set_caption("Juhuslikud kujundid")
#pind.fill(lGreen)
#for i in range(1, 10):
#    x = random.randint(0, 620)
#    y = random.randint(0, 460)
#    pygame.draw.rect(pind, varv, [x, y, 20, 20])
#    pygame.display.flip()
#while True:
#    event = pygame.event.poll()
#    if event.type == pygame.QUIT:
#        break
#pygame.quit()



#pygame.init()
#red = [255, 0, 0]
#green = [0, 255, 0]
#blue = [0, 0, 255]
#pink = [255, 153, 255]
#lGreen = [153, 255, 153]
#pind = pygame.display.set_mode([640, 480])
#pygame.display.set_caption("Majake")
#pind.fill(lGreen)
#def drawHouse(x, y, width, height, screen, color):
#    points = [(x, y - (3 / 4.0) * height), (x, y), (x + width, y), (x + width, y - (3 / 4.0) * height), 
#              (x, y - (3 / 4.0) * height), (x + width / 2.0, y - height), (x + width, y - (3 / 4.0) * height)]
#    lineThickness = 3
#    pygame.draw.lines(screen, color, False, points, lineThickness)
#drawHouse(100, 400, 300, 400, pind, red)
#pygame.display.flip()


pygame.init()
sw = 640
sh = 480
bg = (144, 238, 144)  

#setka
#def draw_grid(screen, square_size, line_color):
#    rows = sh // square_size
#    cols = sw // square_size
#    for row in range(rows):
#        for col in range(cols):
#            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
#            pygame.draw.rect(screen, line_color, rect, 1)

#def igra():
#    screen = pygame.display.set_mode((sw, sh))
#    pygame.display.set_caption("Võrk")
#    square_size = 20
#    line_color = (255, 0, 0)  
#    running = True
#    while running:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                running = False
#        screen.fill(bg)
#        draw_grid(screen, square_size, line_color)
#        pygame.display.flip()
#    pygame.quit()
#    sys.exit()
#igra()

pygame.init()
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Кролик")
def draw_bunny(screen):
    center_x = window_size[0] // 2
    center_y = window_size[1] // 2
    ear_width = 30
    ear_height = 100
    ear1_rect = pygame.Rect(center_x - 40, center_y - 150, ear_width, ear_height)
    ear2_rect = pygame.Rect(center_x + 10, center_y - 150, ear_width, ear_height)
    pygame.draw.ellipse(screen, GRAY, ear1_rect)
    pygame.draw.ellipse(screen, GRAY, ear2_rect)
    head_radius = 50
    pygame.draw.circle(screen, GRAY, (center_x, center_y - 50), head_radius)
    body_rect = pygame.Rect(center_x - 50, center_y, 100, 200)
    pygame.draw.ellipse(screen, GRAY, body_rect)
    foot_width = 40
    foot_height = 20
    foot1_rect = pygame.Rect(center_x - 70, center_y + 180, foot_width, foot_height)
    foot2_rect = pygame.Rect(center_x + 30, center_y + 180, foot_width, foot_height)
    pygame.draw.ellipse(screen, GRAY, foot1_rect)
    pygame.draw.ellipse(screen, GRAY, foot2_rect)
def draw_house(screen):
    house_x = 50
    house_y = 300
    house_width = 150
    house_height = 100
    roof_height = 50
    house_rect = pygame.Rect(house_x, house_y, house_width, house_height)
    pygame.draw.rect(screen, BROWN, house_rect)
    roof_points = [(house_x, house_y), (house_x + house_width // 2, house_y - roof_height), (house_x + house_width, house_y)]
    pygame.draw.polygon(screen, RED, roof_points)
    door_width = 30
    door_height = 50
    door_x = house_x + house_width // 2 - door_width // 2
    door_y = house_y + house_height - door_height
    door_rect = pygame.Rect(door_x, door_y, door_width, door_height)
    pygame.draw.rect(screen, BLUE, door_rect)
    window_width = 30
    window_height = 30
    window1_x = house_x + 10
    window1_y = house_y + 20
    window2_x = house_x + house_width - 40
    window2_y = house_y + 20
    window1_rect = pygame.Rect(window1_x, window1_y, window_width, window_height)
    window2_rect = pygame.Rect(window2_x, window2_y, window_width, window_height)
    pygame.draw.rect(screen, WHITE, window1_rect)
    pygame.draw.rect(screen, WHITE, window2_rect)
    pygame.draw.line(screen, BLACK, (window1_x + window_width // 2, window1_y), (window1_x + window_width // 2, window1_y + window_height), 2)
    pygame.draw.line(screen, BLACK, (window1_x, window1_y + window_height // 2), (window1_x + window_width, window1_y + window_height // 2), 2)
    pygame.draw.line(screen, BLACK, (window2_x + window_width // 2, window2_y), (window2_x + window_width // 2, window2_y + window_height), 2)
    pygame.draw.line(screen, BLACK, (window2_x, window2_y + window_height // 2), (window2_x + window_width, window2_y + window_height // 2), 2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_bunny(screen)
    draw_house(screen)
    pygame.display.flip()
pygame.quit()
sys.exit()