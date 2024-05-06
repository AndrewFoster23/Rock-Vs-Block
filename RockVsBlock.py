import pygame

size = width, height = 350, 700

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rock vs Block")
clock = pygame.time.Clock()


#Images
rock = pygame.image.load("rock.png")
rock = pygame.transform.scale(rock, (50, 30))


rockRect = rock.get_rect()
rockRect.center = (width // 2 - 25, height // 1.5)

font = pygame.font.SysFont("Arial", 50, bold = True)
font2 = pygame.font.SysFont("Arial", 25, bold = True)
boom = pygame.mixer.Sound("Vineboom.wav")

def drawText(text, x, y, color):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def drawRock(num):
    if num <= 0:
        screen.blit(rock, (rockXCoords[0], rockYCoords[0]))
    
    newNum = num
    if num > 12:
        newNum = 12
    for i in range(newNum):
        rock1 = rock
        rockRect1 = rock1.get_rect()
        rockRect1.center = rockRect.center
        
        #print(rockCoords[i])
        screen.blit(rock, (rockXCoords[i], rockYCoords[i]))

def drawSize(size, xPos):
    newXPos = xPos + 10
    newSize = size
    if size > 9:
        newXPos -= 6
    
    if size > 9 and xPos > 300:
        newXPos = 305
    
    elif xPos > 300:
        newXPos = 310
        
    if size < 0:
        newSize = 0
    img = font2.render("{}".format(newSize), True, (0, 0, 0))
    screen.blit(img, (newXPos + 10, height // 1.5 - 30))
    
def drawBlocks(yCoord):
    b1 = pygame.Rect(0, yCoord, 70, 70)
    b2 = pygame.Rect(70, yCoord, 70, 70)
    b3 = pygame.Rect(140, yCoord, 70, 70)
    b4 = pygame.Rect(210, yCoord, 70, 70)
    b5 = pygame.Rect(280, yCoord, 70, 70)
    
    pygame.draw.rect(screen, colors[0 + stageIndex], b1)
    pygame.draw.rect(screen, colors[1 + stageIndex], b2)
    pygame.draw.rect(screen, colors[2 + stageIndex], b3)
    pygame.draw.rect(screen, colors[3 + stageIndex], b4)
    pygame.draw.rect(screen, colors[4 + stageIndex], b5)
    
    if blockValues[0 + stageIndex] > 9:
        drawText("{}".format(blockValues[0 + stageIndex]), 0 + 12, yCoord + 6, (0, 0, 0))
    else:
        drawText("{}".format(blockValues[0 + stageIndex]), 0 + 22, yCoord + 6, (0, 0, 0))
        
    if blockValues[1 + stageIndex] > 9:
        drawText("{}".format(blockValues[1 + stageIndex]), 70 + 12, yCoord + 6, (0, 0, 0))
    else:
        drawText("{}".format(blockValues[1 + stageIndex]), 70 + 22, yCoord + 6, (0, 0, 0))
        
    if blockValues[2 + stageIndex] > 9:
        drawText("{}".format(blockValues[2 + stageIndex]), 140 + 12, yCoord + 6, (0, 0, 0))
    else:
        drawText("{}".format(blockValues[2 + stageIndex]), 140 + 22, yCoord + 6, (0, 0, 0))  
    
    if blockValues[3 + stageIndex] > 9:
        drawText("{}".format(blockValues[3 + stageIndex]), 210 + 12, yCoord + 6, (0, 0, 0))
    else:
        drawText("{}".format(blockValues[3 + stageIndex]), 210 + 22, yCoord + 6, (0, 0, 0))
        
    if blockValues[4 + stageIndex] > 9:
        drawText("{}".format(blockValues[4 + stageIndex]), 280 + 12, yCoord + 6, (0, 0, 0))
    else:
        drawText("{}".format(blockValues[4 + stageIndex]), 280 + 22, yCoord + 6, (0, 0, 0))
    
    
def drawBlocksAfter(yCoord, blockIndexNum):   
    b1 = pygame.Rect(0, yCoord, 70, 70)
    b2 = pygame.Rect(70, yCoord, 70, 70)
    b3 = pygame.Rect(140, yCoord, 70, 70)
    b4 = pygame.Rect(210, yCoord, 70, 70)
    b5 = pygame.Rect(280, yCoord, 70, 70)
    
    if blockIndexNum != 0:
        pygame.draw.rect(screen, colors[0 + stageIndex - 5], b1)
        if blockValues[0 + stageIndex - 5] > 9:
            drawText("{}".format(blockValues[0 + stageIndex - 5]), 0 + 12, yCoord + 6, (0, 0, 0))
        else:
            drawText("{}".format(blockValues[0 + stageIndex - 5]), 0 + 22, yCoord + 6, (0, 0, 0))
    
    if blockIndexNum != 1:
        pygame.draw.rect(screen, colors[1 + stageIndex - 5], b2)
        if blockValues[1 + stageIndex - 5] > 9:
            drawText("{}".format(blockValues[1 + stageIndex - 5]), 70 + 12, yCoord + 6, (0, 0, 0))
        else:
            drawText("{}".format(blockValues[1 + stageIndex - 5]), 70 + 22, yCoord + 6, (0, 0, 0))
    
    if blockIndexNum != 2:
        pygame.draw.rect(screen, colors[2 + stageIndex - 5], b3)
        if blockValues[2 + stageIndex - 5] > 9:
            drawText("{}".format(blockValues[2 + stageIndex - 5]), 140 + 12, yCoord + 6, (0, 0, 0))
        else:
            drawText("{}".format(blockValues[2 + stageIndex - 5]), 140 + 22, yCoord + 6, (0, 0, 0))
        
    if blockIndexNum != 3:
        pygame.draw.rect(screen, colors[3 + stageIndex - 5], b4)
        if blockValues[3 + stageIndex - 5] > 9:
            drawText("{}".format(blockValues[3 + stageIndex - 5]), 210 + 12, yCoord + 6, (0, 0, 0))
        else:
            drawText("{}".format(blockValues[3 + stageIndex - 5]), 210 + 22, yCoord + 6, (0, 0, 0))
    
    if blockIndexNum != 4:
        pygame.draw.rect(screen, colors[4 + stageIndex - 5], b5)
        if blockValues[4 + stageIndex - 5] > 9:
            drawText("{}".format(blockValues[4 + stageIndex - 5]), 280 + 12, yCoord + 6, (0, 0, 0))
        else:
            drawText("{}".format(blockValues[4 + stageIndex - 5]), 280 + 22, yCoord + 6, (0, 0, 0))
    
    
    
    
def findBlock(xCoord):
    if xCoord < 71 - 18:
        return 0
    elif xCoord < 141 - 18:
        return 1
    elif xCoord < 211 - 18:
        return 2
    elif xCoord < 281 - 18:
        return 3
    else:
        return 4
    


def checkWin(num):
    return False

def changeCoords(xPos):
    newXPos = xPos
    if xPos > 300:
        newXPos = 300
    
    rockXCoords[11] = rockXCoords[10]
    rockXCoords[10] = rockXCoords[9]
    rockXCoords[9] = rockXCoords[8]
    rockXCoords[8] = rockXCoords[7]
    rockXCoords[7] = rockXCoords[6]
    rockXCoords[6] = rockXCoords[5]
    rockXCoords[5] = rockXCoords[4]
    rockXCoords[4] = rockXCoords[3]
    rockXCoords[3] = rockXCoords[2]
    rockXCoords[2] = rockXCoords[1]
    rockXCoords[1] = rockXCoords[0]
    rockXCoords[0] = newXPos
    
def drawExtraRock(index, yCoord):
    screen.blit(rock, (extraRockX[index], yCoord + 110))
    img = font2.render("{}".format(extraRockNum[index]), True, (0, 0, 0))
    screen.blit(img, (extraRockX[index] + 20, yCoord + 80))   


    
    

#Colors
black = (0, 0, 0)
green = (0, 255, 0)
coolGreen = (26, 184, 68)
yellow = (255, 255, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
red = (255, 0, 0)
orange = (232, 137, 49)
lightBlue = (95, 222, 209)
darkBlue = (12, 81, 166)
darkGreen = (25, 110, 36)




colors = [orange, red, white, red, orange, 
          coolGreen, darkBlue, gray, darkBlue, coolGreen,
          orange, white, lightBlue, white, orange,
          lightBlue, coolGreen, red, coolGreen, lightBlue,
          yellow, gray, red, gray, yellow,
          darkGreen, orange, darkBlue, orange, darkGreen,
          red, lightBlue, coolGreen, lightBlue, red,
          red, lightBlue, coolGreen, lightBlue, red]

#Rock Positions
rockXCoords = [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]

rockYCoords = [height // 1.5, height // 1.5 + 20, height // 1.5 + 2*20, height // 1.5 + 3*20, height // 1.5 + 4*20, height // 1.5 + 5*20,
               height // 1.5 + 6*20, height // 1.5 + 7*20, height // 1.5 + 8*20, height // 1.5 + 9*20, height // 1.5 + 10*20, height // 1.5 + 11*20]

blockValues = [1, 2, 5, 1, 2,
               7, 3, 2, 5, 4, 
               10, 7, 12, 5, 4,
               5, 3, 5, 6, 7,
               8, 4, 9, 2, 13,
               5, 12, 6, 7, 8,
               12, 17, 14, 12, 25,
               12, 17, 14, 9, 25]

extraRockX = [148, 8, 8, 290, 148, 80, 218, 218]
extraRockNum = [2, 3, 2, 4, 7, 6, 5, 6]

aWin = 0

fps = 120

currLength = 3
points = 0
count = 1
blockCount = 1

boomCount = 1
longCount = [0, 0, 0, 0, 0, 0, 0]
longCountIndex = 0
blockIndexNum = 0
extraRockIndex = 0

stageIndex = 0
continueBlockIndexNum = 0

continuePls = False

run = True

# Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    
    key = pygame.key.get_pressed()
    boomCount += 1
    if key[pygame.K_SPACE] == True and boomCount > 15:
        boom.play()
        boomCount = 0
    
    screen.fill((26, 128, 217))
            
    count += 1
    mx,my=pygame.mouse.get_pos()
        
    if count % 3 == 0:
        changeCoords(mx)
        count = 0
    
    if longCountIndex != len(longCount):
        if extraRockNum[extraRockIndex] > 0 and longCount[longCountIndex] > 340:
            if mx > extraRockX[extraRockIndex] - 15 and mx < extraRockX[extraRockIndex] + 15:
                currLength += extraRockNum[extraRockIndex]
                extraRockNum[extraRockIndex] = 0
        
    if longCountIndex == len(longCount):
        aWin = 1
        continuePls = True
    
    elif longCount[longCountIndex] < height // 1.5 - 70:
        longCount[longCountIndex] += 1
            
    else:
        blockIndexNum += findBlock(mx)
        blockCount += 1
        #Loss check
        if currLength < 0:
            aWin = 2
                
        else:
            if blockValues[blockIndexNum] == 0:
                boom.play()
                longCountIndex += 1
                
                extraRockIndex += 1
                
                stageIndex += 5
                continueBlockIndexNum = blockIndexNum
                continuePls = True
            elif currLength == 0:
                aWin = 2
            else:    
                if blockCount % 10 == 0:
                    blockCount = 0   
                    
                    blockValues[blockIndexNum] -= 1
                    points += 1
                    currLength -= 1    
                     
                
        blockIndexNum = stageIndex
    #check to decrease currLength and block numbers if together win check section to update
    #Maybe check below
            
    if aWin != 1:
        if longCountIndex == len(longCount):
            drawBlocks(longCount[longCountIndex - 1])
            if extraRockNum[extraRockIndex - 1] > 0:
                drawExtraRock(extraRockIndex - 1, longCount[longCountIndex - 1])
        else:
            drawBlocks(longCount[longCountIndex])
            if extraRockNum[extraRockIndex] > 0:
                drawExtraRock(extraRockIndex, longCount[longCountIndex])
    else:
        continuePls = True
    
    #This works great!        
    if continuePls:
        longCount[longCountIndex - 1] += 1
        drawBlocksAfter(longCount[longCountIndex - 1], continueBlockIndexNum % 5)
        
        if extraRockNum[extraRockIndex - 1] > 0:
            drawExtraRock(extraRockIndex - 1, longCount[longCountIndex - 1])
            
        if longCount[longCountIndex - 1] == 800:
            continuePls = False
        
        
    drawSize(currLength, mx)
    drawRock(currLength)
        
    #blit extra rocks to increase length here (maybe, idk where the right spot is)
        
    drawText("{}".format(points), 15, 10, (0, 0, 0))
        
    if aWin == 1:
        drawText("You win!", width // 2 - 85, height // 2 - 50, (255, 0, 0))
    elif aWin == 2:
        drawText("You lose", width // 2 - 85, height // 2 - 50, (255, 0, 0))
               
    clock.tick(fps)
    pygame.display.flip()   
    
pygame.quit()
