# SPDX-License-Identifier: GPL-3.0-or-later
"""Regenerate the OpenCC tables of 刻舟拼音 (maintainer script).

The tables in opencc/ are plain OpenCC text dictionaries and are the source for
everyone else: edit them directly. The maintainer keeps the master data in a
private book project (build/glyphs.py and build/paranoid*.json) and runs:

    python3 -I tools/gen_tables.py [path/to/book/build]

Outputs:
  opencc/oopart_inherit.json     always on: 傳承字形 + personal choices
  opencc/oopart_paranoid.json    偏執模式 switch: earliest forms on top of that
  docs/paranoid.tsv              the reason for every 偏執 character mapping
"""
import sys, json, pathlib

repo = pathlib.Path(__file__).resolve().parent.parent
book = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path.home() / "projects/book/build")
sys.path.insert(0, str(book))
from glyphs import INHERIT, PARANOID, paranoid_phrases  # noqa: E402

out = repo / "opencc"
out.mkdir(exist_ok=True)


def write(name, title, chars, phrases):
    for kind, table in (("chars", chars), ("phrases", phrases)):
        (out / f"{name}_{kind}.txt").write_text(
            "".join(f"{k}\t{v}\n" for k, v in sorted(table.items())), encoding="utf8")
    group = {"type": "group", "dicts": [{"type": "text", "file": f"{name}_phrases.txt"},
                                        {"type": "text", "file": f"{name}_chars.txt"}]}
    cfg = {"name": title, "segmentation": {"type": "mmseg", "dict": group},
           "conversion_chain": [{"dict": group}]}
    (out / f"{name}.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf8")


# --- 傳承字形 (always on) ---
chars = dict(INHERIT)
# semantic choices: keep the original as a second candidate
chars.update({"只": "衹 只", "繁": "䋣 繁", "才": "纔 才"})
# 才 as a noun stays 才
phrases = {w: w for w in (
    "天才 人才 英才 奇才 口才 文才 才華 才智 才幹 才氣 才子 才女 才俊 才學 才情 才思 才藝 秀才 "
    "蠢才 鬼才 庸才 全才 通才 將才 大才 多才 才德 才識 德才 怪才 幹才 高才").split()}
phrases.update({"才能": "纔能 才能", "什麼": "甚麼", "爲什麼": "爲甚麼", "為什麼": "爲甚麼"})
# 朙月拼音 ranks these first, but merging is 併
phrases.update({"合並": "合併", "一並": "一併"})
write("oopart_inherit", "刻舟拼音・傳承字形", chars, phrases)

# --- 偏執模式 ---
write("oopart_paranoid", "刻舟拼音・偏執模式", dict(PARANOID), paranoid_phrases())

# --- reasons ---
rows = {r["c"]: r for r in json.load(open(book / "paranoid.json", encoding="utf8"))
        if r["decision"] == "map"}
manual = {"並": ("竝", "古今", "竝甲骨已見，並爲後起"),
          "并": ("幷", "隸變", "幷爲說文字頭，并爲隸變省形"),
          "冰": ("仌", "古今", "仌是冰之初文（漢語多功能字庫）；冰本爲凝之本字"),
          "纔": ("才", "古今", "副詞「纔」古作才")}
senses = json.load(open(book / "paranoid_sense_notes.json", encoding="utf8"))
# notes are written in 傳承字形 too (skip the context-dependent 只/繁/才)
_tr = str.maketrans({k: v for k, v in INHERIT.items() if k not in "只繁才" and len(k) == 1})
lines = ["字\t轉爲\t關係\t依據\n"]
for c, t in sorted(PARANOID.items()):
    if c in manual:
        _, kind, note = manual[c]
    elif c in rows:
        kind, note = rows[c]["kind"], rows[c]["note"]
        if kind == "drop-loan":
            kind = "本字"
    elif c in senses:
        kind, note = senses[c]["kind"], senses[c]["note"]
    else:
        kind, note = "", ""
    note = " ".join(note.split()).replace("廣韵", "廣韻").translate(_tr)
    lines.append(f"{c}\t{t}\t{kind}\t{note}\n")
(repo / "docs" / "paranoid.tsv").write_text("".join(lines), encoding="utf8")
print(f"inherit: {len(chars)} chars, {len(phrases)} phrases; "
      f"paranoid: {len(PARANOID)} chars, {len(paranoid_phrases())} phrases")
