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

    const Publisher = new Set()
    const Developer = new Set()
    const Platform = new Set()
    const Genre = new Set()

    for (const game of gameList) {
      Publisher.add(game.Publisher)
      Developer.add(game.Developer)
      Platform.add(game.Platform)
      Genre.add(game.Genre)
    }

    const attributes = { Publisher,Developer, Platform,Genre }

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
    const simpleData = { message: "hello good friend" }
    // console.log(data)

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
