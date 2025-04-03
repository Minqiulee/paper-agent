<script lang="ts">
  let {tag, link} = $props();
</script>

<a href={link} class="inline-block">
  <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs font-medium rounded-full">{tag}</span>
</a>