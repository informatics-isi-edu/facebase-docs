---
title: Visualizations in FaceBase Data
permalink: /docs/visualizations/
---

The FaceBase system includes pipelines that convert data into helpful visualizations that can deepen a user's experience with the data.

Available visualizations in FaceBase include an Image Volume viewer, Histology/Annotations viewer, and Single Cell viewer.

## Image Volume viewer

Some imaging data is created in three dimensions, which is useful in understanding the shape and size of specific anatomical regions of the face and skull, for example when comparing control specimen with mutant specimen.

Where a 3D image has been contributed, FaceBase provides a downsampled 3D preview inside your browser window.

Use your mouse to turn the 3D image in all directions and to zoom in and out.

Use the right panels to step through slices of the interior through different views.

You can also use the Volume panel to adjust the levels or brightness of the planes to virtually examine craniofacial structures from a variety of sources, all within your browser.

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

Two dimensional images in the FaceBase repository are commonly histological – stains to show regions where a gene is expressed.

Our pipeline accepts the raw image file from a microscope and converts it to a high-resolution image that can be viewed in a browser page.

Thus, the viewer acts like an online digital microscope, allowing the user to zoom in for a deep view.

To download a screenshot of the current view, click “Take a Screenshot.” Note the accurate scale included with the image, which is crucial for researchers. This is ideal for use in publications and presentations.


Example dataset:
- [https://www.facebase.org/chaise/record/#1/isa:imaging_data/RID=1-W96W](https://www.facebase.org/chaise/record/#1/isa:imaging_data/RID=1-W96W)  

histology viewer: image 1-W96W displays new feature: Annotations.

In this microscopy image, there are annotations of interest. You can zoom in and pan around. Our viewer supports very high resolution imaging, so depending on the resolution, you can zoom in deeply almost like an online microscope.

Contributors can add annotations which are linked to our anatomy terms. For more information link TBD.

## Surface Mesh Viewer

If a contributor provides surface mesh data - which depicts surfaces of interest  - our Surface Mesh Viewer can create a ‘jigsaw puzzle’ effect where each surface mesh object is given its own color and channel, which can be toggled on and off. Surface meshes may be annotated with anatomical landmarks demarcating specific locations on a specimen. The distance between landmarks can also be calculated.

This educational tool is especially powerful for new researchers to learn anatomical regions.

## Single Cell Viewer

Example datasets:
- [https://www.facebase.org/chaise/record/#1/isa:dataset/RID=1-YSFP](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=1-YSFP)
- [https://www.facebase.org/chaise/record/#1/isa:dataset/RID=R-PPWJ](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=R-PPWJ)

Where available, in Sequencing Data listings, you'll see a thumbnail of a scatter plot for processed data where it is based in R data (such as a Seurat object).

SCREENSHOT TBD

When you open the record, you'll have access to a visualization created via our integration with the [UCSC Cell Browser](https://cells.ucsc.edu/).

SCREENSHOT TBD

We are in the process of enhancing or pipeline to handle additional data. So these visualization will be available for more single cell data soon.
