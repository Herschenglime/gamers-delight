const apiurl = 'http://127.0.0.1:8000/'

export const load = async () => {

  const fetchTest = async () => {
    const gameRes = await fetch(apiurl + 'onegametest')
    const gameData = await gameRes.json() //waits on the above, then fires
    const game = gameData[0]
    const responseTime = gameData[1]

    return gameData
  }

  const fetchUnsorted = async () => {
    const listRes = await fetch(apiurl + 'unsorted')
    const gameList = await listRes.json() //waits on the above, then fires

    const publishers = new Set()
    const developers = new Set()
    const platforms = new Set()
    const genres = new Set()

    for (const game of gameList) {
      publishers.add(game.Publisher)
      developers.add(game.Developer)
      platforms.add(game.Platform)
      genres.add(game.Genre)
    }

    const sortables = {publishers, developers, platforms, genres}

    for (const sortableName in sortables) {
      console.log(sortableName)
      sortables[sortableName].delete(-1)
    }

    console.log(sortables)
    return {gameList, sortables}
  }


  return {
    oneGame: fetchTest(),
    unsorted: fetchUnsorted()
  }

}
  //do this for all returns

//return promises instead of values to avoid waterfall
