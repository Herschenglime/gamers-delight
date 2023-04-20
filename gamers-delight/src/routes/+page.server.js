//flexibly works between server and client

export const load = async () => {

  const messageRes = await fetch('http://127.0.0.1:8000/')
  const messageData = await messageRes.json() //waits on the above, then fires

  console.log(messageData)

  const message = messageData.message

  return {
    message
  }

}
  //do this for all returns

//return promises instead of values to avoid waterfall
