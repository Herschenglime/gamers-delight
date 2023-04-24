<script>
  import Card from './Card.svelte';
  // import { enhance } from '$app/forms';

  export let data;
  const { oneGame, unsorted } = data; //destructuring products array out of data object

  const { gameList, attributes } = unsorted;
  const attributesArray = Object.entries(attributes);

  let gameString = '';
  $: gameString;

 let selectedGame = ""

 function handleGameSearch() {
   selectedGame = gameString;
   console.log(`swag money, you selected ${selectedGame}`)
 }
</script>

<h1 style:text-align="center">Gamer's Delight</h1>

<div class="container">
  <div id="left" class="split">
    <label for="game-name">Game name?</label>
    <input type="text" id="game" name="game" bind:value={gameString} />
    <p>{gameString}</p>

    <button on:click={handleGameSearch}>Search game</button>


    <form method="POST">
      <Card title="Weights">
        <!-- put an each block here once we get the things we care about -->
        <fieldset>
          <div class="slider-group">
            {#each attributesArray as [name, list]}
              <select name={name.slice(0, -1)} id={name.slice(0, -1)}>
                {#each list as attribute}
                  <option value={attribute}>{attribute}</option>
                {/each}
                <!-- smaller each here to go through the possible values to select -->
              </select>
              <label for="">{name.charAt(0).toUpperCase() + name.slice(1)}</label>
              <input
                type="range"
                id="{name.slice(0, -1)}Num"
                name="{name.slice(0, -1)}Num"
                max="5"
                step="1"
                value="4"
              />
              <br />
            {/each}
          </div>
        </fieldset>
      </Card>

      <Card title="Sort By">
        <fieldset>
          <input type="radio" id="sales" name="sortBy" value="Global_Sales" />
          <label for="sales">Sales</label>

          <input type="radio" id="critic-score" name="sortBy" value="Critic_Score" checked />
          <label for="critic-score">Critic Score</label>

          <input type="radio" id="user-score" name="sortBy" value="User_Score" />
          <label for="user-score">User Score</label>

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

  <div id="right" class="split">
    <h2 style:text-align="center">Matches</h2>
    <Card title={oneGame[0].Name}>
      {#if oneGame[0].Similarity_Score}
        this game similar as heck yo
      {:else}
        not similar, yo
      {/if}

      <h4>Year: {oneGame[0].Year_of_Release}</h4>
      <h4>Sales: {(oneGame[0].Global_Sales * 1000000).toLocaleString()}</h4>
      <h4>Platform: {oneGame[0].Global_Sales.Platform}</h4>
      <h4>Genre: {oneGame[0].Genre}</h4>
    </Card>
  </div>
</div>

<!--
     /* https://stackoverflow.com/questions/31913321/how-can-i-limit-length-of-a-value-in-select-tag-in-html */ -->

<style>
  /* https://www.w3schools.com/howto/howto_css_split_screen.asp */
  /* Split the screen in half */
  .container {
    display: flex;
    margin: 0;
  }

  .split {
    display: inline-block;
    overflow-y: auto;
    margin-top: 10px;
    margin: 5px;
  }
  /* Control the left side */
  #left {
    flex: 1;
    border-right: 1px solid;
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
</style>
