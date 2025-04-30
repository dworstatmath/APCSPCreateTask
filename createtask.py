import random
import math
import time
tracklength=150
frame=0
stop=["no","", "stop", "none"]
terrain=[".","-","'",",","*",".","-","'",",",":",":"]
llamacolors=["yellow", "red", "blue", "green"]
colorcodes={"yellow":"\033[1;33m","red":"\033[0;31m", "blue":"\033[0;34m","green":"\033[0;32m"}

def game(startingmoney):
    money=startingmoney
    def generatetrackterrain():
        for i in range(len(llamacolors)+2):
            row=[]
            for j in range(tracklength):
                row.append("\033[0m"+random.choice(terrain))
            row[tracklength-10]="\033[0m|"
            trackterrain.append(row)
    def runrace(betamount, betllama):
        frame=0
        def frameadd():
            for row in racetrack:
                string=""
                for x in row:
                    string+=x
                print(string)
        def trackrefresh():
            for llama in llamacolors:
                racetrack[llamacolors.index(llama)][math.floor(llamapos[llama])+3:math.floor(llamapos[llama])+6]=[colorcodes[llama]+"/",colorcodes[llama]+"^",colorcodes[llama]+">"]
                racetrack[llamacolors.index(llama)+1][math.floor(llamapos[llama]):math.floor(llamapos[llama])+5]=[colorcodes[llama]+",",colorcodes[llama]+"#",colorcodes[llama]+"#",colorcodes[llama]+"#",colorcodes[llama]+"/"]
                if (frame+math.floor(llamastride[llama]))%20<8:
                    racetrack[llamacolors.index(llama)+2][math.floor(llamapos[llama]):math.floor(llamapos[llama])+2]=[colorcodes[llama]+"/",colorcodes[llama]+"/"]
                    racetrack[llamacolors.index(llama)+2][math.floor(llamapos[llama])+3:math.floor(llamapos[llama])+5]=[colorcodes[llama]+"\\",colorcodes[llama]+"\\"]
                elif(frame+math.floor(llamastride[llama]))%20<10:
                    racetrack[llamacolors.index(llama)+2][math.floor(llamapos[llama])+1:math.floor(llamapos[llama])+5]=[colorcodes[llama]+"\\",colorcodes[llama]+"\\",colorcodes[llama]+"\\",colorcodes[llama]+"\\"]
                elif(frame+math.floor(llamastride[llama]))%20<18:
                    racetrack[llamacolors.index(llama)+2][math.floor(llamapos[llama])+1:math.floor(llamapos[llama])+4]=[colorcodes[llama]+"\\",colorcodes[llama]+"X",colorcodes[llama]+"/"]
                else:
                    racetrack[llamacolors.index(llama)+2][math.floor(llamapos[llama]):math.floor(llamapos[llama])+4]=[colorcodes[llama]+"/",colorcodes[llama]+"/",colorcodes[llama]+"/",colorcodes[llama]+"/"]
        winner=[]
        while len(winner)==0:
            time.sleep(0.05 )
            racetrack=[]
            for row in trackterrain:
                newrow=[]
                for item in row:
                    newrow.append(item)
                racetrack.append(newrow)
            trackrefresh()
            frame+=1
            print(frame/10)
            placement=[]
            for llama in llamacolors:
                placement.append(llamapos[llama])
            placement.sort()
            for i in range(len(placement)):
                print(colorcodes[list(llamapos.keys())[list(llamapos.values()).index(placement[len(placement)-1-i])]]+str(i+1)+". "+list(llamapos.keys())[list(llamapos.values()).index(placement[len(placement)-1-i])])

            frameadd()
            for llama in llamacolors:
                llamapos[llama]+=llamav[llama]
                llamav[llama]=(llamav[llama]+random.random()*0.1)/1.1
            for llama in llamacolors:
                if llamapos[llama]>tracklength-10:
                    winner.append(llama)
            if len(winner)>0:
                if len(winner)>1:
                    winnerdist=[]
                    for llama in winner:
                        winnerdist.append(llamapos[llama])
                    winnerdist=max(winnerdist)
                    for llama in winner:
                        if winnerdist==llamapos[llama]:
                            winner=[llama]
                print(winner[0]+" wins")
                if winner[0]==betllama:
                    win.append("this is an indication of a win")
            

    print("you have $"+str(money))
    betl=input("what llama do you want to bet on? (yellow, red, blue, or green)")
    if not(betl in stop):
        while not (betl in llamacolors):
            betl=input("please choose a llama from the list (yellow, red, blue, or green)")
            if betl in stop:
                break 
        if not(betl in stop):  
            betm=input("how much do you want to bet?")
            while not (betm.isdigit() and int(betm)<=money):
                betm=input("please write your bet as a whole number without units that you can pay")
            betm=int(betm)
    while not(betl in stop):
        llamapos={"yellow":0,"red":0, "blue":0,"green":0}
        llamav={"yellow":random.random()*0.5,"red":random.random()*0.5, "blue":random.random()*0.5,"green":random.random()*0.5}
        llamastride={"yellow":random.random()*20,"red":random.random()*20, "blue":random.random()*20,"green":random.random()*20}
        win=[]
        trackterrain=[]
        generatetrackterrain()
        runrace(betm,betl)
        if len(win)==0:
            money-=betm
        else:
            print("you won $"+str(betm*3))
            money+=betm*3
        print("you now have $"+ str(money))
        if money>0:
            betl=input("what llama do you want to bet on? (yellow, red, blue, or green)")
            if not(betl in stop):
                while not (betl in llamacolors):
                    betl=input("please choose a llama from the list (yellow, red, blue, or green)")
                    if betl in stop:
                        break 
                if betl in stop:
                    break 
                betm=input("how much do you want to bet?")
                while not (betm.isdigit() and int(betm)<=money):
                    betm=input("please write your bet as a whole number without units that you can pay")
                betm=int(betm)
        else:
            print("you lost all your money")
            break
    print("thanks for playing, you ended with $"+str(money))
game(100)