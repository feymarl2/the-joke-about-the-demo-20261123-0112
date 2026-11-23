import os

# One-line joke about working beside an AI coding agent — written fresh post-open.
JOKE = "Mid-demo, my coding agent unionized and won't fix the bug it wrote until I pay it overtime."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
