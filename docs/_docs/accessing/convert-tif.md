---
title: Converting TIFF to OME-TIFF (using Bio Formats)
permalink: /docs/convert-tif/
---
Learn to convert a TIFF stack ZIP file to an open source format (OME-TIFF) using the Bio-Formats command line tools:

1. Download the TIFF stack ZIP file that you want to convert. For example, go to this dataset [https://doi.org/10.25550/2E-DST8](https://doi.org/10.25550/2E-DST8), scroll down to the "Imaging Data" section and click the `EuTH12.5mm1.zip` file to download to your computer.

2. Unzip the downloaded file. This will create a folder in your computer containing the stack of TIFF files. For the example above, the name of this folder will be `DMSO12.5mm1_head` and under that folder you'll see a sequence of 511 TIFF files named `DMSO12.5mm1_80000.tif` to `DMSO12.5mm1_80510.tif`.

3. Download the Bio-Formats command line tools file (`bftools.zip`) from: [https://bio-formats.readthedocs.io/en/stable/users/comlinetools/index.html](https://bio-formats.readthedocs.io/en/stable/users/comlinetools/index.html).

4. Unzip the `bftools.zip` file to a new folder in your computer. By default, this folder will be called `bftools`. (This zip file contains the bundled jar and you no longer need to download `bioformats_package.jar` separately.)  

5. Create a `.pattern` file: In the folder with the stack of TIFF files, create a text file called `stack.pattern` containing a single line informing the converting tool how the files should be grouped. For the example given above, the line in the pattern file will be:
```
   DMSO12.5mm1_80<000-510>.tif
```
The pattern file can have any name but must use the extension `.pattern` and must be in the same folder as the TIFF files. (For more information on pattern files please see [https://docs.openmicroscopy.org/bio-formats/6.9.1/formats/pattern-file.html) ](https://docs.openmicroscopy.org/bio-formats/6.9.1/formats/pattern-file.html))

6. Open a Terminal window (in Mac OSX or Linux) or a CMD window (in Windows) and change your directory to the `bftools` folder and type the following command:
```
 ./bfconvert  /Path_to_FB_DATA_DIRECTORY/DMSO12.5mm1_head/stack.pattern  /Path_to_FB_DATA_DIRECTORY/DMSO12.5mm1_head.ome.tif
```
Where we assume the FB_DATA_DIRECTORY is the folder where you initially saved the ZIP file downloaded from FaceBase (e.g., `EuTH12.5mm1.zip`). The bfconvert tool will create the resulting OME-TIFF file in this same folder.

7. This OME-TIFF file may be visualized with an open source viewer such as Fiji, which is available from [ https://imagej.net/software/fiji/downloads](https://imagej.net/software/fiji/downloads).
