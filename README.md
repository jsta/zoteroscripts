## zoteroscripts

Recipes for managing your Zotero library with the `pyzotero` interface to the 
Zotero API

### Setup

Create and activate a conda environment with:

```bash
conda env create -n zoteroscripts -f environment.yml
source activate zoteroscripts
```

### Scripts

 * `manage_tags.py`: Remove all tags from a library that don't appear in a specified list

### Tips

Make sure that your local user library is "synced" with Zotero online
