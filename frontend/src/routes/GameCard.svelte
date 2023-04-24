<script>
  import Card from './Card.svelte';
  export let game;
</script>

<Card title={game.Name}>
  {#if game.Similarity_Score}
    <p><b>Similarity Score:</b> {game.Similarity_Score}</p>
  {/if}

  <p><b>Year:</b> {game.Year_of_Release}</p>
  <p><b>Sales:</b> {(game.Global_Sales * 1000000).toLocaleString()}</p>
  <p><b>Platform:</b> {game.Platform}</p>
  <p><b>Genre:</b> {game.Genre}</p>

  {#if game.Critic_Score != -1}
    <p><b>Critic Score:</b> {game.Critic_Score}</p>
  {/if}
  {#if game.User_Score != -1}
    <p><b>User Score:</b> {game.User_Score}</p>
  {/if}
</Card>
