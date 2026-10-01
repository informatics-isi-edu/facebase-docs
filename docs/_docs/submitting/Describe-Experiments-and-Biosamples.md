---
title: Creating Biosamples and Experiments
permalink: /docs/Describe-Experiments-and-Biosamples/
---

If you have [created a Dataset](../Create-a-Dataset/), you are ready to describe the biosamples and experiments in it.

## Which path does my data take? {#which-path}

Not all assay types are entered the same way. Find your data in the table below before you start.

| If your dataset contains | How to enter it |
| --- | --- |
| Clinical assays, or sequencing, array, imaging, or microscopy data — RNA-seq, ChIP-seq, micro-CT, confocal, and similar | Follow the [five steps](#the-five-steps) on this page. These assays have data files, and files attach to biosamples, so biosamples come first. |
| Enhancer reporter assays | Create the record directly from the Dataset page. See [Enhancer reporter records](#enhancer-records). No separate biosample or experiment record is needed. |

### Key terms {#key-terms}

**Biosamples** represent the biological characteristics of the specimen used within an experiment. Typically, each experiment includes multiple biological samples with essentially the same biological characteristics (e.g., biological replicates).

> **Note:** FaceBase does not collect tissue or other physical samples. The biosamples described here are *metadata* about the physical samples you used in your experiments.

**Experiments** (also known as **assays**) represent an experiment at a fine-grained unit of detail. The record type broadly covers both "bioinformatics" (sequencing or array) and imaging (various forms of microscopy) assay types. An experiment is generally conducted on multiple biological replicates, and may reference another experiment as its control.

**Local identifiers** let you reference your own laboratory's identification schema for your experiments and biosamples. Both forms include a "Local Identifier" field. These are useful for correlating FaceBase entries with your own records. For example, if someone using your data has a question, you can look the item up in your own records. They are also key to matching your files to your biosamples.

### The five steps {#the-five-steps}

All of the instructions that follow assume you are [logged in to the FaceBase site](../Data-Submission-Process/#prerequisites-for-submitting-data).

1. [Create biosamples](#create-biosamples) to describe the biological samples in your study.
2. [Upload files](#upload-files) — in batch with the DERIVA client tools, or one at a time through the browser.
3. [Link files to their biosamples](#link-files) so each file is associated with the sample it came from.
4. [Create experiments](#create-experiments) to describe the experimental details, and link each biosample to its experiment.
5. [Link a protocol](#link-protocol) to document how the experiment was performed.

![A diagram of the five steps in order: create biosamples, upload files, link files to biosamples, create experiments, and link a protocol.]({{ "/assets/img/submission-workflow.svg" | relative_url }}){: .img-responsive}

>**Tip:** Use the Sections panel on the left to jump straight to a section instead of scrolling. The number beside each name tells you how many records it holds. If a section isn't listed, click *Show empty sections* at the top right. The sections don't appear in the order you'll work through them, so use the panel rather than working top to bottom.

{% include screenshot.html src="/assets/img/example-sections-sidebar.png" full="/assets/img/example-sections-sidebar-full.png" alt="Part of the Sections panel on a Dataset page, listing sections with their record counts. The Experiment, Biosample, and File sections are outlined in red." width=691 %}

*Click the image to see the full Sections panel.*

## Step 1. Create biosamples {#create-biosamples}

1. Go to the Dataset record.
2. Go to the *Biosample* section.
    - If you do not see the *Biosample* section, click the *Show empty sections* button near the top right of the page.
3. To the right of the *Biosample* heading, click the *Add records* button. A new browser tab opens with the data entry form.

   {% include screenshot.html src="/assets/img/biosample-add-records.png" alt="The Biosample section of a Dataset page, with the Add records button outlined in red." width=2402 %}

   {% include screenshot.html src="/assets/img/biosample-form.png" alt="The Create 1 Biosample record form, with the Dataset field already filled in and grayed out." width=2000 %}

4. Fill in the form as completely as possible for the fields relevant to your data. Leave the "Experiment" field blank — you will fill it in at [Step 4](#create-experiments), after your experiment records exist. Note: The Dataset field is filled in automatically because you started from the Dataset page.
5. When you are done, click the *Save* button in the upper right corner.
6. Review the confirmation page that displays the entered data.
7. Close the browser tab and return to the Dataset page. You should now see the newly entered biosample. You may need to refresh the page.

### Entering several biosamples at once {#multi-record-entry}

You do not have to enter records one at a time. The following method also works for File and Experiment records.

1. From an existing record page, click the *Copy* button near the upper right. A new form opens with the same values as the record you copied.
2. Click *Clone* to add another record to the form. Each click adds one record. To add several at once, enter a number in the *Qty* box before clicking *Clone*. For example, starting from one record, you can click *Clone* twice, or enter 2 in *Qty* and click *Clone* once. Either way, you end up with three records, as shown below. The form can hold up to 200 records at a time.

>**Tip:** Each new form inherits the values of the right-most existing form. Use this to your advantage: fill in the fields that are shared across records first, click *Clone* as many times as you need, then fill in the values unique to each record.

{% include screenshot.html src="/assets/img/biosample-multi-edit.png" alt="The Create 3 Biosample records form with three records side by side, and the Qty box set to 2 next to the Clone button, outlined in red." width=2904 zoom=true %}

*Click the image to see it full size.*

Nothing is saved until you click *Save*. The entire form succeeds or fails as a single unit — there are no partial submissions.

## Step 2. Upload files {#upload-files}

Once your biosample records exist, you are ready to [upload files](../Upload-Files/). Choose one of the two options below.

### Option 1: Batch upload with the DERIVA client tools

Recommended for anything more than a handful of files. See the [uploading files](../Upload-Files/) page for installation and usage instructions. After the upload finishes, continue to [Step 3](#link-files) to associate the files with their biosamples.

### Option 2: Upload through the browser

Best for a small number of files.

1. From the Dataset page, scroll to the *Biosample* section and click the *View Details* icon for the biosample you want, then scroll down to the *File* section.
2. Click the *Add records* button. A new browser tab opens with the data entry form.
3. In the "URL" field, click the *Select file* button and choose your data file.
4. Click the "File Format" field to open the "Select File Format" window. Find the appropriate extension under the "Name" column and select it.
5. Click *Save* to upload the file.

Because you started from the biosample record, these files are already associated with it and you can skip [Step 3](#link-files).

## Step 3. Link files to their biosamples {#link-files}

Files uploaded with the DERIVA client tools arrive in the dataset unassociated. This step tells FaceBase which biosample each file belongs to.

1. Go back to the Dataset page and scroll down to the *File* section.
2. Narrow the list to the files for one biosample by clicking the *Explore* button and using the search box above the table, or the filters in the left sidebar (click *Show filter panel* if they're hidden). Searching on the portion of the filename that matches that sample — often the [local identifier](#key-terms) — is usually the fastest way.

   {% include screenshot.html src="/assets/img/explore-files.png" alt="The File search page filtered to the 7 files matching 'hh39-dkk3', with the Bulk edit button at the upper right." width=2000 %}

3. Click the *Bulk edit* button.
4. On the left side of the screen, find the "Biosample" field and click the pencil icon. This will make that field editable across all of the file records.
5. Click the "Select a value" dropdown and choose the correct biosample record.
6. Above the dropdown, select the checkbox labeled *N of N selected records* (for example, *7 of 7 selected records*) to apply your choice to every record in the list, then click *Apply*.

   {% include screenshot.html src="/assets/img/bulk-edit-screen.png" alt="The bulk edit panel for the Biosample field, with the '7 of 7 selected records' checkbox and the Apply button outlined in red." width=2566 zoom=true %}

   *Click the image to see it full size.*

7. Click *Save*.

Repeat for each remaining biosample.

> **Working with a lot of files?** We can do Steps 2 and 3 for you. Send us a spreadsheet mapping your biosamples' [local identifiers](#key-terms) to your filenames and we will handle the upload and the associations. Contact us at [help@facebase.org](mailto:help@facebase.org).

## Step 4. Create experiments {#create-experiments}

Create an experiment record to describe the experimental details of your study. The form covers a wide range of experiment types, so in many cases you will fill in only a small number of fields.

1. From the Dataset record, scroll down to the *Experiment* section.
    - If you do not see the *Experiment* section, click the *Show empty sections* button near the top right of the page.
2. To the right of the heading, click the *Add records* button. A new browser tab opens with the data entry form.

   {% include screenshot.html src="/assets/img/add-experiment.png" alt="The Experiment section of a Dataset page, with the Add records button outlined in red." width=2405 %}

   {% include screenshot.html src="/assets/img/experiment-form-seq.png" alt="The Create 1 Experiment record form for a hypothetical RNA-seq assay, with Experiment Type, Local Identifier, Molecule Type, and Strandedness filled in and the remaining fields blank." width=2000 %}

3. Fill in the form as completely as possible for the fields relevant to your data. The example above shows a hypothetical RNA-seq experiment; many fields are left blank because they do not apply to that experiment type.
4. Click *Save*. You will see the newly entered experiment information.

### Link each biosample to its experiment {#link-biosamples-to-experiments}

Now that your experiment records exist, go back and fill in the field you left blank in Step 1.

1. From the Dataset page, open the *Biosample* section.
2. For each biosample, click the pencil (*Edit*) icon in the list — or open the biosample record and click *Edit*. The Experiment column will be empty until you complete this step.

   {% include screenshot.html src="/assets/img/biosample-list-edit-icon.png" alt="The Biosample list on a Dataset page, with the pencil (Edit) icon for the first record outlined in red." width=783 %}

3. Click the "Experiment" field. In the "Select Experiment for Biosample" window, click the button in the "Select" column next to the correct experiment.

   {% include screenshot.html src="/assets/img/select-experiment-window.png" alt="The Select Experiment window listing five experiments, with the Select button for one of them outlined in red." width=1888 %}

4. Click *Save*.

## Step 5. Link an experiment to a protocol {#link-protocol}

Linking a protocol tells others exactly how the experiment was performed, which is often what makes your data reusable.

1. From the Dataset page, scroll down to the *Experiment* section and click the *View Details* icon.
2. On the experiment record, find the "Protocols" field and click *Link records*. This opens the "Link Protocols to Experiment" window. If your protocol is already in the system, check the box next to it and click *Link*.

   {% include screenshot.html src="/assets/img/link-experiment-to-protocol.png" alt="The Protocols field on an experiment record, showing None, with the Link records button outlined in red." width=2000 %}

   {% include screenshot.html src="/assets/img/select-protocol-window.png" alt="The Link Protocols to Experiment window, with one protocol's checkbox selected and the Link button outlined in red." width=1592 %}

3. If your protocol isn't in the system yet, click *Create new*. A new browser tab opens.

   {% include screenshot.html src="/assets/img/create-new-protocol.png" alt="The Link Protocols window, with the Create new button outlined in red." width=1592 %}

4. Fill in the required *Project* and *Name* fields (leave the *Released* field set to "false"), then add the protocol in one of three ways:
    1. Fill in the "Description" field with the protocol information for online display,
    2. Enter a link to an existing online source in the "URL" field, or
    3. Upload a file (PDF, Word document, etc.) by clicking *Select File* at the "Protocol Document" field.

   {% include screenshot.html src="/assets/img/create-new-protocol-form.png" alt="The Create 1 Protocol record form. The Description, URL, and Protocol Document fields, the three ways to add a protocol, are outlined in red." width=2000 %}

5. Click *Save*. Close the tab and return to the "Link Protocols to Experiment" window to select the protocol record you just created.

## Enhancer reporter records {#enhancer-records}

Enhancer reporter assays are entered directly on the Dataset record and do not use the five-step workflow above.

1. Go to the Dataset record.
2. Scroll down to the *Enhancer Reporter Assay* section and click *Add records*. A new window opens where you can select existing records in the system. To create a new record, go to the next step.
3. Click *Create new*. A new browser tab opens with the data entry form.
4. Fill in the details as completely as possible and click *Save*.

## What happens next

When your biosamples, files, and experiments are entered and linked, review your dataset record for completeness and then [email us](mailto:help@facebase.org) to let us know it is ready for review.
