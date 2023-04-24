
<svelte:head>
   <!-- this makes the page dark by default -->
  <meta name="color-scheme" content="dark"/>
</svelte:head>

<slot/>

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
</style>
