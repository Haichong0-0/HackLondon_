import openai

openai.api_key = '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'

response = openai.Completion.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  prompt="This is a test prompt to generate text.",
  max_tokens=500,
    messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)

print(response.choices[0].text.strip())
