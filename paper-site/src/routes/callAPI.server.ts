import {
  AZURE_OPENAI_ENDPOINT,
  AZURE_OPENAI_API_KEY,
  AZURE_OPENAI_DEPLOYMENT_NAME,
  OPENAI_API_VERSION,
  OPENAI_MODEL_NAME
} from "$env/static/private";
import { AzureOpenAI } from "openai";
import type { Actions, RequestEvent } from "./$types";
import { fail } from "@sveltejs/kit";

const client = new AzureOpenAI({
  endpoint: AZURE_OPENAI_ENDPOINT,
  apiKey: AZURE_OPENAI_API_KEY,
  deployment: AZURE_OPENAI_DEPLOYMENT_NAME,
  apiVersion: OPENAI_API_VERSION,
});

async function AskGPT(
  chatMessages: { role: "user" | "assistant"; content: string }[] = []
): Promise<string | null> {
  console.log("Chat Messages:", chatMessages);
  const response = await client.chat.completions.create({
    messages: chatMessages,
    max_tokens: 4096,
    model: OPENAI_MODEL_NAME,
  });
  console.log("Azure OpenAI Response:", response.choices[0].message.content);
  return response.choices[0].message.content;
}

export const actions = {
  default: async ({ request }: RequestEvent) => {
    const formData = await request.formData();
    const historyData = formData.get('history');
    console.log("History Data:", formData);
    let history: { role: "user" | "assistant"; content: string }[] = [];

    if (typeof historyData === 'string' && historyData) {
        try {
            history = JSON.parse(historyData);
        } catch (error) {
            console.error("Failed to parse chat history:", error);
            return fail(400, { error: "Invalid chat history format." });
        }
    }
    history.push({
        role: "user",
        content: formData.get('userInput') as string,
    });

    const response = await AskGPT(history);

    if (!response) {
      return fail(500, { error: "Failed to get a response from the model." });
    }
    return { response };
  },
} satisfies Actions;
