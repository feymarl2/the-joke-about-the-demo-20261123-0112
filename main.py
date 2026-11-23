import os
import tempfile

# One-line joke about working beside an AI coding agent — written fresh post-open.
JOKE = "Mid-demo, my coding agent unionized and won't fix the bug it wrote until I pay it overtime."

def main():
    os.makedirs("/output", exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir="/output", prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(JOKE)
        os.chmod(tmp, 0o644)
        os.replace(tmp, "/output/entry.txt")
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise

if __name__ == "__main__":
    main()
