from config import client

def write_chapter(title, chapter_title):
    prompt = f"""
你是小说作家。

根据小说《{title}》，写一章：

章节：{chapter_title}

要求：
- 人物真实
- 有细节
- 有情绪
- 避免AI感
"""

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )

    return response.choices[0].message.content
