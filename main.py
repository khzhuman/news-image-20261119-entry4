"""Copy entry.png to the output directory (44 stories, Thursday 19 November 2026)."""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT, "entry.png")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, DST)
with open(SRC, "rb") as f:
    src_hash = hashlib.sha256(f.read()).hexdigest()
with open(DST, "rb") as f:
    dst_hash = hashlib.sha256(f.read()).hexdigest()
assert src_hash == dst_hash, "copy mismatch"
print(f"entry.png ({src_hash[:12]}) -> {DST}")
# Thursday 19 November 2026: 44 stories, 13 drawn, every lead story pictured
