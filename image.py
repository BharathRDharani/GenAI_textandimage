from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "What teams are playing in this image?",
                },
                {
                    "type": "input_image",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/IPL_T20_Chennai_vs_Kolkata.JPG/1280px-IPL_T20_Chennai_vs_Kolkata.JPG"
                }
            ]
        }
    ]
)

print(response.output_text)