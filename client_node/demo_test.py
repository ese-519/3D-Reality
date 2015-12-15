import pygame
import os
import cv2
from time import sleep
import sys
import numpy as np
n_img = 34
counter = 1
for i in range(1,33):
    print(i)
    img1 = cv2.imread('/home/sahabi/my_image'+str(i)+'.bmp')
    img2 = cv2.imread('/home/sahabi/my_image'+str(i+1)+'.bmp')
    both = np.hstack((img1,img2))
    cv2.imwrite('test/cam'+str(counter)+'.jpg',both)
    counter+=1
#    cv2.namedWindow("image");
#    cv2.imshow("image", both);
#    cv2.waitKey(30);

# rewrite the code to be easily scaled. 

def waitMotion():

    wait = 0
    while wait == 0:
        pygame.event.get()
        if pygame.mouse.get_pos()[0] - xloc > 60:
            wait = 1
    return

pic = []
picrect = []

pygame.init()
size = width, height = 700, 400
screen = pygame.display.set_mode(size)
imagestore = []

start = 1

for i in range(1,33):
    picture = pygame.image.load(os.path.join('test','cam'+str(start)+'.jpg')).convert_alpha()
    picture = pygame.transform.scale(picture, size)
    pic.append(picture)
    picrect.append(pic[i-1].get_rect())
    start += 1

speed = [0, 0]
black = 0, 0, 0
start = 1
update = 1
while 1:
    if (update==1500):
        pic = []
        picrect = []
        update = 0
        start = 1
        counter = 1
        print('concating..')
        for i in range(1,n_img-1):    
            img1 = cv2.imread('/home/sahabi/my_image'+str(i)+'.bmp')
            img2 = cv2.imread('/home/sahabi/my_image'+str(i+1)+'.bmp')
            both = np.hstack((img1,img2))
            cv2.imwrite('test/cam'+str(counter)+'.jpg',both)
            counter+=1
        print('updating..')
        for i in range(1,33):
            picture = pygame.image.load(os.path.join('test','cam'+str(start)+'.jpg')).convert_alpha()
            picture = pygame.transform.scale(picture, size)
            pic.append(picture)
            picrect.append(pic[i-1].get_rect())
            start += 1
        print('updated..')
    update += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    screen.blit(pic[0], picrect[0])
    pygame.display.flip()
    pygame.event.get()
    if pygame.mouse.get_pressed()[0]:
        pygame.event.get()
        xloc = pygame.mouse.get_pos()[0]
    while pygame.mouse.get_pressed()[0]:
        update += 1
        if (update==1500):
            pic = []
            picrect = []
            update = 0
            start = 1
            counter = 1
            print('concating..')
            for i in range(1,n_img-1):    
                img1 = cv2.imread('/home/sahabi/my_image'+str(i)+'.bmp')
                img2 = cv2.imread('/home/sahabi/my_image'+str(i+1)+'.bmp')
                both = np.hstack((img1,img2))
                cv2.imwrite('test/cam'+str(counter)+'.jpg',both)
                counter+=1
            print('updating..')
            for i in range(1,n_img-1):
                picture = pygame.image.load(os.path.join('test','cam'+str(start)+'.jpg')).convert_alpha()
                picture = pygame.transform.scale(picture, size)
                pic.append(picture)
                picrect.append(pic[i-1].get_rect())
                start += 1
            print('updated')        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        pygame.event.get()
        #print xloc - pygame.mouse.get_pos()[0]
        #sleep(0.01)
	index = (pygame.mouse.get_pos()[0] / -20)%(n_img-2)
        #print index
        pygame.event.get()
        screen.blit(pic[index], picrect[index])
        pygame.display.flip()
        pygame.event.get()
        #sleep(0.01)
