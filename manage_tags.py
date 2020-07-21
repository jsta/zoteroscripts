# remove tags from library that don't appear in a specified list

from pyzotero import zotero
import time

try:
    import config
except:
    print("No zotero keys found")

tags_keep    = ['need to read', 'fun to read', 'important', 'tocite']
library_type = "user"

zot          = zotero.Zotero(config.library_id, library_type, config.api_key)
tags_all     = zot.everything(zot.tags())
tags_rm      = list(set(tags_all) - set(tags_keep)) 
tags_rm      = sorted(tags_rm)

## remove tags individually
# tags_rm[0:2]
# for tag in tags_rm:
#    zot.delete_tags(tag)
#    print(tag)
#    time.sleep(2)

## bulk remove tags in chunks of 50
# zot.delete_tags(*tags_rm[0:2])

# https://stackoverflow.com/a/1751478/3362993
def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

tags_rm = list(chunks(tags_rm, 50))
for tags_rm_subset in tags_rm:
    zot.delete_tags(*tags_rm_subset)
    print(tags_rm_subset[0])
    time.sleep(10)
  