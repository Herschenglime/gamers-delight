#!/usr/bin/env python3

#sorting junk
import pandas as pd
import time
from fastapi import FastAPI, Form
from pydantic import BaseModel

frame = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016 2.csv")
frame = frame.fillna(-1)

  
  # make full list of games
listOfData = []
for i in range(frame.shape[0]):
    listOfData.append(frame.iloc[i])
unsortedList = listOfData

  # make map of games (dict)
nameList = []
gameList = [] 
for game in listOfData:
    nameList.append(str(game["Name"]))
    gameList.append(game)
zippedFile = zip(nameList, gameList)
gameMap = dict(zippedFile) 

def quicksort(unsortedList, sortBy, Ascending = True):
  start = time.perf_counter()
  if Ascending:
    return quicksortrecursive(unsortedList, sortBy), (time.perf_counter() - start)
  else:
    sortedascend = quicksortrecursive(unsortedList, sortBy)
    sortedascend.reverse()
    end = time.perf_counter()
    return sortedascend, (end - start)

def quicksortrecursive(unsortedList, sortBy):
  greaterThan = []
  equalTo = []
  smallerThan = []
  if len(unsortedList) == 1 or len(unsortedList) == 0:
    return unsortedList
  else:
    pivotPoint = unsortedList[0][sortBy]
    for game in unsortedList:
      if game[sortBy] < pivotPoint:
        smallerThan.append(game)
      elif game[sortBy] == pivotPoint:
        equalTo.append(game)
      elif game[sortBy] > pivotPoint:
        greaterThan.append(game)    
    return quicksortrecursive(smallerThan, sortBy) + equalTo + quicksortrecursive(greaterThan, sortBy)

def mergesort(unsortedList, sortBy, ascending = True):
    start = time.perf_counter()
    sortedascend = mergesortrecursive(unsortedList, sortBy)
    if (ascending):
        return sortedascend, (time.perf_counter() - start)
    return sortedascend.reverse(), (time.perf_counter() - start)

def mergesortrecursive(unsortedList, sortBy):
    length = len(unsortedList)
    if length == 1 or length == 0:
        return unsortedList

    sortedList = []

    midIndex = length // 2

    left = mergesortrecursive(unsortedList[:midIndex], sortBy)
    right = mergesortrecursive(unsortedList[midIndex:], sortBy)
    leftPointer = 0
    rightPointer = 0
    while (leftPointer < midIndex and rightPointer < length - midIndex):
        if left[leftPointer][sortBy] < right[rightPointer][sortBy]:
            sortedList.append(left[leftPointer])
            leftPointer += 1
        else:
            sortedList.append(right[rightPointer])
            rightPointer += 1
    
    while (leftPointer < midIndex):
        sortedList.append(left[leftPointer])
        leftPointer += 1
    
    while (rightPointer < length - midIndex):
        sortedList.append(right[rightPointer])
        rightPointer += 1
    
    return sortedList

def shellsort(unsortedList, sortBy, ascending = True, gapFactor = 2):
    start = time.perf_counter()
    sortedList = unsortedList
    gap = len(sortedList) // gapFactor
    while (gap > 0):
        index = gap
        while (index < len(sortedList)):
            tempIndex = index
            while (tempIndex >= gap and sortedList[tempIndex][sortBy] < sortedList[tempIndex - gap][sortBy]):
                temp = sortedList[tempIndex]
                sortedList[tempIndex] = sortedList[tempIndex - gap]
                sortedList[tempIndex - gap] = temp
                tempIndex -= gap
            index += 1
        gap //= gapFactor
    if (ascending):
      return sortedList, (time.perf_counter() - start)
    return sortedList.reverse(), (time.perf_counter() - start)

