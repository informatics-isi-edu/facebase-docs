---
title: Uploading Data Files
permalink: /docs/Upload-Files/
---

- [Before You Begin](#before-you-begin)
- [Interactive File Upload](#interactive-file-upload)
- [Batch File Upload](#batch-file-upload)
  - [Organize your files](#organize-your-files)
    - [Filename Conventions](#filename-conventions)
  - [Install the DERIVA client tools](#install-the-deriva-client-tools)
  - [Configure the DERIVA Upload app](#configure-the-deriva-upload-app)
  - [Upload files with DERIVA Upload](#upload-files-with-deriva-upload)
  - [Upload files with deriva-upload-cli](#upload-files-with-deriva-upload-cli)
    - [Warnings you can ignore](#warnings-you-can-ignore)
- [Review the uploaded files](#review-the-uploaded-files)
  - [Display of thumbnails](#display-of-thumbnails)
  - [Display of surface models](#display-of-surface-models)
  - [Display of Genome Browser tracks](#display-of-genome-browser-tracks)

There are two ways to upload files:

- **Interactive**: upload files individually from your web browser (recommended for smaller datasets).
- **Batch**: upload files in a batch using command-line utilities or desktop applications (recommended for large volumes of data).

## Before You Begin

You must first [create a dataset](../Create-a-Dataset/) and [describe the experiments and biosamples](../Describe-Experiments-and-Biosamples/) used for that dataset. Once you have completed those steps, you may upload data files.

## Interactive File Upload

To upload files from your web browser, see instructions for file upload [here](../Describe-Experiments-and-Biosamples/#upload-files).

## Batch File Upload

Use DERIVA client tools for batch upload of files for a dataset.

### Organize your files

The upload application will scan a directory of your choice and identify the files for upload. It will process them according to rules based on the subdirectories it finds. Please organize your files as follows:

```
facebase/<dataset-RID>/...
```

Where `facebase` is a directory containing a subdirectory named `<dataset-RID>` according to the Dataset's Record ID (RID), e.g., `1-2345` found on your Dataset record page in the browser.

You may organize your files in any hierarchy _under the dataset RID_ directory. Recall that if you use a `local identifier` in your Biosample records, we may be able to assist with the automated linking of your files to your Biosample records.

#### Filename Conventions

The Deriva Upload utility will attempt to identify each file's format based on its filename extension. For example, TIFF images typically use the `.tif` or `.tiff` file extensions. To avoid ambiguity, we ask that you refrain from using the `.` character in the filename before the file extension. For example, the uploader currently does not support a file named `mm_het5.e15.tiff` because the file extension `.e15.tiff` or `.tiff` is ambiguous. It is okay to use `.` characters in a subdirectory name, however, such as `mm_het5.e15/image.tiff`. Also, you may use the web browser interface to upload your files with any naming convention including `.` characters because the web browser form does not attempt to automatically infer the file format. We are working to resolve this current limitation.

When using Deriva Upload, it attempts to match the filename extension to a known extension (see [Data Types and File Formats](../Data-Submission-Key-Concepts/#data-types-and-file-formats)). If the Deriva Upload encounters an unknown file extension, you will see an error such as this:

```
...
/path/to/facebase/1-2345/file.bad.extension.gz -- [RuntimeError] Metadata query did not return any results: /attribute/vocab:file_extension/extension=bad.extension.gz/vocab:file_format/file_format_id:=id?limit=1
...
```

If your filename complies with our [Filename Conventions](#filename-conventions), i.e., you do not have any extraneous `.` characters in the filename itself, then please contact [help](mailto:help@facebase.org) to request support for a new file format. Otherwise, consider replacing the `.` characters such as renaming `file.bad.extension.gz` to `file-bad-extension.gz` for the example given. Deriva Upload does support multi-part extensions such as `.nii.gz`, `.fastq.gz`, `.CEL.gz`, etc.

Finally, 'special characters' in your filenames such as `;`, `#`, spaces `' '`, and `$` will be encoded per Web standards. For more information, see [Percent-encoding (Wikipedia)](https://en.wikipedia.org/wiki/Percent-encoding).

### Install the DERIVA client tools

See the [Deriva Clients](../Deriva-Clients/) document for installation instructions.

What you install depends on your computer:

- **Windows**: an installer bundle that includes both a graphical desktop application called **DERIVA Upload** and a command-line application called `deriva-upload-cli`.
- **Linux**: a Python package that includes both **DERIVA Upload** and `deriva-upload-cli`.
- **macOS**: a Python package that includes `deriva-upload-cli`. The desktop application is not recommended for macOS users at this time; see [If you want the desktop application](../Deriva-Clients/#if-you-want-the-desktop-application) to check whether your Mac can run it.

If you are using **DERIVA Upload**, follow [Configure the DERIVA Upload app](#configure-the-deriva-upload-app). If you are using `deriva-upload-cli`, skip ahead to [Upload files with `deriva-upload-cli`](#upload-files-with-deriva-upload-cli).

### Configure the DERIVA Upload app

This section applies to the **DERIVA Upload** desktop application. It is available on Windows and Linux, and on Macs that can run the [installer bundle](../Deriva-Clients/#if-you-want-the-desktop-application). If you are using `deriva-upload-cli` instead, skip to [Upload files with `deriva-upload-cli`](#upload-files-with-deriva-upload-cli).

1. Open the DERIVA-Upload application.

2. First time use: you will be asked to "Add server configuration now?" Click **Yes**.

    ![Add server configuration]({{ "/assets/img/deriva-config-screen1.png" | relative_url }})

3. In the Server Configuration dialog enter host `www.facebase.org` and Catalog ID `1`. You may optionally add a Description `FaceBase`. Click **OK**.

    ![Add server configuration]({{ "/assets/img/deriva-config-screen2.png" | relative_url }})

4. From the Options dialog click **OK** again.

    ![Add server configuration]({{ "/assets/img/deriva-config-screen3.png" | relative_url }})

5. From the main window, click **Login** to begin your session.

    ![Add server configuration]({{ "/assets/img/deriva-config-screen4.png" | relative_url }})

### Upload files with DERIVA Upload

This section applies only to the **DERIVA Upload** desktop application (Windows, Linux, and Macs that can run the installer bundle).

![Upload Files Interactive]({{ "/assets/img/upload-files-interactive.png" | relative_url }})

1. Click **Browse** (upper right hand side)
    - Find and select the directory with the data files you organized.
    - Click **Open**.
2. Confirm that your files are all accounted for in the "Pending" state.
3. Click **Upload** (upper left hand side).
4. Confirm that the status of all of your files are now in the "Completed" state.

If there are any errors, they should be reported in the status panel beneath the file listing panel.

### Upload files with `deriva-upload-cli`

These steps apply to all platforms. They are the recommended method on macOS at this time.

- On **Windows**, the installer bundle adds an application called "DERIVA Command Line Applications". Running this application opens a terminal window with all DERIVA prerequisites and clients installed and ready to use.
- On **macOS** and **Linux**, open a terminal window as usual.

1. Establish an authentication token.

   ```commandline
   $ deriva-globus-auth-utils login --refresh --host www.facebase.org
   ```

   This opens a web browser. Log in with your usual FaceBase credentials, then return to the terminal window. You should see `Login Successful`. A token lasts roughly 48–72 hours, so you will need to repeat this step from time to time.

2. Upload the dataset files and save a copy of the output to a log file.

   ```commandline
   $ deriva-upload-cli www.facebase.org path/to/<dataset-RID> 2>&1 | tee upload.log
   ```

   The `| tee upload.log` portion writes everything the command prints to a file named `upload.log` in your current folder, while still showing it on screen. On Windows PowerShell, use `| Tee-Object upload.log` instead.

   We recommend always saving a log. If anything goes wrong, sending us `upload.log` is the fastest way for us to help.

3. Check the summary line near the end of the output. It reports how many files were uploaded, how many failed, and how many were skipped:

   ```
   File upload processing completed: 2 files were uploaded successfully, 0 files failed to upload due to errors, 0 files were skipped ...
   ```

Run the command with the `--help` option for more information on command-line options, and with the `--debug` option to produce more detailed output.

#### Warnings you can ignore

Some messages look like failures but are expected.

**Files you have already uploaded.** If your folder contains files that were uploaded in an earlier run, those files are reported as failures with a `409 CONFLICT` message about a duplicate key:

```
WARNING - The following 1 file(s) failed to upload due to errors:

/path/to/facebase/1-2345/image.jpg -- [DerivaUploadCatalogCreateError] [HTTPError] 409 Client Error: CONFLICT for url: ... duplicate key value violates unique constraint "file_url_key" ...
```

**This is normal and does not require action.** It means the file is already stored in FaceBase and was not uploaded again. Any new files in the folder still upload normally — check the summary line to confirm. You will also see a final line such as `[RuntimeError] 1 file(s) failed to upload due to errors.`, which refers to the same thing.

**An OpenSSL warning on macOS.** A message beginning with `NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+` may appear at the top of the output. It is harmless and does not affect your upload.

If you see any other errors, please send an email to [help@facebase.org](mailto:help@facebase.org) and attach your `upload.log` file.

## Review the uploaded files

Return to the FaceBase site to your Dataset record. Scroll down to the File section. For each file, click the 'edit' icon (pencil), go to the Biosample field, click the drop-down, find the Biosample associated with the file (e.g., the file is an image of a specific biological sample), select the Biosample, update or confirm the rest of the File attributes, and click **Save**.

#### Display of thumbnails

If you uploaded thumbnails and want them to appear on the main page of your dataset, find the thumbnail record, edit it, and set the *Show In Dataset* attribute to "True".

#### Display of surface models

If you uploaded 3D model mesh objects (.obj.gz) and you want to display a 3D model on the dataset page, follow the instructions for [defining surface models](../Define-Surface-Model/).

#### Display of Genome Browser tracks

If you uploaded genome browser track data and you want to display your tracks on the dataset page:

1. Go to your dataset.
2. Find the *Genome Browser* subsection and click **Add record**.
3. In the form, select the **Mapping Assembly** (required).

We highly recommend entering a chromosome name (e.g., `chr1`) along with start and end positions. The browser will then display by default at that location. The user will be able to change the browser position from its default position as desired.
