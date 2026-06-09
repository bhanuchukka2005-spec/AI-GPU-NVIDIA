from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

prompt = """
A company has 125 employees.

40% work in Software Development.
25% work in Testing.
The remaining employees work in Support.

Think step by step and calculate:

1. Number of Software Developers
2. Number of Test Engineers
3. Number of Support Staff
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)