from config import client

def plan_story(title):
    prompt = f"""
你是一个小说结构规划师。

请为小说《{title}》生成：
1. 故事大纲
2. 章节列表（10章）

要求：
- 有节奏
- 有冲突
- 有成长
"""

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
