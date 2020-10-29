import pygame as pg
import random as r
import time as t

pg.init()
screen = pg.display.set_mode((655,655))
pg.display.set_caption("15 Puzzle")

RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
WHITE = (255,255,255)
BROWN = (210,105, 30)
BLACK = (  0,  0,  0)

memory = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,0]]
font = pg.font.Font(None,100)
N00 = font.render("", True, (0,0,0),BLACK)
N01 = font.render("1", True, (0,0,0),BROWN)
N02 = font.render("2", True, (0,0,0),BROWN)
N03 = font.render("3", True, (0,0,0),BROWN)
N04 = font.render("4", True, (0,0,0),BROWN)
N05 = font.render("5", True, (0,0,0),BROWN)
N06 = font.render("6", True, (0,0,0),BROWN)
N07 = font.render("7", True, (0,0,0),BROWN)
N08 = font.render("8", True, (0,0,0),BROWN)
N09 = font.render("9", True, (0,0,0),BROWN)
N10 = font.render("10", True, (0,0,0),BROWN)
N11 = font.render("11", True, (0,0,0),BROWN)
N12 = font.render("12", True, (0,0,0),BROWN)
N13 = font.render("13", True, (0,0,0),BROWN)
N14 = font.render("14", True, (0,0,0),BROWN)
N15 = font.render("15", True, (0,0,0),BROWN)
N16 = font.render("16", True, (0,0,0),BROWN)
FontMemory = [[N01,N02,N03,N04],
              [N05,N06,N07,N08],
              [N09,N10,N11,N12],
              [N13,N14,N15,N00]]

#store zero position
Zeroi = 3
Zeroj = 3
for i in range(1000): #randomly generate map(can control easy or hard)
    Rint = r.randrange(4)
    if(Rint == 0): #up
        if(Zeroi != 3):
            memory[Zeroi][Zeroj],memory[Zeroi + 1][Zeroj] = memory[Zeroi + 1][Zeroj],memory[Zeroi][Zeroj]   
            FontMemory[Zeroi][Zeroj],FontMemory[Zeroi + 1][Zeroj] = FontMemory[Zeroi + 1][Zeroj],FontMemory[Zeroi][Zeroj]   
            Zeroi,Zeroj = Zeroi + 1,Zeroj
    elif(Rint == 1): #down
        if(Zeroi != 0):
            memory[Zeroi][Zeroj],memory[Zeroi - 1][Zeroj] = memory[Zeroi - 1][Zeroj],memory[Zeroi][Zeroj]   
            FontMemory[Zeroi][Zeroj],FontMemory[Zeroi - 1][Zeroj] = FontMemory[Zeroi - 1][Zeroj],FontMemory[Zeroi][Zeroj]   
            Zeroi,Zeroj = Zeroi - 1,Zeroj
    elif(Rint == 2): #left
        if(Zeroj != 3):
            memory[Zeroi][Zeroj],memory[Zeroi][Zeroj + 1] = memory[Zeroi][Zeroj + 1],memory[Zeroi][Zeroj]   
            FontMemory[Zeroi][Zeroj],FontMemory[Zeroi][Zeroj + 1] = FontMemory[Zeroi][Zeroj + 1],FontMemory[Zeroi][Zeroj] 
            Zeroi,Zeroj = Zeroi,Zeroj + 1
    else: #right
        if(Zeroj != 0):
            memory[Zeroi][Zeroj],memory[Zeroi][Zeroj - 1] = memory[Zeroi][Zeroj - 1],memory[Zeroi][Zeroj]   
            FontMemory[Zeroi][Zeroj],FontMemory[Zeroi][Zeroj - 1] = FontMemory[Zeroi][Zeroj - 1],FontMemory[Zeroi][Zeroj] 
            Zeroi,Zeroj = Zeroi,Zeroj - 1
