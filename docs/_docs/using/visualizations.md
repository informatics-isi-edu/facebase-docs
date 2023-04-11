---
title: Visualizations in FaceBase Data
permalink: /docs/visualizations/
---

The FaceBase system includes pipelines that convert data [of a specific resolution and format] into helpful visualizations that can deepen a user's experience with the data. Such visualizations include: Image Volumes, Histology/Annotations, Surface Mesh and Single Cell viewers.

Recommended viewing: <a href="https://www.youtube.com/watch?v=XwTeM8QnrmQ&t=3s" target="_blank">Imaging Data in FaceBase</a>

## Image Volume Viewer (3D images)

Some imaging data is created in three dimensions, which is useful in understanding the shape and size of specific anatomical regions of the face and skull, for example when comparing control specimens with mutant specimens.

Where a 3D image has been contributed, FaceBase provides a downsampled 3D preview inside your browser window.  Use the following dataset to try it out - [TKT - microCT - Soft Tissue of Msx1 Control Mice at E16.5](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=TKT):

- Scroll down to the **Downsampled Image Previews** section.
- You have the option to click the "Full Screen" button for a larger view.
- Click the "Click here to load image".
- Once the image loads, you can make the following adjustments:
    - Use your mouse to turn the 3D image in all directions and to zoom in and out.
    - The panels on the right side provide different views of the image. Use the sliders in each panel to step through slices of the image.
- On the left side, hover over the "Volume" label to open the Volume panel where you can adjust the levels or brightness of the planes to virtually examine the structures in the image.

<a href="https://youtu.be/6G6eVzWoMz4" target="_blank">**Check out this video that demonstrates how to use the Image Volume Viewer.**</a>

## Histology/Annotations Viewer (2D images)

Two dimensional images in the FaceBase repository are commonly histological (stains are used to show regions where a gene is expressed). Our pipeline accepts the raw image file from a microscope and converts it into an image may be viewed in a web browser page (Figure 1). The viewer is like an online, digital microscope, allowing the user to zoom in for a deep view of the image (depending on the resolution of the image - the higher the resolution, the more deeply you can zoom in) (Figure 2).

To download a screenshot of the current view that includes an accurate, click **Take a Screenshot**. This is ideal for use in publications and presentations.

![Example of 2D image in default view]({{ "/assets/img/2d-default-img.png" | relative_url }})
*Figure 1: Example of 2D image in default view (Scale at 100mm)*

![Example of the same image zoomed in (Scale at 20 mm)]({{ "/assets/img/2D-image-zoomed-in.png" | relative_url }})
*Figure 2: Example of the same image zoomed in (Scale at 20 mm)*

Using the following dataset as an example: [1-SXC4 - Histology and schematic overview of mouse molar root development](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=1-SXC4):
- Scroll down to the **Imaging Data** section (or use the links on the left side of the page)
- Click *View* for one of the imaging records.
- Click *Full screen* to enlarge the viewer.

### Annotations

Our viewer also supports annotations of anatomical regions in an image. Annotations link to the corresponding FaceBase anatomy page for that region, which displays more information on the region and lists any related data in the FaceBase repository.

To see if an image already has annotations, click **Show Annotations**.

![Example of an annotated image]({{ "/assets/img/annotation-viewer.png" | relative_url }})
*Figure 3: Example of an annotated image*

Data contributors can use editing tools to mark a colored boundary around specific anatomical regions on an image and label them. [Data contributors can find documentation on how to use this feature here.](TBD)

![Example of an annotated image]({{ "/assets/img/annotations-editor.png" | relative_url }})
*Figure 3: Example of the Annotations Editor*

Example dataset:
- [https://www.facebase.org/chaise/record/#1/isa:imaging_data/RID=1-W96W](https://www.facebase.org/chaise/record/#1/isa:imaging_data/RID=1-W96W)  

Contributors can add annotations which are linked to our anatomy terms. [Click here for documentation on annotating images.]({{ "/docs/annotating-images/" | relative_url }})

## Surface Mesh Viewer

If a contributor provides surface mesh data - which depicts surfaces of interest  - our Surface Mesh Viewer can create a ‘jigsaw puzzle’ effect where each surface mesh object is given its own color and channel, which can be toggled on and off. Surface meshes may be annotated with anatomical landmarks demarcating specific locations on a specimen. The distance between landmarks can also be calculated.

This educational tool is especially powerful for new researchers to learn anatomical regions.

Use the following dataset as an example: [3V4A - E18.5 wildtype mouse microCT](https://www.facebase.org/id/3V4A)

- Scroll down to the **3D Surface Models** section.
- Click **Full Screen** if you're on a smaller display.
- Use the following buttons to explore the image: Zoom In, Zoom Out, Rotate.
- Click **Meshes** to open a panel of anatomical regions identified in the image.
    - Click the colored dots to toggle visibility on and off for that region.
    - Click an anatomical term to open the related Anatomiy page that lists all related datasets.

View all available Surface Mesh Model imaging data available in FaceBase.
https://www.facebase.org/chaise/recordset/#1/viz:model@sort(RID)

<a href="https://youtu.be/B_glpcYuspo" target="_blank">**Check out this video that demonstrates how to use the Surface Mesh Viewer.**</a>

## Single Cell Viewer (scatter plot of scRNA-Seq)

Example datasets:
- [https://www.facebase.org/chaise/record/#1/isa:dataset/RID=1-YSFP](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=1-YSFP)
- [https://www.facebase.org/chaise/record/#1/isa:dataset/RID=R-PPWJ](https://www.facebase.org/chaise/record/#1/isa:dataset/RID=R-PPWJ)

Where available, in Sequencing Data listings, you'll see a thumbnail of a scatter plot for processed data where it is based in R data (such as a Seurat object).

add screenshot of record with single cell data

When you open the record, you'll have access to a visualization created via our integration with the [UCSC Cell Browser](https://cells.ucsc.edu/).

add screenshot of scatter plot

We are in the process of enhancing or pipeline to handle additional data. So these visualization will be available for more single cell data soon.
