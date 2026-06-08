from groq import Groq
from IPython.display import Audio

client = Groq(api_key="YOUR_GROQ_API_KEY")

response = client.audio.speech.create(
    model="canopylabs/orpheus-v1-english",
    voice="daniel",
    input="Hello Bhanu. Welcome to Groq text to speech.",
    response_format="wav"
)

response.write_to_file("speech.wav")

Audio("speech.wav")