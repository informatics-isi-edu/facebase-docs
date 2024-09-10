---
title: Self-guided Tutorial
permalink: /docs/Self-Guided-Tutorial/
---

This is a self-guided tutorial released for the Data Submitter's track of the FaceBase Bootcamp held on September 8, 2021.

It is intended to be used to practice creating records, adding metadata and uploading data. The basic directions are below and it is intended that you refer to the documentation [on this site](../Create-a-Dataset/) for more specific details. If you get stuck, please don't hesitate to contact the FaceBase Hub at: [help@facebase.org](mailto:help@facebase.org).

1) Join the “FaceBase Demo” Globus group by going to this link [https://app.globus.org/groups/5eebf313-c0b2-11ea-adc2-0ed6a5b292e1/about](https://app.globus.org/groups/5eebf313-c0b2-11ea-adc2-0ed6a5b292e1/about) and following the instructions to join the group. A member of FaceBase will need to approve your request, so please allow 24-48 hours. If you still have not received notification of acceptance, please contact us at [help@facebase.org](mailto:help@facebase.org).

2) Go to the [FaceBase Demo page](https://www.facebase.org/id/1-RC7M) and login using the same credentials you used to join the group above.

3) Create a new Dataset under that Project following the same structure (in terms of Biosamples, Experiments and Replicates) as in the example [Bootcamp self-guided tutorial dataset](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=2-HR74).

4) From the Supplementary Files section of the above dataset, download to your computer the following file: [Bootcamp-self-guided-tutorial-data.zip](https://www.facebase.org/chaise/record/#1/isa:file/RID=2-HR94)

5) Unpack the zip file to your computer and change the name of its sub-directories by doing the following replacements:
* Rename the directory "DATASET-RID" to the value of the RID of the new Dataset you created.
* Rename the directory called “Micro-CT-mutant-REPLICATE-RID” to the value of the RID of the micro-CT *mutant* Replicate.
* Rename the directory called “Micro-CT-control-REPLICATE-RID” to the value of the RID of the micro-CT *control* Replicate. .
* Rename the directory called “RNA-seq-REPLICATE-RID” to the value of the RID of the RNA-seq Replicate..

6) Start the [DERIVA Upload Utility](https://github.com/informatics-isi-edu/facebase-curation/wiki/Deriva-Clients) and:
* Click the **Options** button to verify that the server value is *www.facebase.org* .
* Click the **Login** button to authenticate using the same credentials you used above.
* Click the **Browse** button and select the directory that you’ve named with the value of the RID of your new dataset.

7) Once the tool has scanned the content of the directory, click the **Upload** button to start uploading the files.

8) Once the utility is finished, check your dataset to verify that the files have been added (you may need to refresh the browser page). Email us at [help@facebase.org](mailto:help@facebase.org) if you have any questions.
