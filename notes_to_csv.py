from pyzotero import zotero
import pandas as pd
import re

try:
    import config
except:
    print("No zotero keys found")

pd.set_option("display.max_columns", None)
library_type = "group"
library_id = "2545340"

# make sure API key has sufficient permissions
zot = zotero.Zotero(library_id, library_type, config.api_key)

collection_id_top_level = pd.DataFrame.from_dict(zot.collections())["key"][0]

# ---

notes = pd.DataFrame(columns=["notes"])
items = zot.collection_items(collection_id_top_level)
for item in items:
    try:
        notes = notes.append(
            {"notes": item["data"]["note"], "parent": item["data"]["parentItem"]},
            ignore_index=True,
        )
    except:
        notes = notes.append({"notes": ""}, ignore_index=True)
notes = notes.loc[[len(x) > 0 for x in notes["notes"]]]

# ---

citations = pd.DataFrame(columns=["citation"])
for parent in notes["parent"]:
    citations = citations.append(
        {
            "citation": zot.item(
                parent,
                content="citation",
                format="keys",
                style="taylor-and-francis-council-of-science-editors-author-date",
            ),
            "parent": parent,
        },
        ignore_index=True,
    )

# ---

res = citations.set_index("parent").join(notes.set_index("parent"))
res["citation"] = [re.sub("\['|'\]", "", str(x)) for x in res["citation"]]
res["citation"] = [re.sub("<.*?>", "", str(x)) for x in res["citation"]]
res["notes"] = [re.sub("<.*?>", "", str(x)) for x in res["notes"]]

res.to_csv("notes.csv", index=False)
