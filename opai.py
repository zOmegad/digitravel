from dotenv import load_dotenv
import os
import openai

load_dotenv('.env')


openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-curie-001",
  prompt="Q: Describe me Paris as if i were a tourist",
  temperature=0,
  max_tokens=240,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response["choices"][0]["text"])