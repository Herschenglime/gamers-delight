const apiurl = 'http://127.0.0.1:8000/'

export const load = async () => {

  const messageRes = await fetch(apiurl)
  const messageData = await messageRes.json() //waits on the above, then fires

  const message = messageData.message

  return {
    message
  }

}
  //do this for all returns

//return promises instead of values to avoid waterfall