def rank_games(unsortedList, publisherGiven, publisherNum, developerGiven, developerNum, platformGiven, platformNum, genreGiven, genreNum, sortBy, sortAlg, Ascend):

  outOfTotal = (publisherNum + developerNum + platformNum + genreNum)

  if outOfTotal == 0:
    if sortAlg == "quick":
      sortedGames = quicksort(unsortedList, sortBy, Ascend)
    elif sortAlg == "merge":
      sortedGames = mergesort(unsortedList, sortBy, Ascend)
    elif sortAlg == "shell":
      sortedGames = shellsort(unsortedList, sortBy, Ascend)
    
    return sortedGames


  similarGames = []
  for game in unsortedList:
    similarityScore = 0
    if (game["Publisher"] == publisherGiven):
      similarityScore += publisherNum
    if (game["Developer"] == developerGiven):
      similarityScore += developerNum
    if (game["Platform"] == platformGiven):
      similarityScore += platformNum
    if (game["Genre"] == genreGiven):
      similarityScore += genreNum
    
    if similarityScore/outOfTotal >= 0.70:
      game["Similarity_Score"] = similarityScore/outOfTotal
      similarGames.append(game)

  if sortAlg == "quick":
    sortedSimilarGames = quicksort(similarGames, sortBy, Ascend)
  elif sortAlg == "merge":
    sortedSimilarGames = mergesort(similarGames, sortBy, Ascend)
  elif sortAlg == "shell":
    sortedSimilarGames = shellsort(similarGames, sortBy, Ascend)
  
  return sortedSimilarGames
  
def rank_from_game(unsortedList, gameTitle, publisherNum, developerNum, platformNum, genreNum, sortBy, sortAlg, Ascend):
  # make full list of games
  return rank_games(unsortedList, gameMap[gameTitle]["Publisher"], publisherNum,  gameMap[gameTitle]["Developer"], developerNum, gameMap[gameTitle]["Platform"], platformNum, gameMap[gameTitle]["Genre"], genreNum,sortBy, sortAlg, Ascend)

def return_one_game_for_testing():
   return unsortedList[0], 27.34

def giveUnsortedList():
   return unsortedList
  



#rank_games("Nintendo", 0, "taco", 0, "NES", 0, "Platform", 0, "Global_Sales", "shell", True)
#rank_from_game("Super Mario Bros.", 5, 1, 3, 2, "Global_Sales", "quick", False)


#api junk
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def testAPI():
    return rank_games(unsortedList, "Nintendo", 0, "taco", 0, "NES", 0, "Platform", 0, "Global_Sales", "merge", True)

@app.get("/onegametest")
async def testingONEGAME():
   return return_one_game_for_testing()

@app.get("/unsorted")
async def giveUnsorted():
   return giveUnsortedList()

@app.post("/submitform")
async def handle_form(gameName: str = Form(...), publisher: str = Form(...), publisherNum: int = Form(...), developer: str = Form(...), developerNum: int = Form(...), platform: str = Form(...), platformNum: int = Form(...), genre: str = Form(...), genreNum: int = Form(...), sortBy: str = Form(...), sortAlg: str = Form(...), ascend: str = Form(...)):
   if gameName == '':
      if ascend == 'true':
        return rank_games(unsortedList,publisher,publisherNum,developer,developerNum,platform,platformNum,genre,genreNum,sortBy, sortAlg, True)
      else:
         return rank_games(unsortedList,publisher,publisherNum,developer,developerNum,platform,platformNum,genre,genreNum,sortBy, sortAlg, False)
   else:
      if ascend == 'true':
         return rank_from_game(unsortedList, gameName, publisherNum,developerNum,platformNum,genreNum,sortBy,sortAlg,True)
      else:
         return rank_from_game(unsortedList, gameName, publisherNum,developerNum,platformNum,genreNum,sortBy,sortAlg,False)
      
class Item(BaseModel):
   gameName: str | None = None
   publisher: str
   publisherNum: str
   developer: str
   developerNum: str
   platform: str
   platformNum: str
   genre: str
   genreNum: str
   sortBy: str
   SortAlg: str
   ascend: str

@app.post("/submitwithpydant")
async def create_item(item: Item):
   if item.gameName == '':
      if item.ascend == 'true':
        return rank_games(unsortedList,item.publisher,int(item.publisherNum),item.developer,int(item.developerNum),item.platform,int(item.platformNum),item.genre,int(item.genreNum),item.sortBy, item.sortAlg, True)
      else:
         return rank_games(unsortedList,item.publisher,int(item.publisherNum),item.developer,int(item.developerNum),item.platform,int(item.platformNum),item.genre,int(item.genreNum),item.sortBy, item.sortAlg, False)
   else:
      if item.ascend == 'true':
         return rank_from_game(unsortedList, int(item.gameName), item.publisherNum,int(item.developerNum),int(item.platformNum),int(item.genreNum),item.sortBy,item.sortAlg,True)
      else:
         return rank_from_game(unsortedList, int(item.gameName), item.publisherNum,int(item.developerNum),int(item.platformNum),int(item.genreNum),item.sortBy,item.sortAlg,False)




@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
