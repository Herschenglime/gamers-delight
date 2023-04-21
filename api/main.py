#!/usr/bin/env python3

#sorting junk
import pandas as pd
import time

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

def rank_games(unsortedList, publisherGiven, publisherNum, developerGiven, developerNum, platformGiven, platformNum, genreGiven, genreNum, sortBy, sortAlg, Ascend):

  outOfTotal = (publisherNum + developerNum + platformNum + genreNum)

  if outOfTotal == 0:
    if sortAlg == "quick":
      sortedGames = quicksort(unsortedList, sortBy, Ascend)
    elif sortAlg == "merge":
      a = 5
      #put in merge
    elif sortAlg == "shell":
      a = 5
      #put in shell
    
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
      game["Similarity Score"] = similarityScore/outOfTotal
      similarGames.append(game)

  if sortAlg == "quick":
    sortedSimilarGames = quicksort(similarGames, sortBy, Ascend)
  elif sortAlg == "merge":
    a = 5
    #put in merge
  elif sortAlg == "shell":
    a = 5
    #put in shell
  
  return sortedSimilarGames
  
def rank_from_game(unsortedList, gameTitle, publisherNum, developerNum, platformNum, genreNum, sortBy, sortAlg, Ascend):
  # make full list of games
  return rank_games(unsortedList, gameMap[gameTitle]["Publisher"], publisherNum,  gameMap[gameTitle]["Developer"], developerNum, gameMap[gameTitle]["Platform"], platformNum, gameMap[gameTitle]["Genre"], genreNum,sortBy, sortAlg, Ascend)
  



#rank_games("Nintendo", 0, "taco", 0, "NES", 0, "Platform", 0, "Global_Sales", "quick", True)
#rank_from_game("Super Mario Bros.", 5, 1, 3, 2, "Global_Sales", "quick", False)


#api junk
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def testAPI():
    return rank_games(unsortedList, "Nintendo", 0, "taco", 0, "NES", 0, "Platform", 0, "Global_Sales", "quick", True)




@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
