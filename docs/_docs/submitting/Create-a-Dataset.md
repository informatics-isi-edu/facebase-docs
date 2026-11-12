---
title: Creating a Dataset
permalink: /docs/Create-a-Dataset/
---

A **dataset** represents a unit of data collected and submitted to the FaceBase site. Typically, a dataset represents a whole or a logical unit of an investigation (i.e., a study within an overall investigation/project). When you submit your data, the first step is creating the **dataset record**, which acts as a container record that describes the unit of data as a whole.

This page describes how to create a dataset record, add tags that will allow your data to be discovered in searches, and link your dataset to related datasets.

**Important**: make sure that you are on the [www.facebase.org](https://www.facebase.org/) site. Do not use the _development_ or _staging_ site for data entry.

## 1. Create the Dataset record

Begin your data submission by creating a Dataset record.

1. Find your project
    - Follow the link here to [Projects](https://www.facebase.org/chaise/recordset/#1/isa:project)
    - Search and find your project, then click the "View Details" icon to go to your project page.
<br/><br/>
    ![Find Project]({{ "/assets/img/find-project.png" | relative_url }})
<br/><br/>
    - Make sure that you are logged in. You will see your user name in the upper right hand corner of the page if you are logged in.
    - If you are not logged in, click the "Log In" link. After you complete the login process, you will be returned to your project page.
    - Then look down the page to the "Dataset" subheading, and click the "Add Record" link to a form that will let you create a dataset.
<br/><br/>
    ![Add Dataset]({{ "/assets/img/add-dataset.png" | relative_url }})
<br/><br/>
    - You can also get to the Dataset Create Form from 'www.facebase.org' ->
    'Data Browser' -> 'Datasets' -> 'All Datasets' -> '+ Create' button.
<br/><br/>
    ![Create Dataset Link]({{ "/assets/img/create-dataset-link.png" | relative_url }})
<br/><br/>
2. Note that the **Record ID** number (this is the unique identifier for FaceBase datasets) will be automatically generated when you submit the form.
3. Fill in the required fields:
<br/><br/>
    ![Dataset Form]({{ "/assets/img/create-dataset-form.png" | relative_url }})
<br/><br/>
    - _Title_: Enter approximately one sentence of text that summarizes your data submission **in a way that is meaningful to the prospective users of the data**. Example: "Whole-genome transcriptome profiling of E13.4 Wnt1-Cre;Tgfbr2flfl by microarray of maxilla and mandible".
    - _Project_: Choose the project the Hub created for you from the dropdown list. (This will normally be filled in for you if you followed the first instructions above and began by finding your project record.)
    - _Released?_: Only the FaceBase data curators can change this value. Default "false".

    Although the following fields are not required, we highly recommend that you use them to help users understand more about your data:
    - _Description_: Enter a description with enough detail so that prospective users of the data can determine whether it may be relevant to their research questions.
        - If you are submitting a standalone dataset (i.e., not part of a series), please provide ample description of your dataset.
        - If your dataset is part of a series, please reference a description of the series if it is not repeated for each set.
        - Note that the field accepts text with "Markdown" rendering. There is a toolbar available to help you format the text (with icons for bold, italics, lists, etc.).
    - _Study Design_: Use this field to add more details about the design of this study.
4. When you are finished Click _Submit_ (upper right hand of the form).

## 2. Add tags for filtering and search

Now that you have added a new Dataset record, you should be back on the display
page for the new Dataset. Since you are logged in, you will see many categories of related records which are currently empty.

At a minimum, please add tags for the following categories using the "Add Record" button:
- _Experiment Type_
- _Organism_

We encourage you to use as many tags as apply to make your data more discoverable. Other likely tags are:
- _Age Stage_
- _Phenotype_
- _Anatomy_
- _Gene_

For each category, add tags using the following procedure:

1. Scroll down to the category.
2. Click the _Add Record_ button on the right hand side of the category heading.
    ![Add Record]({{ "/assets/img/base-record.png" | relative_url }})
3. A modal dialog window will open and overlay the page.
    ![Chose Tags]({{ "/assets/img/choose-tags.png" | relative_url }})
4. Scroll through the list and/or search for terms.
5. Click the checkbox next to each term that applies to your dataset.
6. Click _Submit_ at the upper right corner of the modal window.
7. Confirm that your tags appear on the dataset page. If you do not see the tags
   that you just added, refresh your browser page.

## 3. Link to related datasets

Use the _Related Datasets_ section of your dataset page to link your dataset to
other datasets it is connected to. A related dataset can be:

- **in another repository**, such as GEO or dbGaP. Link to it whether your
  FaceBase dataset holds complementary data (for example, imaging that goes with
  sequencing data in GEO) or only the descriptive metadata for the external data.
- **another FaceBase dataset**. For example, if your dataset is derived from or
  is an analysis of an existing FaceBase dataset, link to that dataset.

To add a related dataset:

1. On your dataset page, find the _Related Datasets_ section (look through the
   hotlinks on the left side of the page).
2. Click the _Add records_ button. The "Create Related Dataset record" form
   opens in a new tab. The _Dataset_ field is already filled in with your
   dataset.
<br/><br/>
    ![Create Related Dataset form]({{ "/assets/img/create-related-dataset.png" | relative_url }})
<br/><br/>
3. In the _Relationship_ field, choose how the datasets are related:
    - For a dataset in another repository: _dbGaP dataset_, _GEO GSE dataset_,
      or _GEO GDS dataset_.
    - For another FaceBase dataset:
        - _Derived from_: your dataset was derived from the related dataset.
        - _Secondary analysis of_: your dataset is an analysis of the related
          dataset.
        - _Primary data source of_: your dataset is the original data that the
          related dataset was derived from or analyzed.
        - _Related FaceBase dataset_: the datasets are related in another way.
4. Identify the related dataset. Fill in **one** of these fields, not both:
    - **For a dataset in another repository**, enter its permanent URL in the
      _Related Dataset URL_ field. Use the DOI link or other permanent URL where
      possible (for example, the GEO or dbGaP page for its accession number).
    - **For another FaceBase dataset**, choose it from the _FaceBase related
      dataset_ list. If the related dataset has not been released yet, only
      logged-in users who can see it will see it listed on your dataset page.
5. Click _Save_, and confirm the related dataset appears on your dataset page.

Please do not upload data to FaceBase that is identical to data you have
already deposited in another repository. Link to it instead.

## Review

Review your dataset record and then you are ready to continue to the next phase: [creating Experiment and Biosample entries](../Describe-Experiments-and-Biosamples/).
