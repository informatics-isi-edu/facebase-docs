---
title: Defining Surface Models (3D models)
permalink: /docs/Define-Surface-Model/
---

These instructions are for adding 3D models to the FaceBase site. We assume
you have uploaded 'meshes' to the site per the [upload instructions](../Upload-Files).
The instructions here assume you are logged in to the FaceBase site.

## Known Limitations

At this time, we know of the following limitations:

- Mesh file names must not include the '`;`' character, and it is probably best to avoid
any "special characters" in mesh file names until further notice.

## Create meshes and landmarks for upload

Avizo 9.5 is able to generate meshes and landmarks that are commensurate with each other and will display accurately in the mesh viewer.

1. Open the microCT scan (Nifti or DICOM) in Avizo and create a 3D Isosurface view.
2. From the Isosurface view, create an extracted surface file.
3. Choose surface view for the extracted surface. Click on surface view.
4. Expand Buffer in the Properties Windows.
5. Select Draw under Buffer to isolate the bone of interest in the 3D surface view. Important note: one must create a new extracted surface from the bone of interest again at this stage.
6. Export the newly extracted surface as Wavefront (.obj).
7. From the extracted surface file (step 2), repeat isolating other bones of interest (step 5).
8. To add a landmark, open Slice from the root file (in step 1).
9. In the Properties Windows, expand Plane Definition and select Show Dragger from Option.
10. Drag the center of the planes (red dot) to the landmark of interest. XYZ coordinates (appear as Plane Point under Plane Definition) will change accordingly.
11. Record the XYZ coordinates.
12. Repeat steps 10-11 for other landmarks.

## Create the model record

[[images/define-surface.jpeg]]

1. Go to your Dataset page.
2. Scroll down the page to the '3D Surface Models' section.
3. Click the 'Add' link to the right of the section heading.
4. Fill in the form:
    - You must enter a 'Label' (i.e., name) for the model.
    - We recommend entering a short description.
    - You can define a background color (Bg Color R...) in RGB color space using
      values from 0..255.
    - You can always come back and edit these values.
5. Click 'Submit Data'

## Add meshes to your model

1. Go to your 3D Surface Model page. If you just followed the instructions
    above, you will be on the right page.
2. Scroll down to the 'Mesh Model Data' section.
3. Click the 'Add' link to the right of the section heading.
4. Fill in the form:
    - You must pick the 'Mesh'. When you 'Pick a value' you will get a listing
      of the known mesh files in the catalog. You can search for your mesh based
      on its file name or dataset accession number.
      [[images/define-surface-pick-mesh.jpeg]]
    - You can customize the color (Color R...) in RGB color space.
    - You can customize the opacity. Note: there are some flaws with opacity
      rendering and you should report problems to us if you encounter them.
5. Click 'Submit Data'

## Add landmark points to your meshes

1. Go to your Mesh Data element that you want to add the landmark points to. (You can go to your mesh data element by clicking the eye icon in the list of Mesh Data elements of the Experiment page.)
2. In the Mesh Data page click the "Add" link to the right of the Landmark section.
3. In the Landmark Create Record page enter:
     - A Label for the landmark point. This will be the label displayed for the point in the mesh viewer.
     - The Point X, Point Y and Point Z coordinates of the landmark point. This are represented as float values and you can enter as many decimal places as required by your model. This values don't have any units and should be in the same unit conversion factor as your mesh data.
4. Enter a Radius value for the size of the sphere representing the landmark point in the mesh viewer. The default value of 0.1 is typically fine but you can adjust it depending on your mesh values.
5. Enter the Color R, Color G and Color B values to adjust the color of the landmark point in the mesh viewer. The default values are (255,0,0) which will produce a red point.
6. Optionally you can also enter an Anatomy value associate to the landmark point.
7. If you only need to add a single point to your mesh you can press the "Submit" button in the top-right corner and your point will be added to your mesh and shown in the mesh display if the "Show Landmarks" button is clicked in the top menu of the mesh viewer.
8. If you want to add additional landmark point, click the "+" button in the top-right corner to add one more point with all values replicated from the original point. Edit only the fields that differentiate this point from the previous one, e.g., Label and X, Y and Z coordinates. You can repeat this process to add as many new point as needed. When done editing all the new points, click the "Submit" button in the top-right corner and your points will be added to your mesh and shown in the mesh display if the "Show Landmarks" button is clicked in the top menu of the mesh viewer. (Even though you can add up to 200 points at a time this way, we recommend that you repeat this procedure at about 10 or 15 at a time)

## Review your new surface model

To review your entry, you will need to go back to the Dataset page. You may
need to refresh the page for the changes to take effect.
