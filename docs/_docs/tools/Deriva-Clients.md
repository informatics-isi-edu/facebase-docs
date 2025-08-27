---
title: Installing DERIVA Clients (Bulk upload and export)
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
