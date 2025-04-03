<script lang="ts">
  import Spotlight from "./Paper.svelte";
  import Chat from "./Chat.svelte";
</script>

<svelte:head>
  <title>Paper Agent</title>
  <meta
    name="description"
    content="Search and chat about academic papers with our AI assistant"
  />
</svelte:head>

<div class="min-h-screen bg-gray-50 flex flex-col">
  <header class="py-6 bg-white shadow-sm">
    <div class="container mx-auto px-4">
      <div class="flex justify-between items-center">
        <h1 class="text-2xl font-medium text-gray-800">
          <span class="font-sans font-black font-stretch-extra-condensed overline align-top">Paper</span><span class="align-sub font-serif font-light underline decoration-wavy text-blue-600">Agent</span>
        </h1>
        <div class="text-sm text-gray-500">Matthew M Li, Data Scientist</div>
      </div>
    </div>
  </header>

  <main class="flex-grow container mx-auto px-4 py-8 max-w-5xl">
    <div class="text-center mb-16 mt-10">
      <h2 class="text-3xl font-bold text-gray-900 mb-4">
        Discover Academic Research
      </h2>
      <p class="text-xl text-gray-600 max-w-2xl mx-auto">
        Chat with our AI assistant about academic papers. Ask questions, get
        summaries, and explore research across disciplines.
      </p>
    </div>

    <div
      class="bg-white rounded-xl shadow-md overflow-hidden border border-gray-100"
    >
    <Chat />
    </div>

    <div class="mt-16 grid md:grid-cols-3 gap-8">
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
        <div class="text-blue-600 mb-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
            />
          </svg>
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">Latest Research</h3>
        <p class="text-gray-600">
          Access the most recent academic papers from top journals and
          conferences.
        </p>
      </div>
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
        <div class="text-blue-600 mb-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
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
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">AI-Powered Chat</h3>
        <p class="text-gray-600">
          Ask questions about papers and get intelligent responses from our AI
          assistant.
        </p>
      </div>
      <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
        <div class="text-blue-600 mb-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"
            />
          </svg>
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">
          Multiple Categories
        </h3>
        <p class="text-gray-600">
          Browse papers across categories including AI, ML, NLP, CV, robotics,
          and more.
        </p>
      </div>
    </div>

    <!-- Spotlight Papers Section -->
    <div class="mt-16">
      <h2 class="text-2xl font-bold text-gray-900 mb-6">Spotlight</h2>

      <div class="space-y-6">
        <!-- papers -->
        <Spotlight
          title="Understanding the Limitations of Self-Supervised Learning"
          abs="This paper discusses the limitations of self-supervised learning methods and proposes a new approach to address these challenges."
          tags={["AI", "ML"]}
        />
      </div>
    </div>

    <footer class="mt-16 text-center text-gray-500 text-sm">
      <p>© {new Date().getFullYear()} Matthew M Li. All rights reserved.</p>
    </footer>
  </main>
</div>
