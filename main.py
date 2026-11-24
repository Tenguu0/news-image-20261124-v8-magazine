import os
import shutil
import sys
from pathlib import Path


def publish() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 2
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        print("error: entry.png is missing next to main.py", file=sys.stderr)
        return 2
    dest = Path(out_dir) / "entry.png"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    return 0


raise SystemExit(publish())
