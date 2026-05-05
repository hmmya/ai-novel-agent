from config import client

def optimize_text(text):
    prompt = f"""
优化以下内容：
- 去AI痕迹
- 增强情绪
- 增强画面感

内容：
{text}
"""

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )

    return response.choices[0].message.content
