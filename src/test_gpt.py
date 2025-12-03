from openai import OpenAI
client = OpenAI()

res = client.responses.create(
    model="gpt-4o-mini",
    input="Say hello"
)

print(res.output_text)
