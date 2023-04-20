<script>
 export let data
 const { message } = data //destructuring products array out of data object
</script>

<h1 style:text-align="center">Gamer's Delight</h1>

<div class="split">
  <div id="left">
    test
  </div>

  <div id="right">

    over here too
  </div>

</div>


<svelte:head>
   <!-- this makes the page dark by default -->
  <meta name="color-scheme" content="dark light"/>
</svelte:head>
<style>
:root {
  font-family: sans-serif;
 }

@media (prefers-color-scheme: dark) {
  :root {
    --color-lightest: hsl(0deg, 0%, 0%);
    --color-lighter: hsl(0deg, 0%, 20%);
    --color-light: hsl(0deg, 0%, 40%);
    --color-strong: hsl(0deg, 0%, 60%);
    --color-stronger: hsl(0deg, 0%, 80%);
    --color-strongest: hsl(0deg, 0%, 100%);
  }
}
 /* https://www.w3schools.com/howto/howto_css_split_screen.asp */
 /* Split the screen in half */
.split {
  display: flex;
}

/* Control the left side */
#left {
  flex: 1;
  background-color: #111;
}

/* Control the right side */
#right {
  flex: 1;
  background-color: red;
}

</style>
