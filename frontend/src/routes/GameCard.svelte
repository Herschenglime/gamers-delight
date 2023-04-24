<script>
  import Card from './Card.svelte';
  export let game;
</script>

<Card title={game.Name}>
  {#if game.Similarity_Score}
    <p>Similarity Score: {game.Similarity_Score}</p>
  {/if}

  <h4>Year: {game.Year_of_Release}</h4>
  <h4>Sales: {(game.Global_Sales * 1000000).toLocaleString()}</h4>
  <h4>Platform: {game.Platform}</h4>
  <h4>Genre: {game.Genre}</h4>
</Card>
