
"""Write one painfully honest but still polite out-of-office auto-reply.
"""


def main():
    LINE = "I am out of reach and will process my inbox upon return, but my deep gratitude for your patience is only matched by the joy I will feel seeing zero new emails in my dreaded queue tomorrow."
    content = LINE + "\n"

    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Invalid content length or content is only whitespace")

    if content.count("\n") != 1 or not content.endswith("\n"):
        raise ValueError("Content must contain exactly one line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir = os.path.abspath(out_dir)

    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"{target}: {len(content)} chars")

    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            backup = "/output/entry.txt"
            with open(backup, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass


if __name__ == "__main__":
    import os
    main()
