from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
r = OpenAI().chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": "Powiedz 'działa'"}],
)
print(r.choices[0].message.content)
print(r)
