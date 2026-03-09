from groq import Groq

client = Groq(api_key="YOUR_GROQ_API_KEY")

def ai_response(prompt):

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content