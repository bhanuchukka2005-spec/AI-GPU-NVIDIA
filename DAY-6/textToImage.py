from google import genai

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents="A futuristic AI assistant standing in a modern laboratory"
)

print(response)