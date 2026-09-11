---
title: Creating Biosamples and Experiments
permalink: /docs/Describe-Experiments-and-Biosamples/
---

If you have [created a Dataset](../Create-a-Dataset/), you are ready to describe the biosamples and experiments in it.

## Which path does my data take? {#which-path}

Not all assay types are entered the same way. Find your data in the table below before you start.

| If your dataset contains | How to enter it |
| --- | --- |
| Sequencing, array, imaging, or microscopy data — RNA-seq, ChIP-seq, arrays, micro-CT, confocal, and similar | Follow the [four steps](#the-four-steps) on this page. These assays have data files, and files attach to biosamples, so biosamples are created first. |
| Clinical assays or enhancer reporter assays | Create the record directly from the Dataset page. See [Clinical and enhancer reporter records](#other-assay-types). No separate biosample or experiment record is needed. |

### Key terms

**Biosamples** represent the biological characteristics of the specimen used within an experiment. Typically, each experiment includes multiple biological samples with essentially the same biological characteristics (e.g., biological replicates).

> **Note:** FaceBase does not collect tissue or other physical samples. The biosamples described here are *metadata* about the physical samples you used in your experiments.

**Experiments** (also known as **assays**) represent an experiment at a fine-grained unit of detail. The record type broadly covers both "bioinformatics" (sequencing or array) and imaging (various forms of microscopy) assay types. An experiment is generally conducted on multiple biological replicates, and may reference another experiment as its control.

**Local identifiers** let you reference your own laboratory's identification schema for your experiments and biosamples. Both forms include a "Local Identifier" field. These are useful for correlating FaceBase entries with your own records — for example, if someone using your data has a question, you can look the item up in your own records. They are also what we use to match your files to your biosamples if you ask us to automate that step.

### The four steps {#the-four-steps}

All of the instructions that follow assume you are [logged in to the FaceBase site](../Data-Submission-Process/#prerequisites-for-submitting-data).

1. [Create biosamples](#create-biosamples) to describe the biological samples in your study.
2. [Upload files](#upload-files) — in batch with the DERIVA client tools, or one at a time through the browser.
3. [Link files to their biosamples](#link-files) so each file is associated with the sample it came from.
4. [Create experiments](#create-experiments) to describe the experimental details, and link each biosample to its experiment.

## Step 1. Create biosamples {#create-biosamples}

1. Go to the Dataset record.
2. Scroll down the page to find the *Biosample* section.
    - If you do not see the *Biosample* section, click the *Show empty sections* link near the top right of the page.
3. To the right of the *Biosample* heading, click the *Add Record* button. A new browser tab opens with the data entry form.

  ![Add Biosample]({{ "/assets/img/add-biosample.png" | relative_url }})

  ![Biosample Form]({{ "/assets/img/biosample-form.png" | relative_url }})

4. Fill in the form as completely as possible for the fields relevant to your data. Leave the "Experiment" field blank — you will fill it in at [Step 4](#create-experiments), after your experiment records exist.
5. When you are done, click the *Save* button in the upper right corner.
6. Review the confirmation page that displays the entered data.
7. Close the browser tab and return to the Dataset page. You should now see the newly entered biosample. You may need to refresh the page.

### Entering several biosamples at once {#multi-record-entry}

You do not have to enter records one at a time. This also works for File and Experiment records.

1. From an existing record page, click the *Copy* button near the upper right. A new form opens with the same values as the record you copied.
2. Click the *Clone* button in the upper right to add another data entry form each time you click. To add several at once, type a number in the field beside *Clone* before clicking. You can expand the form to up to 200 records at a time.

Each new form inherits the values of the right-most existing form. Use this to your advantage: fill in the fields that are shared across records first, click *Clone* as many times as you need, then fill in the values unique to each record.

![Multiple Record Edit]({{ "/assets/img/biosample-multi-edit.png" | relative_url }})

Nothing is saved until you click *Save*. The entire form succeeds or fails as a single unit — there are no partial submissions.

## Step 2. Upload files {#upload-files}

Once your biosample records exist, you are ready to [upload files](../Upload-Files/). Choose one of the two options below.

### Option 1: Batch upload with the DERIVA client tools

Recommended for anything more than a handful of files. See the [uploading files](../Upload-Files/) page for installation and usage instructions. After the upload finishes, continue to [Step 3](#link-files) to associate the files with their biosamples.

### Option 2: Upload through the browser

Best for a small number of files.

1. From the Dataset page, scroll to the *Biosample* section and click the *View Details* icon for the biosample you want, then scroll down to the *File* section.
2. Click the *Add Record* button. A new browser tab opens with the data entry form.
3. In the "Url" field, click the *Select file* button and choose your data file.
4. Click the "File Format" field to open the "Select File Format" modal. Find the appropriate extension under the "Name" column and select it.
5. Click *Save* to upload the file.

Because you started from the biosample record, files uploaded this way are already associated with that biosample and you can skip [Step 3](#link-files).

## Step 3. Link files to their biosamples {#link-files}

Files uploaded with the DERIVA client tools arrive in the dataset unassociated. This step tells FaceBase which biosample each file belongs to.

1. Go back to the Dataset page and scroll down to the *File* section.
2. Narrow the list to the files for one biosample, by clicking the *Explore* button and using the search box above the table or the filters in the left sidebar. Searching on the portion of the filename that matches that sample — often the [local identifier](#which-path) — is usually the fastest way.
3. Click the *Bulk Edit* button.
4. On the left side of the screen, find the "Biosample" field and click the pencil icon.
5. Click the "Select a value" dropdown, choose the correct biosample record, and click *Save*.

Repeat for each remaining biosample.

> **Working with a lot of files?** We can do Steps 2 and 3 for you. Send us a spreadsheet mapping your biosamples' [local identifiers](#which-path) to your filenames and we will handle the upload and the associations. Contact us at [help@facebase.org](mailto:help@facebase.org).

## Step 4. Create experiments {#create-experiments}

Create an experiment record if you are entering RNA-seq, ChIP-seq, array, imaging (micro-CT), or microscopy (confocal) data. The form covers a wide range of experiment types, so in many cases you will fill in only a small number of fields — sometimes only one or two.

1. From the Dataset record, scroll down to the *Experiment* section.
    - If you do not see the *Experiment* section, click the *Show empty sections* link near the top right of the page.
2. To the right of the heading, click the *Add Record* button. A new browser tab opens with the data entry form.

![Add Experiment]({{ "/assets/img/add-experiment.png" | relative_url }})

![Experiment Form - Sequencing]({{ "/assets/img/experiment-form-seq.png" | relative_url }})

3. Fill in the form as completely as possible for the fields relevant to your data. The example above shows a hypothetical RNA-seq experiment; many fields are left blank because they do not apply to that experiment type.
4. Link the experiment to a protocol. See [Linking an experiment to a protocol](#link-protocol) below.
5. Click *Save*. You will see the newly entered experiment information.

### Link each biosample to its experiment {#link-biosamples-to-experiments}

Now that your experiment records exist, go back and fill in the field you left blank in Step 1.

1. From the Dataset page, open the *Biosample* section.
2. For each biosample, click the *Edit* icon in the list — or open the biosample record and click *Edit*.
3. Click the "Experiment" dropdown and choose the experiment the sample belongs to.
4. Click *Save*.

### Linking an experiment to a protocol {#link-protocol}

On the experiment form, click the "Protocol" field to open the "Select Protocol" modal.

![Link Experiment to Protocol]({{ "/assets/img/link-experiment-to-protocol.png" | relative_url }})

From there you can either:

- **Select an existing protocol.** Search for a protocol already in the system and select it.
- **Create a new protocol.** Click the *Create New* button. A new browser tab opens, where you can:
    - Fill in the fields with the protocol information for online display,
    - Enter a link to an existing online source in the "Protocol Uri" field, or
    - Upload a file (PDF, Word document, etc.) by clicking *Select File* at the "File Url" field.

    Click *Save* to see the information you entered, then close the tab and return to the "Select Protocol" modal to select the protocol record you just created.

![Create Protocol]({{ "/assets/img/create-protocol.png" | relative_url }})

## Clinical and enhancer reporter records {#other-assay-types}

Clinical assays and enhancer reporter assays are entered directly on the Dataset record and do not use the four-step workflow above.

1. Go to the Dataset record.
2. Scroll down to the *Enhancer Reporter Assay* or *Clinical Assay* section and click the *Add Record* button. A new browser tab opens with the data entry form.
3. Fill in the details as completely as possible and click *Save*.

## What happens next

When your biosamples, files, and experiments are entered and linked, review your dataset record for completeness and then [email us to let us know it is ready for review at help@facebase.org](mailto:help@facebase.org).
