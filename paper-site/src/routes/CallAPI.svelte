<script lang="ts">
  import {
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT_NAME,
    OPENAI_API_VERSION,
  } from "$env/static/private";

  function AskGPT(chatMessages: { role: "user" | "assistant"; content: string }[] = []) {
    // TODO
  }
</script>
