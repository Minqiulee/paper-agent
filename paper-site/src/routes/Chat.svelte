<script lang="ts">
    import { onMount, tick } from "svelte";
    let searchQuery = "";
    let chatMessages: { role: "user" | "assistant"; content: string }[] = [];
    let isLoading = false;
    let chatContainer: HTMLElement;

    function scrollChatToBottom() {
        if (chatContainer) {
        chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    }

    async function handleSearch() {
        if (!searchQuery.trim()) return;
    
        isLoading = true;
        chatMessages = [...chatMessages, { role: "user", content: searchQuery }];
        
        await tick();
        scrollChatToBottom();
    
        // Simulate a response - in a real implementation, this would be an API call
        setTimeout(async () => {
            chatMessages = [
                ...chatMessages,
                {
                    role: "assistant",
                    content: `Here are some papers related to "${searchQuery}". Would you like me to explain any of these in more detail?`,
                },
            ];
            searchQuery = "";
            isLoading = false;
    
            // Wait for DOM updates before scrolling
            await tick();
            scrollChatToBottom();
        }, 1000);
    }

    function resetChat() {
        chatMessages = [];
        searchQuery = "";
    }

    onMount(() => {
        // Focus the search input on page load
        const searchInput = document.querySelector(
        'input[type="text"]'
        ) as HTMLInputElement;
        if (searchInput) {
        searchInput.focus();
        }
    });
</script>


{#if chatMessages.length > 0}
  <div
    class="max-h-[400px] overflow-y-auto p-6 space-y-4 bg-gray-50"
    bind:this={chatContainer}
  >
    {#each chatMessages as message}
      <div
        class="flex {message.role === 'assistant'
          ? 'justify-start'
          : 'justify-end'}"
      >
        <div
          class="max-w-[80%] px-4 py-3 rounded-lg {message.role === 'assistant'
            ? 'bg-white shadow-sm text-gray-800'
            : 'bg-blue-600 text-white'}"
        >
          <p>{message.content}</p>
        </div>
      </div>
    {/each}
    {#if isLoading}
      <div class="flex justify-start">
        <div class="bg-white shadow-sm text-gray-800 rounded-lg px-4 py-3">
          <div class="flex space-x-2">
            <div class="w-2 h-2 rounded-full bg-gray-300 animate-bounce"></div>
            <div
              class="w-2 h-2 rounded-full bg-gray-300 animate-bounce"
              style="animation-delay: 0.2s"
            ></div>
            <div
              class="w-2 h-2 rounded-full bg-gray-300 animate-bounce"
              style="animation-delay: 0.4s"
            ></div>
          </div>
        </div>
      </div>
    {/if}
  </div>
{/if}

<!-- Search Input -->
<div
  class="p-6 bg-white {chatMessages.length > 0
    ? 'border-t border-gray-100'
    : ''}"
>
  <form on:submit|preventDefault={handleSearch} class="flex gap-2">
    <input
      type="text"
      bind:value={searchQuery}
      placeholder="Ask about academic papers..."
      class="flex-grow px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
    />
    <button
      type="submit"
      class="px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium transition-colors"
      disabled={isLoading}
    >
      {isLoading ? "Searching..." : "Search"}
    </button>
    {#if chatMessages.length > 0}
      <button
        type="button"
        on:click={resetChat}
        class="px-3 py-2 bg-gray-100 hover:bg-gray-200 text-gray-600 rounded-lg transition-colors"
      >
        Clear
      </button>
    {/if}
  </form>

  {#if chatMessages.length === 0}
    <div class="mt-6 text-center text-gray-500">
      <p>
        Examples: "Show me recent papers on machine learning" • "Find papers
        about climate change" • "Summarize papers on quantum computing"
      </p>
    </div>
  {/if}
</div>
