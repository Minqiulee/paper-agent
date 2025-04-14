<script lang="ts">
  import { enhance } from "$app/forms";

  let userInput = "";
  let chatMessages: { role: "user" | "assistant"; content: string }[] = [];
  let isLoading = false;
  let chatContainerElement: HTMLElement;
</script>

<form
  method="POST"
  use:enhance={(form) => {
    return async ({ result, update }) => {
      // Prevent empty submission
      if (!userInput.trim()) {
        form.cancel();
        return;
      }

      // Add user message immediately for responsiveness
      chatMessages = [...chatMessages, { role: "user", content: userInput }];
      isLoading = true;

      userInput = "";

      // Runs after form submission completes
      isLoading = false;
      // Check result.data for success/error properties based on server action return
      if (result.type === "success" && result.data?.response) {
        chatMessages = [
          ...chatMessages,
          { role: "assistant", content: result.data.response as string },
        ];
      } else {
        // Handle unexpected result types if necessary
        chatMessages = [
          ...chatMessages,
          {
            role: "assistant",
            content: "Error: Unexpected response from server.",
          },
        ];
      }
      await update({ reset: false }); // Prevent form reset if desired, apply changes
    };
  }}
>

<input type="hidden" name="history" value={JSON.stringify(chatMessages)} />
</form>
