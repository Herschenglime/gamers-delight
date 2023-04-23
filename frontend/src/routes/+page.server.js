const apiurl = 'http://127.0.0.1:8000/'

export const load = async () => {

  const fetchMessage = async () => {
    const messageRes = await fetch(apiurl)
    const messageData = await messageRes.json() //waits on the above, then fires

    return messageData.message
  }

  const fetchTest = async () => {
    const gameRes = await fetch(apiurl + 'onegametest')
    const gameData = await gameRes.json() //waits on the above, then fires
    const game = gameData[0]
    const responseTime = gameData[1]

    return gameData
  }

  return {
    message: fetchMessage(),
    oneGame: fetchTest()
  }

}
  //do this for all returns

//return promises instead of values to avoid waterfall
