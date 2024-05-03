# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:50:30 2020

@author: ddilt
"""


import tkinter
import random

## Question 1
def initializeGame():
    global correctAnswer
    global timesWrong
    global totalTimesWrong
    operationDecider = random.randint(1,4)
    
    
    timesWrong = 0
    
    ## 1 = addition problem ###
    if operationDecider == 1:
        num1 = random.randint(1,1000)
        num2 = random.randint(1,1000)
        correctAnswer = num1 + num2
        gameWindow.title("{} + {} = ?".format(num1, num2))
        statusLabel.configure(text="You haven't made an answer yet")
        button1Check.configure(text="Check It!", command=checkAnswer)
    
    ## 2 = subtraction problem##
    if operationDecider == 2:
        num1 = random.randint(1,1000)
        num2 = random.randint(1, num1)
        correctAnswer = num1 - num2
        gameWindow.title("{} - {} = ?".format(num1, num2))
        statusLabel.configure(text="You haven't made an answer yet")
        button1Check.configure(text="Check It!", command=checkAnswer)
    
    ## 3 = multiplication problem##
    if operationDecider == 3:
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        correctAnswer = num1 * num2
        gameWindow.title("{} x {} = ?".format(num1, num2))
        statusLabel.configure(text="You haven't made an answer yet")
        button1Check.configure(text="Check It!", command=checkAnswer)
        
    ## 4 = division problem##
    if operationDecider == 4:
        num1 = random.randint(1,1000)  
        num2 = random.randint(1,1000)
        correctAnswer = num1/num2
      
        while correctAnswer is not type(int):
            if num1 % num2 == 0:
                break
            else:
                num2 = random.randint(1,num1)
                correctAnswer = num1/num2
            
        gameWindow.title("{} / {} = ?".format(num1, num2))
        statusLabel.configure(text="You haven't made an answer yet")
        button1Check.configure(text="Check It!", command=checkAnswer)
                
        
    
def checkAnswer():
    global correctAnswer
    global timesWrong
    global totalTimesWrong
    global totalSolved
    global problemsAttempted
    
    answerAsString = answerEntry.get()
    answer = int(answerAsString)
    
    
    if timesWrong == 0:
        problemsAttempted = problemsAttempted + 1
    
    if answer == correctAnswer:
        
        
        totalSolved = totalSolved + 1
        
        
        statusLabel.configure(text = str(answer) + " is correct!")
        button1Check.configure(text = "New Question", command = newQuestion)
##test ->   print(totalTimesWrong, totalSolved)    <- ########
        
    if answer != correctAnswer:
        timesWrong = timesWrong + 1   
        totalTimesWrong = totalTimesWrong + 1
        ##test ###print(totalTimesWrong)
        statusLabel.configure(text = str(answer) + " is incorrect, try again. You have been wrong {} time(s) on this question".format(timesWrong))
        
    answerEntry.delete(0, tkinter.END)
        
        

correctAnswer = None
gameWindow = None
button1Check = None
button2DiffQuestion = None
button3Quit = None
timesWrong = 0
totalTimesWrong = 0
totalSolved = 0
problemsAttempted = 0


    
        

def newQuestion():
    initializeGame()
    
def quitGame():
       
    if problemsAttempted > 0:
        averageWrong = totalTimesWrong / problemsAttempted 
        print('you attempted {} problems, and solved {}. Average amount of incorrect answers per problem is {}'.format(problemsAttempted,totalSolved, averageWrong))
        
    else:
        print("You didn't attempt any problems")
        
    gameWindow.destroy()
    
    


def initializeGameWindow():
    
    global gameWindow
    global answerEntry
    global button1Check
    global button2DiffQuestion
    global button3Quit
    global statusLabel
    
    gameWindow = tkinter.Tk()
    gameWindow.geometry('500x150')
    
    topFrame = tkinter.Frame(gameWindow)
    topFrame.pack()
    
    label1 = tkinter.Label(topFrame, text="Your Answer:")
    label1.pack(side=tkinter.LEFT)
    answerEntry = tkinter.Entry(topFrame)
    answerEntry.pack(side=tkinter.LEFT)
    button1Check = tkinter.Button(topFrame, text="Check It!", command=checkAnswer)
    button1Check.pack()
    button2DiffQuestion = tkinter.Button(topFrame, text="Want different question?", command=newQuestion)
    button2DiffQuestion.pack()
    button3Quit = tkinter.Button(topFrame, text="Quit?", command=quitGame)
    button3Quit.pack()
    
    statusLabel = tkinter.Label(gameWindow, text="You haven't made any guesses yet")
    statusLabel.pack()
    
    

def startGameGUI():
    global correctAnswer
    global totalTimesWrong
    global totalSolved
    global problemsAttempted
    
    totalTimesWrong = 0
    totalSolved = 0
    problemsAttempted = 0
    initializeGameWindow()
    initializeGame()
    gameWindow.mainloop()




    

    
    
    