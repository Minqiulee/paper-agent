<script lang="ts">
  import { preventDefault } from "svelte/legacy";
  import Tags from "./Tags.svelte";
  let { title, abs, tags } = $props();
  let openedPaper: number | null = $state(null);
  let paperQuestions: Record<number, string> = $state({});
  let paperResponses: Record<number, string> = $state({});

  function handlePaperQuestion(paperId: number) {
    if (!paperQuestions[paperId]?.trim()) return;
    // Simulate a response - in a real implementation, this would be an API call
    setTimeout(() => {
      paperResponses[paperId] =
        `This is a simulated response for your question about paper ${paperId}.`;
      paperQuestions[paperId] = "";
    }, 1000);
  }
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
      onclick={() => (openedPaper = openedPaper === 1 ? null : 1)}
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

    {#if openedPaper === 1}
      <div
        class="mt-4 p-4 bg-gray-50 rounded-lg shadow-md transition-all duration-100 origin-top-left"
      >
        <form
          onsubmit={(event) => {
            event.preventDefault();
            handlePaperQuestion(1);
          }}
          class="flex gap-2"
        >
          <input
            type="text"
            bind:value={paperQuestions[1]}
            placeholder="Ask a question about this paper..."
            class="flex-grow px-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
          <button
            type="submit"
            class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium transition-colors"
          >
            Ask
          </button>
        </form>

        {#if paperResponses[1]}
          <div class="mt-4 bg-white p-4 rounded-lg shadow-sm">
            <p class="text-gray-800">{paperResponses[1]}</p>
          </div>
        {/if}
      </div>
    {/if}
  </div>
</div>
