'''        COLOR GUESS GAME(CGG) version 0.2
------------------------------------------------------
     Created by Justin J. De La Cruz
     Game where you have to write the color of the text
     and not the text written.

     version 0.2 changes:
          - Included Classes
          - New GUI design
---------------------------------------------------------
'''

from graphics import *
import random
import time
import threading

#    Global variables

colors = ['red','blue','green','pink','white','yellow','orange','purple']
timer = 30      #not in game
score = 0

win = GraphWin("Color Guess Game ver. 0.2",350,350)
win.setCoords(0,0,500,500)
win.setBackground("black")

scoreText = Text(Point(250.0,480.0),"Score: %s" %score)
scoreText.setFill("white")
scoreText.setSize(15)
scoreText.setStyle("bold")
scoreText.setFace("courier")
scoreText.draw(win)

#    Classes

class GUI:
     ''' It displays the games window using Zelle graphics.py '''
     def __init(self, win):
          self.win = win          

     def window(self):          
          rectange = Rectangle(Point(20.0,100.0),Point(480.0,460.00))          
          rectange.setOutline("red")
          #rectange.setFill("white")
          rectange.draw(win)

          back_Circle = Circle(Point(250.0,280.0),125)
          back_Circle.setFill("light gray")
          back_Circle.setOutline("gray")
          #back_Circle.draw(win)


          startText = Text(Point(250.0,275.0),"Start Game.")
          startText.setFill("white")
          startText.setFace("courier")
          startText.setSize(30)
          startText.draw(win)

          subtitle_Text = Text(Point(250.0,85.0),"Write the color, NOT THE TEXT!")
          subtitle_Text.setFill("white")
          subtitle_Text.setSize(13)
          subtitle_Text.setFace("courier")
          subtitle_Text.setStyle("bold")
          subtitle_Text.draw(win)

          while True:               
               win.getMouse()
               startText.undraw()
               break
          '''
          timeText = Text(Point(60.0,85.0), "Timer: %s" %timer)
          timeText.draw(win)
          '''
           
     def ballBounce(self):
          ball = Circle(Point(250.0,250.0), 50)
          ball.setOutline("light gray")
          ball.setFill(str(random.choice(colors)))
          ball.draw(win)

          dx = 1
          dy = 1

          while win.checkMouse():
               
               ball.move(dx,dy)
               

               if ball.getP1().getX() == 20.0 or ball.getP2().getX() == 480.0:

                    dx = -dx
                    ball.setFill(random.choice(colors))

               if ball.getP1().getY() == 100.0 or ball.getP2().getY() == 460.0:

                    dy = -dy
                    ball.setFill(random.choice(colors))
              
               update(100)               
         
class Game:
     ''' This class has the game's main functionality '''
     
     def __init__(self):
          pass     

     def entryBox(self):
          input = Entry(Point(250.0,50.0),25)
          input.setText('')
          input.setFill('white')
          input.draw(win)
          win.checkKey()

          while True:
               key = win.getKey()

               if key == "Return":
                    input_Color = str(input.getText().lower())
                    break
               
          return input_Color     

     def countdown():
          ''' Timer for game '''
          global timer

          for count in range(timer, 0, -1):
               timer -=1
               timer.sleep(1)

               if timer == 0:
                    print("TIMES UP!")
                    break

     def game_reset(self):
          global score
          global timer

          leaderboard_Text = Text(Point(250.0,280.0),"Play Again?...\n (yes or no)")
          leaderboard_Text.setFill("white")
          leaderboard_Text.setSize(16)
          leaderboard_Text.setFace("courier")
          leaderboard_Text.setStyle("bold")
          leaderboard_Text.draw(win)

          if (Game.entryBox(self) == 'yes'):
               leaderboard_Text.setText("Reseting...")
               print("Game reset...")
               score = 0
               timer = 30
               time.sleep(2)
               leaderboard_Text.setText("Starting...")
               print("Starting game...")
               time.sleep(2)
               leaderboard_Text.setText("")               

          else:
               exit()                 

     def leaderstats(self):
          ''' Stores player's name and score on leaderboard_CGG.txt'''          
          global score
          
          infile = open('leaderboard_CGG.txt','r')
          outline = open('leaderboard_CGG.txt','a')
     
          outline.write("\n")
          leaderboard_Text = Text(Point(250.0,280.0),"LeaderBoard:\n Enter your name.")
          leaderboard_Text.setFill("white")
          leaderboard_Text.setSize(16)
          leaderboard_Text.setFace("courier")
          leaderboard_Text.setStyle("bold")
          leaderboard_Text.draw(win)

          outline.write(Game.entryBox(self))
          
          outline.write(" ")
          outline.write(str(score))
          print("Player data stored...")

          leaderboard_Text.setText("Ok,\nStoring your score...")
          time.sleep(2)
          leaderboard_Text.setText("Done! name stored")
          time.sleep(2)
          leaderboard_Text.setText(" ")
     
          infile.close()
          outline.close()          
  
     def gameplay(self):
          ''' Game functionality '''
          global score

          entryBox = Game.entryBox

          while True:

               random_color = random.choice(colors)
               random_Fill = random.choice(colors)
               answer_color = random_Fill

               colorText = Text(Point(250.0,280.0), random_color)
               colorText.setFill(random_Fill)
               colorText.setSize(36)
               colorText.draw(win)

               if (entryBox(self) == answer_color):                    
                    score += 1
                    scoreText.setText("Score: " + str(score))
                    colorText.setText(random_color)
                    #print("Good answer") #Terminal answer

                    goodLabel = Text(Point(250.0,280.0), "Good Answer")
                    goodLabel.setSize(20)
                    goodLabel.setFill("white")
                    goodLabel.setFace("courier")
                    goodLabel.draw(win)

                    colorText.setText("")
                    time.sleep(0.5)
                    goodLabel.setText("")
                    
               else:
                    #print("Bad answer") #Terminal answer
                    badLabel = Text(Point(250.0,280.0),"Bad Answer:\n %s" %answer_color)
                    badLabel.setSize(20)
                    badLabel.setFill("white")
                    badLabel.setFace("courier")
                    badLabel.draw(win)

                    colorText.setText("")
                    time.sleep(2.5)
                    badLabel.setText("")

                    colorText.setText("")
               
                    gameover_Label = Text(Point(250.0,280.0),"GAME OVER")
                    gameover_Label.setSize(20)
                    gameover_Label.setFill("white")
                    gameover_Label.setStyle("bold")
                    gameover_Label.setFace("courier")
                    gameover_Label.draw(win)
                    print("GAME OVER...")
                    time.sleep(2)
                    gameover_Label.undraw()
                    break

     def gameStart(self):
          '''Include all functions from class Game and GUI'''
          
          while True:               
               gui = GUI()
               gui.window()
               game.gameplay()
               game.leaderstats()
               game.game_reset()         


if __name__ == "__main__":

    game = Game()
    game.gameStart()
