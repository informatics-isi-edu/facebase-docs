---
title: Installing DERIVA Clients (Bulk upload and export)
permalink: /docs/Deriva-Clients/
---

- [Which instructions should I follow?](#which-instructions-should-i-follow)
- [Windows](#windows)
- [macOS](#macos)
  - [What is different when using the command line](#what-is-different-when-using-the-command-line)
  - [1. Check that you have Python 3](#1-check-that-you-have-python-3)
    - [Option A: Command-line developer tools](#option-a-command-line-developer-tools)
    - [Option B: Installer from python.org](#option-b-installer-from-pythonorg)
  - [2. Install the clients](#2-install-the-clients)
  - [Next step](#next-step)
  - [If you want the desktop application](#if-you-want-the-desktop-application)
- [Linux](#linux)
- [Authentication](#authentication)
  - [Establish an Access Token](#establish-an-access-token)
    - [The --no-browser Option](#the---no-browser-option)
    - [The --refresh Option](#the---refresh-option)
  - [Terminate an Access Token](#terminate-an-access-token)
- [Troubleshooting](#troubleshooting)
  - [The installation fails with PyQtWebEngine or metadata-generation-failed](#the-installation-fails-with-pyqtwebengine-or-metadata-generation-failed)
  - [error: externally-managed-environment](#error-externally-managed-environment)
  - [NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+](#notopensslwarning-urllib3-v2-only-supports-openssl-111)
  - [command not found after installing](#command-not-found-after-installing)
  - [pip3: command not found](#pip3-command-not-found)
  - [Still stuck?](#still-stuck)

DERIVA Clients are used for authenticating with the FaceBase server, bulk uploading data, and bulk downloading data. They include both graphical desktop applications and command-line applications.

- **DERIVA Upload** and `deriva-upload-cli` for batch upload of files for data contributors.
- **BDBag** and `bdbag` for batch download of files for all users.
- `deriva-globus-auth-utils` for authentication for command-line applications.

On Windows and Linux, both the desktop and command-line applications are available. **On macOS, we recommend the command-line applications**; see [macOS](#macos) below.

## Which instructions should I follow?

| Your computer | Install | What you get |
| :---- | :---- | :---- |
| [Windows](#windows) | Installer bundle (`.msi`) | Desktop applications and command-line applications |
| [macOS](#macos) | Python package `deriva` — **recommended**<br>Installer bundle (`.dmg`) — [check whether your Mac can run it](#if-you-want-the-desktop-application) | Command-line applications only<br>Desktop applications and command-line applications |
| [Linux](#linux) | Python package `deriva-client` | Desktop applications and command-line applications |

If you are on Windows or Linux and you only want the command-line applications and programming interfaces, you may follow the macOS instructions instead — the `deriva` package works on all three platforms.

## Windows

Download the latest `.msi` file:

- [Official Releases (Recommended)](https://buildbot.derivacloud.org/~buildbot/deriva-client-bundle/release/)
- [Nightly Builds](https://buildbot.derivacloud.org/~buildbot/deriva-client-bundle/dev/)

Double-click the downloaded installer and follow the prompts to complete the installation.

The bundle installs the **DERIVA Upload** and **BDBag** desktop applications. It also adds a shortcut called **DERIVA Command Line Applications**, which opens a terminal window with all DERIVA prerequisites and clients installed and ready to use.

Next: [Uploading Data Files](../Upload-Files/).

## macOS

There are two ways to install the DERIVA clients on a Mac.

**The command-line applications are the recommended option.** They work on every Mac, regardless of its age or which version of macOS it runs, and they are the option we will continue to support. Follow [steps 1 and 2](#1-check-that-you-have-python-3) below.

The **DERIVA Upload** desktop application is available through the current macOS installer bundle (`.dmg`), but not on every Mac, and it is not a long-term option on any Mac. We are working on a replacement macOS installer bundle. If you would prefer a graphical application and your Mac can run the current one, see [If you want the desktop application](#if-you-want-the-desktop-application) at the end of this section.

<!--
MAINTAINER NOTE: keep this section date-free. Apple's timeline for removing the translation
layer has already shifted once, and a published date invites contributors to postpone. Put the
timing in the newsletter announcement instead. The same applies to the "A replacement is in
progress" note further down — no target date, and remove that note once the new bundle ships.
-->

### What is different when using the command line

Two things work differently than they do with the desktop application. Both catch people out, so they are worth reading before you start.

- **There is no application window.** You run commands in the Terminal app instead. Terminal is in your Applications folder, under Utilities.
- **Logging in is a separate step.** The desktop application has a **Login** button. With the command-line applications you run a login command once, before you upload. See [Authentication](#authentication).

### 1. Check that you have Python 3

Open Terminal and run:

```commandline
$ python3 --version
$ pip3 --version
```

If the first command reports Python 3.9 or later and the second reports a version number, you already have everything you need — continue to [step 2](#2-install-the-clients).

Otherwise, install Python using one of the options below. Option A is the quickest and is sufficient for uploading and downloading data.

You do not need to install `pip` separately. It is included with Python 3. If `pip3` is not found but `python3` is, run `python3 -m pip --version`, then use `python3 -m pip` in place of `pip3` throughout these instructions.

#### Option A: Command-line developer tools

This is the simplest option and requires no downloads. In Terminal, run:

```commandline
$ xcode-select --install
```

Accept the prompt and wait for the installation to finish — it may take several minutes. Then run `python3 --version` again to confirm.

#### Option B: Installer from python.org

Use this option if you want a newer version of Python than Apple provides.

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest macOS installer.
2. Open the downloaded `.pkg` file and follow the prompts.
3. Open a **new** Terminal window and run `python3 --version` to confirm.

### 2. Install the clients

```commandline
$ pip3 install --user deriva
```

Confirm the installation:

```commandline
$ deriva-upload-cli --help
```

**On macOS, install `deriva`, not `deriva-client`.** The `deriva-client` package also includes the desktop applications, which currently do not install reliably on all macOS versions. If you have already tried it and seen an error, see [Troubleshooting](#the-installation-fails-with-pyqtwebengine-or-metadata-generation-failed).

If the command above fails with `error: externally-managed-environment`, see [Troubleshooting](#error-externally-managed-environment).

You only need to do these two steps once.

### Next step

Installation is complete. See ["Uploading Data Files"](../Upload-Files/) for instructions on how to log in and upload files for a dataset.

### If you want the desktop application

The **DERIVA Upload** desktop application is available for macOS in the installer bundle (`.dmg`), but whether it will run depends on your Mac:

- **Intel Macs**: the bundle installs and runs.
- **Apple silicon Macs** (M1, M2, M3, and later): the bundle relies on Apple's Rosetta translation software. It will run only if Rosetta is installed, and Apple is phasing Rosetta out.

Either way, the current bundle is not a long-term option, and we recommend the command-line applications above for any new setup.

**A replacement is in progress.** We are working on a new macOS installer bundle that does not depend on Rosetta. We do not have a release date to share yet, and we will announce it here and through our usual channels when it is ready. In the meantime, the command-line applications are fully supported and our recommended option.

**Which Mac do I have?** Open the Apple menu and choose **About This Mac**. If it lists an Apple M-series chip, you have an Apple silicon Mac. If it lists an Intel processor, you have an Intel Mac. You can also run `uname -m` in Terminal: `arm64` means Apple silicon, `x86_64` means Intel.

If your Mac can run it, download the latest `.dmg` file:

- [Official Releases (Recommended)](https://buildbot.derivacloud.org/~buildbot/deriva-client-bundle/release/)
- [Nightly Builds](https://buildbot.derivacloud.org/~buildbot/deriva-client-bundle/dev/)

Double-click the downloaded installer and follow the prompts. Then see [Configure the DERIVA Upload app](../Upload-Files/#configure-the-deriva-upload-app).

## Linux

Install the clients from the Python PyPI package:

```commandline
$ pip3 install --user deriva-client
```

The `--user` option may be used at your discretion. Alternatively, consider creating and installing the package in a virtual environment.

The desktop applications can be invoked with the commands `deriva-upload` and `bdbag-gui`.

If you only want the programming interfaces (APIs) and command-line interfaces (CLIs), and you know you do not want the desktop graphical client applications, install the `deriva` package instead:

```commandline
$ pip3 install --user deriva
```

Next: [Uploading Data Files](../Upload-Files/).

## Authentication

The command-line clients (CLIs) can be run on the local host or on a remote server, such as a compute cluster used to process data. Often, using the CLI requires an access token. Below, we describe how to establish an access token (a.k.a., bearer token) for use with the CLIs.

**IMPORTANT**: *Do not share your access token.* In simple terms, the access token is equivalent to a short-term, temporary password. Treat it as you would your FaceBase username and password.

- Do not share it with anyone.
- Do not copy and paste it into an email.
- Do not store it anywhere visible to others.

### Establish an Access Token

Use the following command to establish an access token.

```commandline
$ deriva-globus-auth-utils login --refresh --host www.facebase.org
```

Running the above command will open a web browser to initiate the user login. Follow the usual steps to log in using your FaceBase username and password. See the `--no-browser` option for more details.

#### The `--no-browser` Option

By default, the `deriva-globus-auth-utils login` command will open a web browser on the computer where it is run. You may, however, want to run these commands on a remote computer -- for example, if you are transferring data to or from a compute cluster or other server. In this case, you will want to run the command from the remote computer using the `--no-browser` option.

```commandline
$ deriva-globus-auth-utils login --refresh --host www.facebase.org --no-browser
```

Using the `--no-browser` flag will instead prompt you to follow a `URL` to authenticate with FaceBase, then return to the terminal window to enter the access token. Simply open a web browser on your local computer (laptop or desktop), copy and paste the `URL`, follow the login procedures as usual, copy the resulting access token, and finally paste the token into the prompt given by the `deriva-globus-auth-utils login` command.

#### The `--refresh` Option

The `--refresh` flag is optional but recommended to keep your token active during your data transfer operation. By default, the access token is valid for approximately 48-72 hours. For long-running data transfers, you may need more than 48 hours, and therefore using `--refresh` will keep your access token from expiring.

### Terminate an Access Token

When you are finished using the access token, log out using the following command *on the same computer* that you issued the login command. When you do this, the token will be invalidated immediately.

```commandline
$ deriva-globus-auth-utils logout
```

## Troubleshooting

### The installation fails with `PyQtWebEngine` or `metadata-generation-failed`

You will see output ending with something like:

```
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> PyQtWebEngine
```

This happens when `deriva-client` is installed on macOS. That package includes the desktop applications, which depend on components that are not reliably available for macOS and must otherwise be built from source. Install the `deriva` package instead:

```commandline
$ pip3 install --user deriva
```

Nothing needs to be cleaned up first — the failed installation did not change anything.

### `error: externally-managed-environment`

The full message looks something like this:

```
error: externally-managed-environment

× This environment is externally managed
```

This means `pip` is refusing to install into your Python installation because that installation is managed by something else. It most commonly happens when Python was installed with [Homebrew](https://brew.sh), and it is not a problem with your setup — it is how those Python installations are designed to behave.

The fix is to install the clients in a virtual environment, which is a self-contained folder that contains its own copy of Python and any packages you add to it.

Create the environment once:

```commandline
$ python3 -m venv ~/deriva-env
$ source ~/deriva-env/bin/activate
$ pip install deriva
```

Then activate it each time you open a new Terminal window, **before** running any DERIVA command:

```commandline
$ source ~/deriva-env/bin/activate
```

Your prompt will show `(deriva-env)` while the environment is active. When you are finished, you may leave it by running `deactivate` or by simply closing the Terminal window.

Once this is done, continue to [Uploading Data Files](../Upload-Files/).

### `NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+`

You may see this warning at the top of the output every time you run a command:

```
NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'.
```

**This is harmless and can be ignored.** It reports a detail of the Python installation included with macOS. It does not affect uploads or downloads.

### `command not found` after installing

The clients were installed, but the folder containing them may not be on your `PATH`. On macOS, add the following line to `~/.zshrc`, replacing `3.x` with the version reported by `python3 --version`:

```commandline
export PATH="$HOME/Library/Python/3.x/bin:$PATH"
```

On Linux, the equivalent folder is usually `$HOME/.local/bin`. Open a new terminal window for the change to take effect.

If you installed it into a virtual environment, check that it is active. Your prompt should show `(deriva-env)`. If it does not, run `source ~/deriva-env/bin/activate` and try again.

### `pip3: command not found`

Python 3 is either not installed or not on your `PATH`. See [step 1](#1-check-that-you-have-python-3).

### Still stuck?

Send an email to [help@facebase.org](mailto:help@facebase.org). Include the command you ran and your `upload.log` file, or the complete error message if you were unable to upload.
