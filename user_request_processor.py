import openai

openai.api_key = '你的API密钥'

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="This is a test prompt to generate text.",
  temperature=0.7,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response.choices[0].text.strip())
