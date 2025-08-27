---
title: Application Programmatic Interface
permalink: /docs/Application-Programmatic-Interface/
---

If you are building tools or other services that interface with the FaceBase platform, you will need the [basic installation described on this page]({{ "/docs/Deriva-Clients/" | relative_url }}). We have two example scripts to demonstrate how to use the APIs to (a) create a dataset and then (b) upload files.

## Before You Begin

You must first [establish an access token](#authentication) in order to use the APIs to make any modifications to the FaceBase data. You must have a registered FaceBase user account and you must be a member of a FaceBase "project" that has been approved to upload datasets. If you are unsure about any of this, please contact [help@facebase.org](mailto:help@facebase.org).

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
