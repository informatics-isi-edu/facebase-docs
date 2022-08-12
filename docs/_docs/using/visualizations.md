---
title: Visualizations in FaceBase Data
permalink: /docs/visualizations/
---

The FaceBase system includes pipelines that convert data into helpful visualizations that can deepen a user's experience with the data.


## Image Volume viewer

Example datasets:
- [https://www.facebase.org/chaise/record/#1/isa:dataset/RID=TKT](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=TKT)
- [https://www.facebase.org/chaise/record/#1/isa:dataset/RID=1-SXC4](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=1-SXC4)


NIFTI (and what other kinds?) files are converted into a online viewer in the browser.

Using [this dataset](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=TKT), with full resolution NIFT and microCT data, as an example, scroll down to the section "Downsampled Image Previews".

NIFTI is one medical imaging standard that's widely supported and can be viewable by most available tools.

Use the **Click here to load the image** button.

An orthogonal slice viewer displays different panes that 'slice' through different orientations of the 3D image.

Click the **Volumes** label in the top left and choose 3D. This converts the image to 3D Volume. Then use the Threshold bar to adjust as/if needed until the image is clear.

You can view this in action in [TBD video](#).

## Histology/Annotations Viewer

Example dataset:
- [https://www.facebase.org/chaise/record/#1/isa:imaging_data/RID=1-W96W](https://www.facebase.org/chaise/record/#1/isa:imaging_data/RID=1-W96W)  

histology viewer: image 1-W96W displays new feature: Annotations.

In this microscopy image, there are annotations of interest. You can zoom in and pan around. Our viewer supports very high resolution imaging, so depending on the resolution, you can zoom in deeply almost like an online microscope.

Contributors can add annotations which are linked to our anatomy terms. For more information link TBD.

## Single Cell Viewer

Example datasets:
- [https://www.facebase.org/chaise/record/#1/isa:dataset/RID=1-YSFP](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=1-YSFP)
- [https://www.facebase.org/chaise/record/#1/isa:dataset/RID=R-PPWJ](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=R-PPWJ)

Where available, in Sequencing Data listings, you'll see a thumbnail of a scatter plot for processed data where it is based in R data (such as a Seurat object).

SCREENSHOT TBD

When you open the record, you'll have access to a visualization created via our integration with the [UCSC Cell Browser](https://cells.ucsc.edu/).

SCREENSHOT TBD

We are in the process of enhancing or pipeline to handle additional data. So these visualization will be available for more single cell data soon.
