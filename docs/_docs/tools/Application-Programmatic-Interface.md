---
title: Application Programming Interface
permalink: /docs/Application-Programming-Interface/
---

If you are building software or services that interface with the FaceBase platform, you will need to install the [Deriva Client API (deriva-py)]({{ "/docs/Deriva-Clients/" | relative_url }}). Below, we give examples of how to use the APIs for a few key operations: lookup vocabulary terms, create a dataset and upload files.

## Before You Begin

Many operations on FaceBase that are read-only do not require authentication. However, operations that access pre-release data (i.e., your own data), retrieve controlled access data, or operations that make updates for your own data submission will require authentication.

For these operations that require authentication, you must first [establish an access token](#authentication) in order to use the APIs. You must have a registered FaceBase user account and you must be a member of a FaceBase [project](https://www.facebase.org/chaise/recordset/#1/isa:project) that has been approved to upload datasets or be a member of an approved controlled access Data Access Request. If you are unsure about any of this, please contact [help@facebase.org](mailto:help@facebase.org).

## Lookup Vocabulary Terms

If you retrieve FaceBase data, it is typically annotated with vocabulary term identifiers such as `UBERON:0001684`. You may want to lookup the preferred name, in this case, `mandible`.

```python
from deriva.core import DerivaServer

# establish connection
server = DerivaServer('https', hostname)
catalog = server.connect_ermrest(catalog_id)
_ = catalog.getPathBuilder()

# first get a handle to the vocabular table; this will fail if no such table exists.
vocabulary = _.vocab.tables[vocab_table_name]

# now lookup the term; this will return a `ResultSet` that behaves like a python 
# sequence and it will not have any entries if there is no match for the `term_id`.
terms = vocabulary.filter(vocabulary.id == term_id).entities()
```

A complete example may be found in [lookup_vocab_example.py](/assets/files/lookup_vocab_example.py).

## Create a Dataset

Your code must instantiate the `DerivaServer`, connect to the "catalog", resolve the project identifier, and insert a minimal metadata record, and get back the dataset's record identifier (RID).

```python
from deriva.core import DerivaServer, get_credential

# get credentials and connect
credential = get_credential(hostname)
server = DerivaServer('https', hostname, credential)
catalog = server.connect_ermrest(catalog_id)
_ = catalog.getPathBuilder()

# resolve project id
projects = _.isa.project.filter(_.isa.project.RID == project_rid).entities()

# insert minimal metadata record
dataset_records = _.isa.dataset.insert([metadata], defaults={'id', 'accession', 'released', 'release_date'}

rid = dataset_records[0]['RID']
```

A complete example may be found in [create_dataset_record_example.py](/assets/files/create_dataset_record_example.py).

### Organize Files

Next you must re-organize your files under a directory named according to the dataset RID. Let's say that your RID is `1-2345`. Your files must be organized under `path/to/1-2345`. For complete details on allowable file names, please review our [filename conventions](../Upload-Files/#filename-conventions). There are many standard APIs for moving or copying files, so the steps here are left as an exercise for the reader.

### Upload Files

Finally, you will invoke the `DerivaUpload` API to upload your files to FaceBase. Note that the API returns a results object with status codes and human-readable labels for each file processed.

```python
from deriva.transfer import GenericUploader

# create server dictionary
server={
    "host": hostname,
    "protocol": "https",
    "catalog_id": catalog_id,
}

# instantiate and invoke the uploader
uploader = GenericUploader(server=server)
try:
    uploader.getUpdatedConfig()
    uploader.scanDirectory(path)
    results = uploader.uploadFiles()
    print(results)
except Exception as e:
    print(e)
finally:
    uploader.cleanup()
```

A complete example may be found in [upload_dataset_files_example.py](/assets/files/upload_dataset_files_example.py).
