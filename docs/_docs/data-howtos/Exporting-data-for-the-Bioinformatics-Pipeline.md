---
title: Exporting data for the Bioinformatics Pipeline
permalink: /docs/Exporting-data-for-the-Bioinformatics-Pipeline/
---

For complete information on downloading data from FaceBase, please see [our Exporting doc](./Exporting-Data-from-FaceBase).

The following instructions are specific to using the Bioinformatics Pipeline.

## Bulk Download of Sequencing Data

Bulk download of data from FaceBase is primarily supported by the "Export -> BAG"
functionality on the FaceBase site. The instructions provided here are intended
only for bulk download of sequencing data as required by the Hub and our partners
that operate the Bioinformatics Pipeline.

With these instructions, you may download all of the raw sequencing data files
(fastq) for RNA-seq and ChIP-seq experiments, on a per dataset basis.

1. You must have a FaceBase User account
    - Go to [FaceBase](www.facebase.org) and sign up
2. Install the client tools. See [Deriva Clients](./Deriva-Clients).
    - Install DERIVA-Auth on your desktop computer
    - Install DERIVA Python (deriva-py) on the computer where you want to download the files to.
3. Establish an authentication token. See [Authentication Tokens](./Deriva-Clients#Authentication-Tokens).
4. Download a copy of the [fb-seq-bag.json download specification](./fb-seq-bag.json)
    - If you want to do a _dry run_ before really downloading an entire dataset,
    open the `fb-seq-bag.json` file and search-replace `"download"` with `"fetch"`
    - When you run the download client in the next step it will create a 'fetch'
    file that lists the files _to be downloaded_ but will not actually download
    them
5. Pass the cookie during your cURL request to access files.
    ```
    $ deriva-download-cli www.facebase.org fb-seq-bag.json <output-dir> dataset=<dataset_RID>
    ```
    - where `<output-dir>` is the directory under which the downloaded files will be stored
    - and where `<dataset_RID>` is the dataset "RID" (e.g., 'TMJ')
