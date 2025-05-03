---
title: DERIVA Tools - Bulk upload and export
permalink: /docs/Deriva-Clients/
---

DERIVA Clients are used for authenticating to the FaceBase server, bulk uploading of data, and bulk downloading of data.
They include both graphical desktop applications and command-line applications.

- **DERIVA Upload Command Line Interface** and `deriva-upload-cli` for batch upload of files for data contributors.
- **BDBag** and `bdbag` for batch download of files for all users.
- `deriva-globus-auth-utils` for authentication for command-line applications.


## Installing the DERIVA Client Bundle

The DERIVA Clients are bundled for installation on Mac, Windows, and Linux.

### System Requirements
- macOS,
- Windows, or
- Linux (recent distros of Ubunto and Fedora preferred with Python 3+)

### Installation for Windows or MacOS users

Download and install the DERIVA Client Bundle from the [official releases page](https://github.com/informatics-isi-edu/deriva-client-bundle/releases).

**Important note for Mac users**: If you are using a Mac with Apple Silicon-based hardware (i.e., "M1", "M2", etc.), you 
may experience an error that requires installation of our latest development build found [here](https://buildbot.derivacloud.org/~buildbot/deriva-client-bundle/dev/DERIVA-Client-Tools-1.7.0-202410011807-osx.dmg).
You will also need to delete the hidden directory `$HOME/.deriva` before re-running the applications.

### Installation for Linux users

Install the clients from the Python PyPI package.
```commandline
$ pip3 install --user deriva-client
```

The `--user` option may be used at your discretion. Alternatively, consider creating and installing the package in
a virtual environment.

The desktop applications can be invoked with the commands `deriva-upload` and `bdbag-gui`.

### Basic Installation

If you only want the programming interfaces (APIs) and command line interfaces (CLIs), and you know you do not want the desktop graphical client applications, consider installing the `deriva` package instead.

```commandline
$ pip3 install --user deriva
```

## Authentication Tokens

The command-line clients (cli) can be run from the local host or a remote
server, such as a compute cluster used to process data. When running on a
remove server, the `deriva-upload-cli` and `bdbag` utilities
may require an authentication token.

### DO NOT SHARE YOUR TOKEN

The authentication token is equivalent to a short-term, temporary password, in
simple terms. Treat it as you would your FaceBase username and password.
- Do not share it with anyone.
- Do not copy and paste it into an email.

### Authentication Token Lifetime

The authentication token will **expire in 30 minutes** by default. However, the
authentication client will refresh the token so long as you use the `--refresh` 
option.

### Establish an Authentication Token

Use the following command to establish an authentication token with the server.

```commandline
$ deriva-globus-auth-utils login --refresh --host www.facebase.org
```

The command will open a browser window unless you use the `--no-browser` flag. By using
the `--no-browser` flag, the client will instead instruct you to follow a URL to authenticate
to FaceBase and then return to the terminal window to enter the authentication token. This 
method is typical for users transfering files from a remote server such as a cluster where their
data files are stored. The `--refresh` flag is optional but recommended to ensure your session 
remains active for the duration of your data transfer operation.

Note that the `deriva-globus-auth-utils` and the command-line applications for upload or download
must be run on the same computer. You do not copy tokens between computers or applications.

### Terminate an Authentication Token

When you are finished using the authentication token, logout using the following command _on the same computer_ 
that you issued the login command. When you do this, the token will be invalidated immediately.

```commandline
$ deriva-globus-auth-utils logout
```

## Programmatic Interface Examples (Preview)

_The documentation here is under review. Do not attempt to use it unless you have first contacted the FaceBase team._

If you are building tools or other services that interface with the FaceBase platform, you will need the [basic installation](#basic-installation) described above. We have two example scripts to demonstrate how to use the APIs to (a) create a dataset and then (b) upload files.

### Before You Begin

You must first [establish an authentication token](#establish-an-authentication-token) in order to use the APIs to make any modifications to the FaceBase data. You must have a registered FaceBase user account and you must be a member of a FaceBase "project" that has been approved to upload datasets. If you are unsure about any of this, please contact [help@facebase.org](mailto:help@facebase.org).

### Create a Dataset

Your code must import the `DerivaServer`, connect to the "catalog", resolve the project identifier, and insert a minimal metadata record, and get back the dataset's record identifier (RID).

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
dataset_records = _.isa.dataset.insert([metadata], defaults={'id', 'accession', 'released'}

rid = dataset_records[0]['RID']
```

A complete example may be found in [create_dataset_record_example.py](/assets/files/create_dataset_record_example.py).

### Organize Files

Next you must re-organize your files under a directory named according to the dataset RID. Let's say that your RID is `1-2345`. Your files must be organized under `path/to/1-2345`. They may have any subdirectory hierarchy or none at all, for example `path/to/1-2345/my_image.png` and `path/to/1-2345/a/B/c/my_tabular_data.csv` are allowable. There are many standard APIs for moving or copying files, so the steps here are left as an exercise for the reader.

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
