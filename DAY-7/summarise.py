from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

prompt = """
### INSTRUCTION ###

Summarize the text in exactly 3 bullet points.

### INPUT TEXT ###

Artificial Intelligence is transforming
education by enabling personalized learning,
automated assessment systems, intelligent
tutoring platforms, and content generation.
It helps students learn at their own pace
while reducing administrative burden on
educators.

### OUTPUT ###
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)