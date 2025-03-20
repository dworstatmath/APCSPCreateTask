import random
import math
import time
tracklength=150
frame=0
terrain=[".","-","'",",","*",".","-","'",",",":",":"]
trackterrain=[]
racetrack=[[],]
llamacolors=["yellow", "red", "blue", "green"]
colorcodes={"yellow":"\033[1;33m","red":"\033[0;31m", "blue":"\033[0;34m","green":"\033[0;32m"}
llamapos={"yellow":0,"red":0, "blue":0,"green":0}
llamav={"yellow":random.random()*0.5,"red":random.random()*0.5, "blue":random.random()*0.5,"green":random.random()*0.5}
money="$100"
print("   /^>")
print(",###/")
print("// \\\\")
def generatetrackterrain():
    for i in range(len(llamacolors)+2):
        row=[]
        for j in range(tracklength):
            row.append("\033[0m"+random.choice(terrain))
        trackterrain.append(row)
def trackrefresh():
    for llama in llamacolors:
        racetrack[llamacolors.index(llama)][math.floor(llamapos[llama])+3:math.floor(llamapos[llama])+6]=[colorcodes[llama]+"/",colorcodes[llama]+"^",colorcodes[llama]+">"]
        racetrack[llamacolors.index(llama)+1][math.floor(llamapos[llama]):math.floor(llamapos[llama])+5]=[colorcodes[llama]+",",colorcodes[llama]+"#",colorcodes[llama]+"#",colorcodes[llama]+"#",colorcodes[llama]+"/"]
        if frame%20<10:
            racetrack[llamacolors.index(llama)+2][math.floor(llamapos[llama]):math.floor(llamapos[llama])+2]=[colorcodes[llama]+"/",colorcodes[llama]+"/"]
            racetrack[llamacolors.index(llama)+2][math.floor(llamapos[llama])+3:math.floor(llamapos[llama])+5]=[colorcodes[llama]+"\\",colorcodes[llama]+"\\"]
        else:
            racetrack[llamacolors.index(llama)+2][math.floor(llamapos[llama])+1:math.floor(llamapos[llama])+4]=[colorcodes[llama]+"\\",colorcodes[llama]+"X",colorcodes[llama]+"/"]

def frameadd():
    for row in racetrack:
        string=""
        for x in row:
            string+=x
        print(string)
    
generatetrackterrain()  
while frame<10: 
    time.sleep(0.05 )
    racetrack=[]
    for row in trackterrain:
        newrow=[]
        for item in row:
            newrow.append(item)
        racetrack.append(newrow)
    trackrefresh()
    frame=frame+1
    frameadd()
    for llama in llamacolors:
        llamapos[llama]+=llamav[llama]
        llamav[llama]=(llamav[llama]+random.random()*0.1)/1.1