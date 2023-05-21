import pygame
import requests
from io import BytesIO

pygame.init()
screen = pygame.display.set_mode((440, 660))
link = "https://pbs.twimg.com/media/FupdQcSXwAsL0_A?format=png&name=900x900"
response = requests.get(link)
img = pygame.image.load(BytesIO(response.content))
img = pygame.transform.scale(img, (440, 660))  # <------

clock = pygame.time.Clock()

hoanh = []
tung = []

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            hoanh.append(event.pos[0])
            tung.append(event.pos[1])
            print(hoanh)
            print(tung)
            print(len(hoanh))
        elif event.type == pygame.QUIT:
            quit()
    screen.blit(img, (0, 0))
    pygame.display.update()
