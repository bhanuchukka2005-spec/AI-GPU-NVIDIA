from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

prompt = """
Classify the sentiment of the following review:

'The laptop performance is excellent and battery life is amazing.'

Output only:
Positive, Negative, or Neutral
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)