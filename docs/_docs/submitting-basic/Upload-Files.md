---
title: Uploading Data Files
permalink: /docs/Upload-Files/
---

There are two ways to upload files:

- **Interactive**: upload files individually from your web browser (recommended for smaller datasets).
- **Batch**: upload files in a batch using command-line utilities or desktop applications (recommended for large volumes of data).

**IMPORTANT**: Do NOT upload _Human Subjects_ data using these procedures described below. Please contact [FaceBase Help](mailto:help@facebase.org) for more information.

## Before You Begin

You must first [create a dataset](../Create-a-Dataset/) and [describe the experiments, biosamples, and replicates](../Describe-Experiments-Biosamples-and-Replicates/) used for that dataset. Once you have completed those steps you may upload data files.

## Interactive File Upload

To upload files from your web browser:

1. Go to a **Replicate** record (to find Replicate records, go to the Dataset, select the Experiment and then you'll see a listing of Replicates for that Experiment). You will see sections for various data types such as: sequencing, processed, track, imaging, and/or mesh data files.
2. For the data type section related to your data, click the **Add Record** button. A new browser tab opens with the data entry form.
3. In the "Url" field, click the **Select file** button to select the data file.
4. In the "File Type" field, click the field to open the "Select File Type" modal window. Find the appropriate extension under the "Name" column and select it.
5. When you are finished, click **Save** to upload the file.

Repeat for each file you want to upload.

## Batch File Upload

Use DERIVA client tools for batch upload of files for a dataset.

### Organize your files

The upload application will scan a directory of your choice and identify the files for upload. It will process them according to rules based on the subdirectories it finds them in. Please organize your files as follows:

```
<dataset-RID>/<replicate-RID>/
    seq/
        raw sequencing files (.fastq.gz)
    proc/<mapping-assembly>/
        processed data (.bam, .bam.bai, .count, .tsv, .fastqc{.tgz|.zip})
        track data (.bed, .bb, .bw)
    img/
        high-resolution imaging data (.nii.gz, .ome.tif[f], .aim, .tif[f], .jp[e]g)
    mesh/
        3D model mesh objects (.obj.gz)
    thumb/<derived-from>/
        low-resolution "thumbnail" images (.jp[e]g, .png)
    array/
        microarray data (.CEL.gz)
```

Where:
- `<dataset-RID>` is the Dataset's Record ID (RID), e.g., `1-BBC4`
- `<replicate-RID>` is the Replicates's Record ID (RID), e.g., `1-BBCA`
- `<mapping-assembly>` is the reference genome mapping assembly, i.e., `mm9`,
    `mm10`, `hg18`, `hg19`
- `<derived-from>` is a directory using the _exact_ same name as a filename
    _including file extension_ from your raw images under the `img` directory,
    e.g., `.../my-confocal-image.ome.tiff/...`.

**NOTE**: If you use 'special characters' in your filenames such as `;`, `#`, 
spaces `' '`, and `$` the special characters will be encoded per Web standards. 
For more information, see this [Wikipedia article on Percent-encoding](https://en.wikipedia.org/wiki/Percent-encoding).

The following figure is an example of the directory structure for a dataset 
ready for upload.

![File Organization]({{ "/assets/img/upload-files-organize.png" | relative_url }})

### Install the DERIVA client tools

See the [Deriva Clients](../Deriva-Clients/) document for installation instructions. 
This installer includes both a graphical desktop application called **DERIVA Upload**
and a command-line interface called **deriva-upload-cli**.

### Configure the DERIVA Upload app

This section applies only to the DERIVA Upload desktop application.

1. Open the DERIVA-Upload application.
2. First time use: you will be asked to "Add server configuration now?" Click **Yes**.

    ![Add server configuration]({{ "/assets/img/deriva-config-screen1.png" | relative_url }})

3. In the Server Configuration dialog enter host `www.facebase.org` and Catalog ID `1`. You may optionally add a Description `FaceBase`. Click **OK**.

    ![Add server configuration]({{ "/assets/img/deriva-config-screen2.png" | relative_url }})

4. From the Options dialog click **OK** again.

    ![Add server configuration]({{ "/assets/img/deriva-config-screen3.png" | relative_url }})

5. From the main window, click **Login** to begin your session.

    ![Add server configuration]({{ "/assets/img/deriva-config-screen4.png" | relative_url }})


### Upload files DERIVA Upload

![Upload Files Interactive]({{ "/assets/img/upload-files-interactive.png" | relative_url }})

1. Click **Browse** (upper right hand side)
    - Find and select the directory with the data files you organized.
    - Click **Open**.
2. Confirm that your files are all accounted for in the "Pending" state.
3. Click **Upload** (upper left hand side).
4. Confirm that the status of all of your files are now in the "Completed" state.

If there are any errors, they should be reported in the status panel beneath the file listing panel.

### Upload files with `deriva-upload-cli`

If you installed the DERIVA Clients you will find an application called "DERIVA Command Line Applications".
Running this application will open a terminal window with all DERIVA prerequisites and clients installed 
and ready to use.

1. Establish an authentication token.
   ```commandline
   $ deriva-globus-auth-utils login --refresh --host www.facebase.org
   ```
2. Upload files for a dataset.
    ```commandline
    $ deriva-upload-cli www.facebase.org path/to/<dataset-RID>
    ```

Errors will be reported to the standard output or error. Please send email to [help@facebase.org](mailto:help@facebase.org) and 
include any listed errors. Run the command with the `--debug` option to provide additional details. Use the
`--help` option for more information on command-line options.

## Review the uploaded files

Return to the FaceBase site to your Dataset record. Drill down through the Experiments
and Replicates in order to see the data files that you have uploaded. Make sure that
their metadata are correct. For example, if you uploaded raw sequencing files, make sure 
that the "paired" and "read" attributes are correct in the metadata seen on the site. If 
they are incorrect, click the 'edit' icon (pencil), correct the attribute(s), and click **Save**.

#### Display of thumbnails

If you uploaded thumbnails, and you want those thumbnails to appear on the main page
of your dataset, find the thumbnail record, edit it, and set the *Show In Dataset*
attribute to "True".

#### Display of surface models

If you uploaded 3D model mesh objects (.obj.gz) and you want to display a 3D model on
the dataset page, follow the instructions for [defining surface models](../Define-Surface-Model/).

#### Display of Genome Browser tracks

If you uploaded genome browser track data and you want to display your tracks on the
dataset page:

1. Go to your dataset.
2. Find the *Genome Browser* subsection and click **Add record**.
3. In the form, select the **Mapping Assembly** (required).

We highly recommend entering a chromosome name (`chr1`, etc.) and a start and end position. The browser will then display by default at that loci. The user will be able to change the browser position from the default position as they desire.
