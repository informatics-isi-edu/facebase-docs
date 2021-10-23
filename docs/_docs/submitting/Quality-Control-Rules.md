---
title: Quality Control Rules
permalink: /docs/Quality-Control-Rules/
---

Version 1:

The following is a list of metrics to measure the quality level of data in FaceBase. A program is run nightly that compares existing data to these metrics and flags discrepancies.

## 1. Dataset-level Requirements

### 1.1 Dataset-level required **fields**:

* Accession (in place)
* Title (in place)
* Description
* Project (in place)
* Requires DOI
* DOI (generated)
* Released (in place)

### 1.2 Dataset-level required **high-level metadata tags**:

* Organism
* Experiment Type
* Stage (depending on Species and specimen)
* Anatomy
* Gene

### 1.3 Dataset-level organizational requirements:

* At least one Experiment AND one Biosample AND one Replicate associating the Experiment and
Biosample

## 2. Experiment-level requirements

* At least one associated Replicate
* Experiment Type (in place)
* Local Identifier
* Strandedness (depending on Experiment Type value)
* Target of Assay (depending on Experiment Type=ChIP-seq)
* Control Assay (depending on Target of Assay value)
* Molecule Type (depending on Experiment Type value)
* Histone Modification (depending on Target of Assay value)
* Chromatin Modifier (depending on Experiment Type value)
* Transcription Factor (depending on Experiment Type value)
* RNA-Seq Selection (depending on Experiment Type value)

## 3. Biosample-level requirements:

* At least one associated Replicate
* Local Identifier
* Species (in place)
* Specimen (in place)
* Stage (depending on Species and specimen)
* Anatomy
* Collection Date
* Cell Source (depending on Specimen value)
* Cell Characterization (depending on Specimen value)

## 4. Replicate-level requirements:

* Experiment (in place)
* Biosample (in place)
* Bioreplicate Number (in place)
* Technical Replicate Number (in place)
* Sequencing files (depending on associated Experiment Type)
* Image or Mesh file (depending on associated Experiment Type)
