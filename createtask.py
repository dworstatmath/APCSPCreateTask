import random
import math
tracklength=150
frame=0
terrain=[".",".","'",",","*",".",".","'",",","*",":"]
trackterrain=[]
racetrack=[]
horsecolors=["yellow", "red", "blue", "green"]
colorcodes={"yellow":"\033[1;33m","red":"\033[0;31m", "blue":"\033[0;34m","green":"\033[0;32m"}
horsepos={"yellow":0,"red":0, "blue":0,"green":0}
horsedir={"yellow":random()*0.5,"red":random()*0.5, "blue":random()*0.5,"green":random()*0.5}
money="$100"
print("   /^>")
print(",###/")
print("// \\\\")
def generatetrackterrain():
    for i in range(len(horsecolors)+2):
        row=[]
        for j in range(tracklength):
            row.append(random.choice(terrain))
        trackterrain.append(row)
def trackrefresh():
    for horse in horsecolors:
        racetrack[horsecolors.index(horse)][math.floor(horsepos[horse]):math.floor(horsepos[horse])+3]=[colorcodes[horse]+"/",colorcodes[horse]+"^",colorcodes[horse]+">"]
        racetrack[horsecolors.index(horse)+1][math.floor(horsepos[horse]):math.floor(horsepos[horse])+3]=[colorcodes[horse]+"/",colorcodes[horse]+"^",colorcodes[horse]+">"]
def frame():
    frame+=1
    for row in racetrack:
        string=""
        for x in row:
            string+=x
        print(string)

