from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="microsoft/phi-3-medium-128k-instruct:free",
  messages=[
    {
      "role": "user",
      "content": "hi"
    }
  ]
)
print(completion.choices[0].message.content)

