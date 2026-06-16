from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

try:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="""
        Generate exactly 3 questions and answers on DBMS.

        Format:

        Question: <question>
        Answer: <answer>

        Question: <question>
        Answer: <answer>

        Question: <question>
        Answer: <answer>
        """
    )

    print("\n===== GEMINI RESPONSE =====\n")
    print(response.text)

except Exception as e:

    print("\n===== ERROR =====\n")
    print(e)