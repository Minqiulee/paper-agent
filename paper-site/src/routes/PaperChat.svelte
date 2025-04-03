<script lang="ts">
  let paperQuestion = $state("");
  let paperResponse = $state("");
  function handlePaperQuestion(paperId: number, paperQuestions: string) {
    if (!paperQuestions[paperId]?.trim()) return;
    // Simulate a response - in a real implementation, this would be an API call
    paperResponse = `This is a simulated response for ${paperQuestion} about paper ${paperId}.`;
  }
</script>

<div
  class="mt-4 p-4 bg-gray-50 rounded-lg shadow-md transition-all duration-100 origin-top-left"
>
  <form
    onsubmit={(event) => {
      event.preventDefault();
      handlePaperQuestion(1, paperQuestion);
    }}
    class="flex gap-2"
  >
    <input
      type="text"
      bind:value={paperQuestion}
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
  {#if paperResponse}
    <div class="mt-4 bg-white p-4 rounded-lg shadow-sm">
      <p class="text-gray-800">{paperResponse}</p>
    </div>
  {/if}
</div>
