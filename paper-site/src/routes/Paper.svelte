<script lang="ts">
  import Tags from "./Tags.svelte";
  import PaperChat from "./PaperChat.svelte";
  let { title, abs, tags } = $props();
  let selected = $state(false);
</script>

<div class="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
  <h3 class="text-xl font-medium text-gray-900 mb-2">{title}</h3>
  <p class="text-gray-600 mb-4">{abs}</p>

  <div class="flex flex-wrap gap-2 mb-4">
    {#each tags as tag}
      <Tags {tag} link={`/tags/${tag}`} />
    {/each}
  </div>

  <div class="border-t border-gray-100 pt-4 mt-2 relative">
    <button
      class="flex items-center justify-center w-10 h-10 bg-blue-600 hover:bg-blue-700 text-white rounded-full shadow-sm transition-all duration-200"
      onclick={()=>{selected = !selected}}
      aria-label="Ask about this paper"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
        />
      </svg>
    </button>

    {#if selected}
      <PaperChat/>
    {/if}
  </div>
</div>
