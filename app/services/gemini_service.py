from google import genai
from google.genai import types
from config.settings import settings

class GeminiService:
    def __init__(self , user_api_key):
        self.client = genai.Client(
            api_key=user_api_key
        )

    def analyze_image(self, image_bytes, mime_type, prompt):
        contents = [
            types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
            types.Part.from_text(text=prompt)
        ]

        response = self.client.models.generate_content(
            model=settings.MODEL_NAME,
            contents=contents,
            config={
                "temperature": settings.AI_TEMPERATURE,
                "top_p": settings.AI_TOP_P,
                "top_k": settings.AI_TOP_K,
                "max_output_tokens": settings.AI_MAX_TOKENS,
            }
        )

        return response.text
