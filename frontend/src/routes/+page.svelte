<script lang="js">
  import Card from './Card.svelte';
  import GameCard from './GameCard.svelte';
  // import { enhance } from '$app/forms';

  /** @type {import('./$types').PageData} */
  export let data;

  /** @type {import('./$types').ActionData} */
  export let form;
  const resData = form?.resData;
  // $: matches = resData[0];
  // $: resTime = resData[1];

  // console.log(matches);

  const { unsorted } = data; //destructuring products array out of data object

  const { gameList, attributes } = unsorted;
  // console.log(gameList)
  const attributesArray = Object.entries(attributes);

  let gameString = '';
  $: gameString;

  let selectedGameName = '';

  function handleGameSearch() {
    selectedGameName = gameString;
    console.log(`swag money, you selected ${selectedGameName}`);

    const found = gameList.find((element) => element.Name === gameString);

    if (found) {
      console.log(found);
      console.log(attributesArray);
      for (const attributePair of attributesArray) {
        const attributeName = attributePair[0];
        const selectElement = document.getElementById(attributeName);

        let foundVal = found[attributeName.charAt(0).toUpperCase() + attributeName.slice(1)]; //uppercase first letter

        console.log('foundVal pre-conversion: ' + foundVal);
        foundVal = foundVal == -1 ? 'N/A' : foundVal;
        console.log('foundVal post-conversion: ' + foundVal);

        console.log(attributeName);

        selectElement.value = foundVal;
      }
    } else {
      alert('Game not found in database.');
    }
  }
</script>

<div class="everything">
  <h1 style:text-align="center">Gamer's Delight</h1>
  {#if form?.success}
    <h3>Sort time: {resData[1]}</h3>
  {/if}

  <div class="container">
    <div id="left" class="split">
      <div class="scrollable-list">
        <form on:submit|preventDefault={handleGameSearch}>
          <label for="game-name">Game name?</label>
          <input type="text" id="game" name="game" bind:value={gameString} />
          <button>Search game</button>
        </form>

        <p>{gameString}</p>

        <form method="POST">
          <Card title="Weights">
            <!-- put an each block here once we get the things we care about -->
            {#await attributesArray}
              <p>...data not yet loaded...</p>
            {:then attributesArray}
              <fieldset>
                <div class="slider-group">
                  {#each attributesArray as [name, list]}
                    <select {name} id={name}>
                      {#each list as attribute}
                        <option value={attribute} id="{name}-{attribute}">{attribute}</option>
                      {/each}
                      <!-- smaller each here to go through the possible values to select -->
                    </select>
                    <label for="">{name.charAt(0).toUpperCase() + name.slice(1)}</label>
                    <input
                      type="range"
                      id="{name.toLowerCase()}Num"
                      name="{name.toLowerCase()}Num"
                      max="5"
                      step="1"
                      value="4"
                    />
                    <br />
                  {/each}
                </div>
              </fieldset>
            {:catch error}
              <p>data didn't load :(</p>
            {/await}
          </Card>

          <Card title="Sort By">
            <fieldset>
              <input type="radio" id="sales" name="sortBy" value="Global_Sales" />
              <label for="sales">Sales</label>

              <input type="radio" id="critic-score" name="sortBy" value="Critic_Score" checked />
              <label for="critic-score">Critic Score</label>

              <input type="radio" id="year" name="sortBy" value="Year_of_Release" />
              <label for="year">Year of Release</label>

              <br />

              <input type="radio" id="ascending" name="ascend" value="true" />
              <label for="ascending">Ascending</label>

              <input type="radio" id="descending" name="ascend" value="false" checked />
              <label for="descending">Descending</label>
            </fieldset>
          </Card>

          <Card title="Sorting Algorithm">
            <input type="radio" id="shell" value="shell" name="sortAlg" />
            <label for="shell">Shell Sort</label>

            <input type="radio" id="quick" value="quick" name="sortAlg" checked />
            <label for="quick">Quick Sort</label>

            <input type="radio" id="merge" value="merge" name="sortAlg" />
            <label for="merge">Merge Sort</label>
          </Card>

          <button>Submit form</button>
        </form>
      </div>
    </div>

    <div id="right" class="split">
      <h2 style:text-align="center">Matches</h2>
      <div class="scrollable-list">
        {#if form?.success}
          {#each resData[0].slice(0,50) as game}
            <GameCard {game} />
          {/each}
        {/if}
      </div>
    </div>
  </div>
</div>

<!--
     /* https://stackoverflow.com/questions/31913321/how-can-i-limit-length-of-a-value-in-select-tag-in-html */ -->

<style>
  /* https://www.w3schools.com/howto/howto_css_split_screen.asp */
  /* Split the screen in half */
  .container {
    display: flex;
    margin: 0px;
    max-height: inherit;
  }

  .split {
    display: inline-block;
    margin-top: 10px;
    margin: 5px 5px 0 5px;
    max-height: inherit;
  }
  .scrollable-list {
    overflow-y: scroll;
    display: flex;
    flex-direction: column;
    height: 100vh;
    max-height: inherit;
  }
  /* Control the left side */
  #left {
    flex: 1;
  }

  /* Control the right side */
  #right {
    flex: 1;
  }

  .slider-group {
    text-align: center;
  }

  select {
    width: 100%;
    max-width: 10em;
    text-overflow: ellipsis;
  }

  .everything {
    margin: 0px;
    padding: 0px;
    height: 100vh;
  }
</style>
