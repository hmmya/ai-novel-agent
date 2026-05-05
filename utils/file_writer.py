def append_to_file(filename, content):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content + "\n\n")
