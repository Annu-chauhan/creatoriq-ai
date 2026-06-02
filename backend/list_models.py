from google import genai

client = genai.Client(
    api_key="your_gemini_api_key_here"
)

for model in client.models.list():
    print(model.name)