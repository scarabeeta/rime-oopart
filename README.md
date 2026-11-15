# 刻舟拼音

> 楚人有涉江者，其劍自舟中墜於水，遽契其舟，曰：「是吾劍之所從墜。」舟止，從其所契者入水求之。舟已行矣，而劍不行，求劍若此，不亦惑乎？
>
> ——《呂氏春秋・察今》

刻舟拼音是一套 [Rime](https://rime.im) 輸入方案，使用方法上與朙月拼音無異，但輸出**傳承字形**。

舟行而劍不行，自然是一無所獲。印刷字形幾經整理後舊寫法沉入水底，時代早已走遠。明知其惑而樂此不疲，故名「刻舟」。

英文名 **oopart** 指「出現在不該出現的年代的東西」，此物本色正是不合時宜也。

## 刻舟與偏執

默認模式是**刻舟**，在方案選單裏可以換作**偏執**。

**刻舟**　依 I.字坊《[傳承字形推薦形體表](https://github.com/ichitenfont/inheritedglyphs)》出字：眞、値、敎、靑、淸、吿、尙、硏……另有幾個作者的個人習慣用字：衹（只）、纔（副詞「才」）、甚麼、眾、媆。「才」作名詞時，如天才、人才、才華，一仍其舊。有來歷且不致讓讀者疑爲錯字，適合日常書寫。

**偏執**　溯流而上，每個詞取它最早見於典籍與出土文字的寫法：時作旹，冰作仌，鐵作銕，的確作旳塙，並且作竝且。實用與否概不計較。這些寫法在今天已不合時宜，所以收在這個模式。

| | |
|---|---|
| 通行 | 真正的教育，值得清清靜靜地研究。他只是告訴我，時候還早，並且要先喝茶。我的目的是參加；年年春天，打字作電報。 |
| 刻舟 | 眞正的敎育，値得淸淸靜靜地硏究。他衹是吿訴我，時候還早，並且要先喝茶。我的目的是參加；年年春天，打字作電報。 |
| 偏執 | 眞正的敎毓，値㝵淸淸竫竫地硏究。他衹是吿訴我，旹候還早，竝且要先欱荼。我的目旳是參加；秊秊萅天，朾字乍申報。 |

方案、字典、用戶詞庫等都沿用朙月拼音，平日的打字習慣與詞頻不變，衹在出字前改換字形。

## 安裝

需要先裝好朙月拼音（`luna_pinyin`）和五筆畫（`stroke`）。鼠鬚管、小狼毫自帶；Linux 一般隨 `rime-data` 或 `rime-luna-pinyin` 套件安裝。

用 Rime 的配方管理器[東風破](https://github.com/rime/plum)安裝：

```sh
# 安裝並加入方案選單
rime-install scarabeeta/rime-oopart:customize

# 衹安裝文件，方案選單自行設定
rime-install scarabeeta/rime-oopart
```

各平臺的 `rime-install`：

| 平臺 | 做法 |
|---|---|
| macOS 鼠鬚管 | `"/Library/Input Methods/Squirrel.app/Contents/MacOS/rime-install" scarabeeta/rime-oopart:customize`<br>（會在當前目錄建一個 `plum` 文件夾，裝完可以刪除） |
| Windows 小狼毫 | 「輸入法設定」→「獲取更多輸入方案」，輸入 `scarabeeta/rime-oopart:customize` |
| Linux | `curl -fsSL https://raw.githubusercontent.com/rime/plum/master/rime-install \| bash -s -- scarabeeta/rime-oopart:customize`<br>fcitx5 用戶在前面加 `rime_frontend=fcitx5-rime` |

裝畢重新部署即可。`:customize` 會在 `default.custom.yaml` 裏把刻舟拼音添到方案列表末尾，原有方案悉數保留。

### 手動安裝

把 `oopart.schema.yaml` 與 `opencc/oopart_*` 複製到 Rime 用戶目錄（保留 `opencc/` 子目錄），再在 `default.custom.yaml` 加上：

```yaml
patch:
  schema_list/@next:
    schema: oopart
```

用戶目錄：鼠鬚管 `~/Library/Rime`，小狼毫 `%APPDATA%\Rime`，fcitx5 `~/.local/share/fcitx5/rime`，ibus `~/.config/ibus/rime`。

## 用法

按 `` Ctrl+` `` 或 `F4` 喚出方案選單，選擇「刻舟拼音」。同一選單裏有「刻舟 → 偏執」一項，點按可以切換。

## 偏執的分寸

- 取同詞最早形，體、隸變、古文籀文、甲金文隸定、古今分化、本字皆在其列。古今字一概取古。
- 假借不取，因爲當時尙無專字；後來有了就該用專字。所以從來衹有借字的詞，如的、這、們、嗎，仍用今字；早年借字、後出本字的，取本字，如雕刻作彫刻、邪惡作衺惡。
- 一字數詞者按詞而定。的確作旳塙，「我的」照舊；稱讚作爯贊，稱重照舊；喝水作欱水，吆喝照舊。
- 專名不改，人名、地名、國名悉從其舊。
- 不輾轉相求，凝的本字是冰，冰的初文是仌，但凝衹到冰爲止。
- 不取統一碼擴展 B 區以後的字，因多數字型不能顯示。

每條轉換依據記在 [`docs/paranoid.tsv`](docs/paranoid.tsv)。

## 字表

兩層轉換都是 OpenCC 的純文本詞典，一行一條並以 Tab 分隔。可以直接增刪：

- 刻舟：[`opencc/oopart_inherit_chars.txt`](opencc/oopart_inherit_chars.txt)、[`opencc/oopart_inherit_phrases.txt`](opencc/oopart_inherit_phrases.txt)
- 偏執：[`opencc/oopart_paranoid_chars.txt`](opencc/oopart_paranoid_chars.txt)、[`opencc/oopart_paranoid_phrases.txt`](opencc/oopart_paranoid_phrases.txt)

刻舟一層取推薦形體表的表一（同碼異形）與表二註記，不取擴展 B 區及以後的字。`tools/gen_tables.py` 是作者從自己的底稿重新生成字表所用。

## 來源與許可

本倉庫以 [GPL-3.0-or-later](LICENSE) 發佈。下列來源的署名照其許可證保留；I.字坊的表格經篩選改動，CC-CEDICT 的專名名單依 CC BY-SA 4.0 與 GPLv3 的兼容條款併入。

| 來源 | 用途 | 許可 |
|---|---|---|
| I.字坊《[傳承字形推薦形體表](https://github.com/ichitenfont/inheritedglyphs)》1.04 | 刻舟一層的字形對照（按上述原則篩選並加入個人用字） | CC BY 4.0 |
| [CC-CEDICT](https://cc-cedict.org) | 偏執一層的專名名單 | CC BY-SA 4.0 |
| [說文解字數據](https://github.com/shuowenjiezi/shuowen) | 說文字頭、重文、段注，用以搜羅候選字 | Apache 2.0 |
| [Unihan](https://www.unicode.org/charts/unihan.html) | 異體字關係 | Unicode License |
| [漢語多功能字庫](https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/)（香港中文大學） | 甲骨文、金文字形與字源的查證 | 引用 |

朙月拼音的方案與字典出自 [rime-luna-pinyin](https://github.com/rime/rime-luna-pinyin)（LGPL-3.0），本倉庫僅引用，不收其文件。

## 附言

字形的考訂出於業餘，調査恐有疏漏，望方家不吝指正。

---

*A Rime input schema that types like Luna Pinyin but outputs inherited (traditional printing) glyph forms, with an optional "paranoid" mode that goes back to the earliest attested form of each word.*
