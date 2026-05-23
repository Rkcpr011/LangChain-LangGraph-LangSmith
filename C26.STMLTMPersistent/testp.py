from openai import OpenAI

endpoint = "https://rkcpr-azr-ai-001.services.ai.azure.com/openai/v1"
deployment_name = "gpt-5.4"


client = OpenAI(
    base_url=endpoint
  
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

print(completion.choices[0].message)