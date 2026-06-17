from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

print("KEY FOUND:", os.getenv("GOOGLE_API_KEY") is not None)

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

try:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say hello"
    )

    print(response.text)

except Exception as e:

    print("ERROR:")
    print(e)