---
title: DERIVA Tools - Bulk upload and export
permalink: /docs/Deriva-Clients/
---

DERIVA Clients are used for authenticating to the FaceBase server, bulk uploading of data, and bulk downloading of data.
They include both graphical desktop applications and command-line applications.

- **DERIVA Upload** and `deriva-upload-cli` for batch upload of files for data contributors.
- **BDBag** and `bdbag` for batch download of files for all users.
- `deriva-globus-auth-utils` for authentication for command-line applications.

## Installing the DERIVA Client Bundle

The DERIVA Clients are bundled for installation on Mac, Windows, and Linux.

### System Requirements
- macOS,
- Windows, or
- Linux

### Installation for Windows or MacOS users

Download latest `.msi` file for Windows users or `.dmg` file for Mac OS users:
 - [Official Releases (Recommended)](https://buildbot.derivacloud.org/~buildbot/deriva-client-bundle/release/)
 - [Nightly Builds](https://buildbot.derivacloud.org/~buildbot/deriva-client-bundle/dev/)

Double-click the downloaded installer, and follow the prompts to complete the installation.

<!--
THIS NOTE SHOULD NOT BE RELEVANT ANY MORE

**Important note for Mac users**: If you are using a Mac with Apple Silicon-based hardware (i.e., "M1", "M2", etc.), you 
may experience an error that requires installation of our latest development build. You will also need to delete the hidden directory `$HOME/.deriva` before re-running the applications.
//-->

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

## Authentication

The command-line clients (CLI) can be run from the local host or a remote
server, such as a compute cluster used to process data. Often, using a 
CLI will require an access token. Below, we describe how to establish an 
access token (a.k.a., bearer token) for use with the CLIs.

**IMPORTANT**: _Do not share your access token._
The access token is equivalent to a short-term, temporary password, in
simple terms. Treat it as you would your FaceBase username and password.
- Do not share it with anyone.
- Do not copy and paste it into an email.
- Do not store it anywhere visible to others.

### Establish an Access Token

Use the following command to establish an access token.

```commandline
$ deriva-globus-auth-utils login --refresh --host www.facebase.org
```

Running the above command will open a web browser to initiate the user login.
Follow the usual steps to login using your FaceBase username and password. See 
the `--no-browser` option for more details.

#### The `--no-browser` Option

By default, the `deriva-globus-auth-utils login` command will open a web browser
on the computer on which it was run. You may, however, want to run these commands
on a remote computer -- for example, if you are transfering data to or from a 
compute cluster or other server. In this case, you will want to run the command 
from the remote computer using the `--no-browser` option.

```commandline
$ deriva-globus-auth-utils login --refresh --host www.facebase.org --no-browser
```

Using the `--no-browser` flag will instead instruct you to follow a `URL` to authenticate
to FaceBase and then return to the terminal window to enter the access token. Simply
open a web browser on your local computer (laptop or desktop), copy and paste the `URL`,
follow the login procedures as usual, copy the resulting access token, and finally paste
the token into the prompt given by the `deriva-globus-auth-utils login` command.

#### The `--refresh` Option

The `--refresh` flag is optional but recommended to ensure your token 
remains active for the duration of your data transfer operation. By default, 
the access token is valid for approximately 48-72 hours. For long-running data
transfers, you may need more than 48 hours and therefore using `--refresh` will 
keep your access token from expiring.

### Terminate an Access Token

When you are finished using the access token, logout using the following command 
_on the same computer_ that you issued the login command. When you do this, the token 
will be invalidated immediately.

```commandline
$ deriva-globus-auth-utils logout
```

## Programmatic Interface Examples

If you are building tools or other services that interface with the FaceBase platform, you will need the [basic installation](#basic-installation) described above. We have two example scripts to demonstrate how to use the APIs to (a) create a dataset and then (b) upload files.

### Before You Begin

You must first [establish an access token](#authentication) in order to use the APIs to make any modifications to the FaceBase data. You must have a registered FaceBase user account and you must be a member of a FaceBase "project" that has been approved to upload datasets. If you are unsure about any of this, please contact [help@facebase.org](mailto:help@facebase.org).

### Create a Dataset

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
