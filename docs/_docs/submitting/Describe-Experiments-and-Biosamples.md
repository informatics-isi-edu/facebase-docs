---
title: Creating Experiments and Biosamples
permalink: /docs/Describe-Experiments-and-Biosamples/
---

If you have [created a Dataset](../Create-a-Dataset/) then you are ready to
describe the experiments and biosamples for your dataset.

**Experiments** (also known as **assays**) represent an experiment at a fine-grained unit of detail. It is intended to broadly cover multiple "bioinformatics" (i.e., sequencing or array) and imaging (i.e., various forms of microscopy) assay types. An experiment will generally be conducted on multiple biological replicates. An experiment may reference another experiment as its "control."

**Biosample** records in the database represent the biological characteristics of the specimen used within an Experiment. Typically, each experiment will include multiple biological samples with essentially the same biological characteristics (e.g., biological replicates).

All of the instructions that follow assume you are [logged in to the FaceBase site](../Data-Submission-Process/#prerequisites-for-submitting-data).

The main steps are:
1. [Create experiments](#1-create-experiments) to describe the experimental details of the study.
2. [Create biosamples](#2-create-biosamples) to describe the biological samples for the study.
3. [Upload files](#3-upload-files) associated with specific biosamples.

## What are Local Identifiers?

You will notice that the biosample and the experiment forms have fields for entering a *Local Identifier*. Local identifiers provides a way to reference your own laboratory's local identification schema for your experiments and biosamples. This can be useful for correlating FaceBase data entries with your own records. For example, if a user of your data has a question, you may be able to use these local identifiers as a means of looking up items from your own records.

## 1. Create Experiments

Create an experiment record if you are entering RNA-seq, ChIP-seq, array, imaging
(micro-CT), or microscopy (confocal) experiments. Because the form covers a wide
range of experiment types, in many cases you will only fill in a small (sometimes
only 1-2) number of fields.

1. Go to the Dataset record
2. Scroll down the page to find the _Experiment_ section.
    - If you do not see the _Experiment_ section, click the 'Show All Related Records'
      link near the top right of the page.
3. To the right of the heading, click the _Add Record_ button. This will open a new browser tab with the data entry form.

![Add Experiment]({{ "/assets/img/add-experiment.png" | relative_url }})

![Experiment Form - Sequencing]({{ "/assets/img/experiment-form-seq.png" | relative_url }})

4. Fill in the form as completely as possible for the fields relevant to your data.
    The example above shows a hypothetical RNA-seq experiment. Note that many fields
    are left blank because they are not relevant to this experiment type.

5. To link your Experiment to a protocol, click the Protocol field to display the "Select Protocol" modal window.

![Link Experiment to Protocol]({{ "/assets/img/link-experiment-to-protocol.png" | relative_url }})

From here you can:

- Search for a protocol that is already in the system and select it.
- Click the _Create New_ button to add a protocol to the system and then select it. This will open a new browser tab. Your choices for adding a new protocol are:
    - Fill in the fields with the protocol information for online display.
    - Enter a link to an existing online source in the "Protocol Uri" field.
    - Upload a file (PDF, Word doc, etc) by clicking "Select File" at the "File Url" field.
    - When you are done, click the _Submit_ button and you will see the information you entered. You can then close this browser tab and go back to the "Select Protocol" modal window to select the Protocol record you just entered.

    ![Create Protocol]({{ "/assets/img/create-protocol.png" | relative_url }})

6. When you are finished entering the Experiment information, click on the _Submit_ button and you will see the newly entered Experiment information.

## 2. Create Biosamples

Enter metadata regarding the biosamples in your dataset. *FaceBase does not collect
tissue or other physical samples. The 'biosamples' here are metadata to describe the
physical samples you used in your experiments only.*

1. Go to an Experiment record page.
    - Do not use the _edit_ mode of the page; remain on the display page.
2. Scroll down the page to find the _Biosample_ section.
    - If you do not see the _Biosample_ section, click the _Show All Related Records_
      link near the top right of the page.
3. To the right of the _Biosample_ heading, click the _Add Record_ button. This will open a new browser tab with the data entry form.

  ![Add Biosample]({{ "/assets/img/add-biosample.png" | relative_url }})

  ![Biosample Form]({{ "/assets/img/biosample-form.png" | relative_url }})

4. Fill in the form as completely as possible for the fields relevant to your data.
5. When you are done, click the _Submit_ button in the upper right corner.
6. Review the confirmation page that displays the entered data.
7. When you are done viewing the confirmation page, close the browser tab and
    return to the Dataset page. You should now see the newly entered Biosample. You may need to refresh your browser page.

### Entering multiple records (multi-edit)

You can choose to enter multiple records at a time. From a record page, click the _Copy_ button near the upper right side of the page. A new form appears with the same values as the record you copied.

Click the _Clone_ button in the upper right corner to expand a new data entry form each time you click.

You can also enter the number of copies in the number field before clicking _Clone_ to create that number of new data entry forms. You can expand the form with up to 200 records at a time.

Note that when you click Clone, the new data entry form will include any values from the right-most existing form. You can use this to streamline data entry by filling in some fields that are shared by multiple entries, pressing the _Clone_ button multiple times, then filling in the unique field values for each record on the page.

![Multiple Record Edit]({{ "/assets/img/biosample-multi-edit.png" | relative_url }})

No matter how many entries you add, the form will not be saved to the system until you click the _Submit_
button. Note that the entire form with all records will succeed or fail to be
submitted as one unit. There are no partial successes when submitting multiple
records.


## 3. Upload Files

When you have created your Biosample records, you are now ready to
[upload files](../Upload-Files/). There are two options for uploading files:
1. Use the bulk upload utilities described on the
    [uploading files](../Upload-Files/) page of this wiki. Note that if you use the bulk uploader you will still need to return to the web browser and associate each file with a biosample (if applicable). If you have a large number of biosamples and files, we can help automate the process as long as you have a spreadsheet that documents the mapping from your biosamples' [local identifiers](#what-are-local-identifiers) to your filenames.
2. Go to each Biosample page, add records for each file and upload via the browser. (To find Biosample records, go to the Dataset, select the Experiment and then you'll see a listing of Biosamples for that Experiment).
    1. Go to the Biosample record and you'll see the File section.
    2. Click the _Add Record_ button. A new browser tab opens with the data entry form.
    3. In the "Url" field, click the _Select file_ button to select the data file.
    4. In the "File Format" field, click the field to open the "Select File Format" modal window. Find the appropriate extension under the "Name" column and select it.
    5. When you are finished, click _Submit_ to upload the file.

## 4. Creating records for other assay types

To enter _clinical_ assays and _enhancer_ records, you can add them
from the Dataset record.

1. Go to the Dataset record.
2. Scroll down to the "Enhancer Reporter Assay" or "Clinical Assay" section and click the _Add record_ button. A new browser tab opens with the data entry
3. Fill in the details as completely as possible and click _Submit_.

## Review your entries

When you have reviewed your biosample, experiment, and/or other metadata, you are
ready to [upload files](../Upload-Files/).
