---
title: DERIVA Tools - Bulk upload and export
permalink: /docs/Deriva-Clients/
---

These instructions are a supplement to the [documentation for uploading files to FaceBase](../Upload-Files/).

The DERIVA client tools are used for authenticating to the FaceBase server, bulk uploading of data, and bulk downloading of data. We provide both graphical desktop clients and command-line interface clients.

- DERIVA Client Tools
    - `DERIVA-Auth`: a desktop client for establishing an authentication token.
    - `DERIVA-Upload`: a desktop client for uploading data files.
- DERIVA Python command-line clients (Python 3.x)
    - `deriva-upload-cli`: a command-line utility for uploading data files.
    - `deriva-download-cli`: a command-line utility for downloading data files.


## Installing DERIVA Client Tools

The DERIVA-Upload, DERIVA-Auth, and Command-Line clients are bundled for installation on Mac, Windows, and Linux.

#### System Requirements
- macOS,
- Windows, or
- Linux (recent distros of Ubunto and Fedora preferred with Python 3+)

#### Installation steps for Windows and MacOS
1. Go to the [Deriva Client Tools Releases](https://github.com/informatics-isi-edu/deriva-client-bundle/releases) page.
2. Download the appropriate file for your Operating System.
3. Run the installer.

#### Installation steps for Linux
1. Open a terminal
2. Use the Python PIP command: `pip3 install --user deriva-client`

**Note**:
 - On Windows and MacOS, the installation will create launchers and icons for the desktop applications.
 - On Linux, the desktop applications can be invoked from a new terminal window with the commands `deriva-auth` and `deriva-upload`.

## Authentication Tokens

The command-line clients (cli) can be run from the local host or a remote
server, such as a compute cluster used to process data. When running on a
remove server, the `deriva-upload-cli` and `deriva-download-cli` utilities
_require_ an authentication token, so you _must_ be able to install and run
the desktop DERIVA-Auth utility on a Windows, macOS, or Linux desktop even
if you plan to upload/download data files using the CLI from another server.
The CLI can be run remotely from the DERIVA-Auth.

Most likely if you are transferring large files to/from a cluster, you will run
DERIVA-Auth on your local desktop to establish and maintain the authentication
token, while you run the `deriva-upload-cli` or `deriva-download-cli` from your
cluster just passing it the authentication token that you established with
DERIVA-Auth as a parameter when you invoke the CLI.

### DO NOT SHARE YOUR TOKEN

The authentication token is equivalent to a short-term, temporary password, in
simple terms. Treat it as you would your FaceBase username and password.
- Do not share it with anyone.
- Do not copy and paste it into an email.

### Authentication Token Lifetime

The authentication token will **expire in 30 minutes** by default. However, the
DERIVA-Auth client will refresh the token so long as you leave the DERIVA-Auth
client open and running on your desktop.

For long transfers, keep the authentication agent running on your local
system while the remote transfer is in progress. If you close the DERIVA-Auth
client, any ongoing transfers (past the 30 minute limit) will fail and report
'not authorized' errors.

### Establish an Authentication Token

Now you need to establish and copy your authentication token for use with the command-line client:

1. Open the DERIVA-Auth application.
2. First time use:
    - In the *Server:* input box enter `www.facebase.org`
    - Click **Add**.
3. Subsequent use:
    - Ensure that the *Server:* field indicates `www.facebase.org`
    - Click **Login**.
3. Follow the prompts in the main panel to login.
4. Copy the "bearer" token:
    - Click **Show Token**.
    - Click **Show Details...** (see the figure below).
    - Copy the token.
    - Click **Close**.

![Window that will allow you to copy the token]({{ "/assets/img/deriva-clients-auth-tok.jpeg" | relative_url }})

If there are any errors, they should be reported in the status panel beneath the file listing panel.

### Terminate an Authentication Token

When you are finished using the authentication token, click **Logout** and exit the application. When you do this, the token will be invalidated immediately.
