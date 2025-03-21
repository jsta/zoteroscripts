## zoteroscripts

Recipes for managing your Zotero library with the `pyzotero` interface to the Zotero API

### Setup

1. Create and activate a conda environment with:

```bash
conda env create -n zoteroscripts -f environment.yml
source activate zoteroscripts
```

2. Store your API `library_id` and `api_key` credentials in a file named `config.py`

### Scripts

* `manage_tags.py`: Remove all tags from a library that don't appear in a specified list

* `notes_to_csv.py`: Export all notes from a given collection to a csv file

* `save_webpage.py`: CLI tool to save a webpage to a given collection

### Tips

Make sure that your local user library is "synced" with Zotero online

### References

https://pyzotero.readthedocs.io/en/latest/
