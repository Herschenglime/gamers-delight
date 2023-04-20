<script type="text/javascript">
 export let title;
</script>

<div class="card">
  <h3 style:text-align="center">{title}</h3>
  <slot/>
</div>

<style>
.card {
  border: solid;
  border-width: 2px;
  border-radius: 10px;
  background-color: var(--color-lighter);
  margin: 5px 5px 5px 0;
  padding: 10px;
 }

</style>
