from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_answer(query, docs):
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a BIS expert.

Context:
{context}

Task:
Give top 3 BIS standards and reasons.

Return JSON:
{{
 "standards": [],
 "reasons": []
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content