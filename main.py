from agents.planner import plan_story
from agents.writer import write_chapter
from agents.optimizer import optimize_text
from utils.file_writer import append_to_file

TITLE = "万界误差"

def run():
    print("📌 生成大纲...")
    outline = plan_story(TITLE)
    append_to_file("output/novel.txt", "【大纲】\n" + outline)

    chapters = [
        "第1章 初入裂界",
        "第2章 异常浮现",
        "第3章 规则错位",
        "第4章 初次修正",
        "第5章 危机升级"
    ]

    for ch in chapters:
        print(f"✍️ 生成 {ch} ...")

        content = write_chapter(TITLE, ch)
        optimized = optimize_text(content)

        append_to_file("output/novel.txt", f"{ch}\n{optimized}")

    print("✅ 完成！")

if __name__ == "__main__":
    run()