Run = True
tSTART = t.time()
while Run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP: #up
                if(Zeroi != 3):
                    memory[Zeroi][Zeroj],memory[Zeroi + 1][Zeroj] = memory[Zeroi + 1][Zeroj],memory[Zeroi][Zeroj]   
                    FontMemory[Zeroi][Zeroj],FontMemory[Zeroi + 1][Zeroj] = FontMemory[Zeroi + 1][Zeroj],FontMemory[Zeroi][Zeroj]   
                    Zeroi,Zeroj = Zeroi + 1,Zeroj
            elif event.key == pg.K_DOWN: #down
                if(Zeroi != 0):
                    memory[Zeroi][Zeroj],memory[Zeroi - 1][Zeroj] = memory[Zeroi - 1][Zeroj],memory[Zeroi][Zeroj]   
                    FontMemory[Zeroi][Zeroj],FontMemory[Zeroi - 1][Zeroj] = FontMemory[Zeroi - 1][Zeroj],FontMemory[Zeroi][Zeroj]   
                    Zeroi,Zeroj = Zeroi - 1,Zeroj
            elif event.key == pg.K_LEFT: #left
                if(Zeroj != 3):
                    memory[Zeroi][Zeroj],memory[Zeroi][Zeroj + 1] = memory[Zeroi][Zeroj + 1],memory[Zeroi][Zeroj]   
                    FontMemory[Zeroi][Zeroj],FontMemory[Zeroi][Zeroj + 1] = FontMemory[Zeroi][Zeroj + 1],FontMemory[Zeroi][Zeroj] 
                    Zeroi,Zeroj = Zeroi,Zeroj + 1
            elif event.key == pg.K_RIGHT: #right
                if(Zeroj != 0):
                   memory[Zeroi][Zeroj],memory[Zeroi][Zeroj - 1] = memory[Zeroi][Zeroj - 1],memory[Zeroi][Zeroj]   
                   FontMemory[Zeroi][Zeroj],FontMemory[Zeroi][Zeroj - 1] = FontMemory[Zeroi][Zeroj - 1],FontMemory[Zeroi][Zeroj] 
                   Zeroi,Zeroj = Zeroi,Zeroj - 1
                   
    screen.fill(BLACK)
    
    #draw brown puzzle
    if memory[0][0] != 0:
        pg.draw.rect(screen,BROWN,(0,0,160,160))
    if memory[0][1] != 0:
        pg.draw.rect(screen,BROWN,(165,0,160,160))
    if memory[0][2] != 0:
        pg.draw.rect(screen,BROWN,(330,0,160,160))
    if memory[0][3] != 0:
        pg.draw.rect(screen,BROWN,(495,0,160,160))
    
    if memory[1][0] != 0:
        pg.draw.rect(screen,BROWN,(0,165,160,160))
    if memory[1][1] != 0:
        pg.draw.rect(screen,BROWN,(165,165,160,160))
    if memory[1][2] != 0:
        pg.draw.rect(screen,BROWN,(330,165,160,160))
    if memory[1][3] != 0:
        pg.draw.rect(screen,BROWN,(495,165,160,160))
    
    if memory[2][0] != 0:
        pg.draw.rect(screen,BROWN,(0,330,160,160))
    if memory[2][1] != 0:
        pg.draw.rect(screen,BROWN,(165,330,160,160))
    if memory[2][2] != 0:
        pg.draw.rect(screen,BROWN,(330,330,160,160))
    if memory[2][3] != 0:
        pg.draw.rect(screen,BROWN,(495,330,160,160))
        
    if memory[3][0] != 0:
        pg.draw.rect(screen,BROWN,(0,495,160,160))
    if memory[3][1] != 0:
        pg.draw.rect(screen,BROWN,(165,495,160,160))
    if memory[3][2] != 0:
        pg.draw.rect(screen,BROWN,(330,495,160,160))
    if memory[3][3] != 0:   
        pg.draw.rect(screen,BROWN,(495,495,160,160))
        
    #draw font + fine adjustment
    if(memory[0][0] >= 10):
        screen.blit(FontMemory[0][0],(40,50))
    else:
        screen.blit(FontMemory[0][0],(60,50))
    
    if(memory[0][1] >= 10):
        screen.blit(FontMemory[0][1],(205,50))
    else:
        screen.blit(FontMemory[0][1],(225,50))
        
    if(memory[0][2] >= 10):
        screen.blit(FontMemory[0][2],(370,50))
    else:
        screen.blit(FontMemory[0][2],(390,50))
        
    if(memory[0][3] >= 10):
        screen.blit(FontMemory[0][3],(535,50))
    else:
        screen.blit(FontMemory[0][3],(555,50))
    
    if(memory[1][0] >= 10):
        screen.blit(FontMemory[1][0],(40,215))
    else:
        screen.blit(FontMemory[1][0],(60,215))
    
    if(memory[1][1] >= 10):
        screen.blit(FontMemory[1][1],(205,215))
    else:
        screen.blit(FontMemory[1][1],(225,215))
    
    if(memory[1][2] >= 10):
        screen.blit(FontMemory[1][2],(370,215))
    else:
        screen.blit(FontMemory[1][2],(390,215))
    
    if(memory[1][3] >= 10):
        screen.blit(FontMemory[1][3],(535,215))
    else:
        screen.blit(FontMemory[1][3],(555,215))
    
    if(memory[2][0] >= 10):
        screen.blit(FontMemory[2][0],(40,380))
    else:
        screen.blit(FontMemory[2][0],(60,380))
    
    if(memory[2][1] >= 10):
        screen.blit(FontMemory[2][1],(205,380))
    else:
        screen.blit(FontMemory[2][1],(225,380))
    
    if(memory[2][2] >= 10):
        screen.blit(FontMemory[2][2],(370,380))
    else:
        screen.blit(FontMemory[2][2],(390,380))
    
    if(memory[2][3] >= 10):
        screen.blit(FontMemory[2][3],(535,380))
    else:
        screen.blit(FontMemory[2][3],(555,380))
    
    if(memory[3][0] >= 10):
        screen.blit(FontMemory[3][0],(40,545))
    else:
        screen.blit(FontMemory[3][0],(60,545))
    
    if(memory[3][1] >= 10):
        screen.blit(FontMemory[3][1],(205,545))
    else:
        screen.blit(FontMemory[3][1],(225,545))
    
    if(memory[3][2] >= 10):
        screen.blit(FontMemory[3][2],(370,545))
    else:
        screen.blit(FontMemory[3][2],(390,545))
    
    if(memory[3][3] >= 10):
        screen.blit(FontMemory[3][3],(535,545))
    else:
        screen.blit(FontMemory[3][3],(555,545))
        
    #Check whether win
    if(memory[0][0] == 1  and
       memory[0][1] == 2  and
       memory[0][2] == 3  and
       memory[0][3] == 4  and
       
       memory[1][0] == 5  and
       memory[1][1] == 6  and
       memory[1][2] == 7  and
       memory[1][3] == 8  and
       
       memory[2][0] == 9  and
       memory[2][1] == 10 and
       memory[2][2] == 11 and
       memory[2][3] == 12 and
       
       memory[3][0] == 13 and
       memory[3][1] == 14 and
       memory[3][2] == 15 and
       memory[3][3] == 0):
        pg.draw.rect(screen,BROWN,(495,495,160,160)) #draw 16
        screen.blit(N16,(535,545)) #draw 16
        Run = False
    pg.display.update()

pg.quit()
tEND = t.time()
print("You spend %.2f seconds" % (tEND - tSTART))