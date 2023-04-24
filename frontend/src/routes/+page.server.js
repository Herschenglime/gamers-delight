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

    const attributes = { publishers, developers, platforms, genres }

    for (const attributeName in attributes) {
      attributes[attributeName].delete(-1)
      attributes[attributeName].add("N/A")

      //convert set to array for iterability in svelte
      attributes[attributeName] = [...attributes[attributeName]]
    }

    return { gameList, attributes }
  }


  return {
    oneGame: fetchTest(),
    unsorted: fetchUnsorted()
  }

}

/** @type {import('./$types').Actions} */
export const actions = {
  default: async ({ request }) => {
    const formData = await request.formData()
    const gameObj = {}

    formData.forEach((value, key) => (gameObj[key] = value));

    console.log(gameObj)
    const simpleData = {message: "hello good friend"}
    // console.log(data)

    const response = await fetch(apiurl + 'submitwithpydant', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(gameObj)
    });

    const resData = await response.json();
    console.log(resData)
  }
};
