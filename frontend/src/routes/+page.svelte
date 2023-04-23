<script>
  import Card from './Card.svelte';

  export let data;
  const { oneGame, unsorted } = data; //destructuring products array out of data object


</script>

<h1 style:text-align="center">Gamer's Delight</h1>

<div class="container">
  <div id="left" class="split">
    <form>
      <label for="game-name">Game name?</label>
      <input type="text" id="game-name" />

      <Card title="Weights">
        <!-- put an each block here once we get the things we care about -->
        <fieldset>
          <div class="slider-group">
            <select name="publisher" id="publisher">
              <!-- smaller each here to go through the possible values to select -->
              <option value="nintendo">Nintendo</option>
            </select>
            <label for="">Publisher</label>
            <input type="range" id="publisher-weight" name="publisher" max="5" step="1" value="4" />
          </div>
        </fieldset>
      </Card>

      <Card title="Sort By">
        <fieldset>
          <input type="radio" id="sales" name="sort-criteria" value="sales" checked />
          <label for="sales">Sales</label>

          <input type="radio" id="critic-score" name="sort-criteria" value="critic-score" />
          <label for="critic-score">Critic Score</label>

          <input type="radio" id="user-score" name="sort-criteria" value="user-score" />
          <label for="user-score">User Score</label>

          <br />

          <input type="radio" id="ascending" name="sort-order" value="ascending" />
          <label for="ascending">Ascending</label>

          <input type="radio" id="descending" name="sort-order" value="descending" checked />
          <label for="descending">Descending</label>
        </fieldset>
      </Card>

      <Card title="Sorting Algorithm">
        <input type="radio" id="shell" value="shell" name="sort" checked />
        <label for="shell">Shell Sort</label>

        <input type="radio" id="quick" value="quick" name="sort" />
        <label for="quick">Quick Sort</label>

        <input type="radio" id="merge" value="merge" name="sort" />
        <label for="merge">Merge Sort</label>
      </Card>
    </form>
  </div>

  <div id="right" class="split">
    <h2 style:text-align="center">Matches</h2>
    <Card title="{oneGame[0].Name}">
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
</style>
