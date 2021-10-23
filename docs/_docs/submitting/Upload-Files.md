---
title: Upload Data Files
permalink: /docs/Upload-Files/
---

You must first [create a dataset](../Create-a-Dataset/) and [describe the experiments, biosamples, and replicates](../Describe-Experiments-Biosamples-and-Replicates/) used for that dataset. Once you have completed those steps you may upload data files.

In general, the steps to follow are:
1. Organize your files into a specific directory hierarchy.
2. Use one of our desktop or command-line upload tools.

**IMPORTANT**: Do NOT upload _Human Subjects_ data using the procedures described below. Human subjects data are uploaded to FaceBase using a different procedure. Please contact [FaceBase Help](mailto:help@facebase.org) for more information.

## Uploading from the Data Browser

We do support the ability to upload data from the browser. This is sufficient when it's not a large number of files and they're not that large (less than 1 GB each). In general, we recommend using the desktop or command-line upload tools. But if you prefer, here is how to upload data from the browser:

1. Go to the Replicate record (to find Replicate records, go to the Dataset, select the Experiment and then you'll see a listing of Replicates for that Experiment). You will see sections for various data types such as: sequencing, processed, track, imaging, and/or mesh data files.
2. For the data type section related to your data, click the _Add Record_ button. A new browser tab opens with the data entry form.
3. In the "Url" field, click the _Select file_ button to select the data file.
4. In the "File Type" field, click the field to open the "Select File Type" modal window. Find the appropriate extension under the "Name" column and select it.
5. When you are finished, click _Submit_ to upload the file.

## Organize your files

The upload application will scan a directory of your choice and identify the files for upload. It will process them according to rules based on the subdirectories it finds them in. Please organize your files as follows:

```
<dataset>/<replicate>/
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
- `<dataset>` is the Dataset's Record ID (RID), e.g., `1-BBC4`
- `<replicate>` is the Replicates's Record ID (RID), e.g., `1-BBCA`
- `<mapping-assembly>` is the reference genome mapping assembly, i.e., `mm9`,
    `mm10`, `hg18`, `hg19`
- `<derived-from>` is a directory using the _exact_ same name as a filename
    _including file extension_ from your raw images under the `img` directory,
    e.g., `.../my-confocal-image.ome.tiff/...`.

**NOTE** it is generally advised to avoid _special characters_ in your filenames like
`;`, `#`, spaces `' '`, `$`, etc. These have to be converted into what is known as
"percent-encodings" per the Web standards. In general, we believe we are able to support
special characters, but this can be a source of confusion and errors at times. For
more information, see this [Wikipedia article on Percent-encoding](https://en.wikipedia.org/wiki/Percent-encoding).

Here is an example of the directory layout.

![File Organization]({{ "/assets/img/upload-files-organize.png" | relative_url }})

## Install the DERIVA clients
See the [Deriva Clients](../Deriva-Clients/) document for installation instructions.

## Configure the DERIVA Upload Utility (DERIVA-Upload)

1. Open the DERIVA-Upload application.
2. First time use: you will be asked to "Add server configuration now?" Click "Yes".

    ![Add server configuration]({{ "/assets/img/deriva-config-screen1.png" | relative_url }})

3. In the Server Configuration dialog enter host `www.facebase.org` and Catalog ID `1`. You may optionally add a Description `FaceBase`. Click "OK"

    ![Add server configuration]({{ "/assets/img/deriva-config-screen2.png" | relative_url }})

4. From the Options dialog click "OK" again.

    ![Add server configuration]({{ "/assets/img/deriva-config-screen3.png" | relative_url }})

5. From the main window, click "Login" to begin you session.

    ![Add server configuration]({{ "/assets/img/deriva-config-screen4.png" | relative_url }})


## Upload files with DERIVA Upload Utility (DERIVA-Upload)

![Upload Files Interactive]({{ "/assets/img/upload-files-interactive.png" | relative_url }})

1. Open the DERIVA-Upload application
1. Click Login (upper right hand side)
    - This uses your usual FaceBase username and password
4. Click Browse (upper right hand side)
    - Find the directory
    - Select it
    - Click Open
5. Confirm that your files are all accounted for in the "Pending" state.
6. Click Upload (upper left hand side)
7. Confirm that the status of all of your files are now in the "Completed" state.

If there are any errors, they should be reported in the status panel beneath the file listing panel.

## Upload your files with a command-line interface

1. Establish an authentication token. See [Authentication Tokens](../Deriva-Clients/#Authentication-Tokens).
2. Get familiar with the `deriva-upload-cli` options:
    ```
    $ deriva-upload-cli --help
    ```
3. From the command-line of your host, you will run a command like this:
    ```
    $ deriva-upload-cli --token <your-auth-token> www.facebase.org path/to/<dataset-RID>
    ```
5. Errors will be reported to the standard output or error. Please include them in any email to the Hub.

## Review the uploaded files

Return to the FaceBase site to your Dataset record. Drill down through the Experiments
and Replicates in order to see the data files that you have uploaded. Make sure that
their metadata are correct. For example, if you uploaded raw sequencing files, make sure
that the "paired" and "read" attributes are correct in the metadata seen on the site.
If they are incorrect, click the 'edit' icon, correct the attribute, and 'Submit' the
updated record.

### Display of thumbnails

If you uploaded thumbnails, and you want those thumbnails to appear on the main page
of your dataset, find the thumbnail record, edit it, and set the "Show In Dataset"
attribute to "True".

### Display of surface models

If you uploaded 3D model mesh objects (.obj.gz) and you want to display a 3D model on
the dataset page, follow the instructions to [define surface models](../Define-Surface-Model/).

### Display of Genome Browser tracks

If you uploaded genome browser track data and you want to display your tracks on the
dataset page, go to your dataset. Find the "Genome Browser" subsection, click "Add record". In the form, select the Mapping Assembly (required). We highly recommend entering a chromosome name (`chr1`, etc.) and a start and end position -- the browser will then display by default at that loci. The user will be able to change the browser position from the default position as they desire.
