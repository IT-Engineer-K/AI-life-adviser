import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

class Chat:
    def __init__(self, system):
        self.system = system
        self.messages = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=system),
                ],
            ),
        ]
    

    def generate(self, prompt):
        self.messages.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt),
                ],
            ),)
        client = genai.Client(
            api_key=os.environ.get("GEMINI_API_KEY"),
        )

        model = "gemini-flash-latest"
        contents = self.messages
        # 思考なし
        generate_content_config = types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_budget=0,
            ),
        )

        res = ""
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            res += chunk.text
        return res