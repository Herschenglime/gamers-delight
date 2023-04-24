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

    const publisher = new Set()
    const developer = new Set()
    const platform = new Set()
    const genre = new Set()

    for (const game of gameList) {
      publisher.add(game.Publisher)
      developer.add(game.Developer)
      platform.add(game.Platform)
      genre.add(game.Genre)
    }

    const attributes = { publisher,developer, platform,genre }

    for (const attributeName in attributes) {
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
    console.log("submitted form")
    const formData = await request.formData()
    const gameObj = {}

    formData.forEach((value, key) => (gameObj[key] = value));

    console.log(gameObj)
    const simpleData = { message: "hello good friend" }

    const response = await fetch(apiurl + 'submitwithpydant', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        "Content-Type": "application/json",
      },
      body: JSON.stringify(gameObj)
    });

    const resData = await response.json();
    console.log(resData)
    return { success: true, resData }
  }
};
