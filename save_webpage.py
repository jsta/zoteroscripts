# python save_webpage.py --title test --description test --url test --name_collection test
import argparse
import itertools
from pyzotero import zotero

try:
    import config
except:
    print("No zotero keys found")

library_type = "user"


def main(title, description, url, name_collection):
    zot = zotero.Zotero(config.library_id, library_type, config.api_key)

    collections = [k for k in zot.all_collections()]
    collection = list(
        itertools.compress(
            collections,
            [coll["data"]["name"] == name_collection for coll in collections],
        )
    )[0]
    key_collection = collection["key"]

    template = zot.item_template("webpage")
    # [k for k in template.keys()]
    template["url"] = url
    template["title"] = title
    template["abstractNote"] = description
    template["collections"].append(key_collection)
    assert zot.check_items([template])

    resp = zot.create_items([template])
    assert len(resp["successful"]["0"]["key"]) > 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", nargs=1, type=str)
    parser.add_argument("--description", nargs=1, type=str, default=[""])
    parser.add_argument("--url", nargs=1, type=str)
    parser.add_argument("--name_collection", nargs=1, type=str)

    args = parser.parse_args()
    # print(args)
    title = args.title[0]
    description = args.description[0]
    url = args.url[0]
    name_collection = args.name_collection[0]

    main(title, description, url, name_collection)
