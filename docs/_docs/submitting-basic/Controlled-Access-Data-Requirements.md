---
title: Guidelines for Submitting Controlled Access Data
permalink: /docs/Controlled-Access-Data-Requirements/
---

The purpose of this document is to provide guidelines for the submission of controlled access data to FaceBase. For a more general overview of Data Management and Sharing (DMS) with respect to controlled access data, please see:

[https://sharing.nih.gov/data-management-and-sharing-policy/protecting-participant-privacy-when-sharing-scientific-data/designating-scientific-data-for-controlled-access](https://sharing.nih.gov/data-management-and-sharing-policy/protecting-participant-privacy-when-sharing-scientific-data/designating-scientific-data-for-controlled-access)


## Subject-level Data

Data and metadata produced from human subjects research often include sensitive subject-level information such as geolocations, dates, rare diseases, etc. By definition, human subjects data that are submitted to FaceBase will include some form of subject-level information. Typically, such data come in the form of metadata on the subjects, per-subject data files like images or genomics, and/or per-subject rows in a database. In the following sections, we discuss the standards for submitting each of these forms of data to FaceBase.

## Cohorts and Consent Groups

If your human subjects data includes distinct consent groups or other cohort groupings you should submit each grouping as a separate dataset. Doing so will allow users of FaceBase to request your data, specific to a particular consent group or cohort. This streamlines the work of the NIH Data Access Committee (DAC) in reviewing requests for controlled access data. The online forms for entering metadata on datasets allow you to cross-reference related datasets. In addition, datasets are always grouped under your FaceBase project page.

## De-identification

Investigators **MUST** de-identify their research data, removing all Personally Identifiable Information (PII) and Protected Health Information (PHI), _to the extent possible_. For example, explicit identifiers such as name, date of birth, address, and medical record number, can and should be removed or otherwise de-identified _before_ submission to FaceBase. However, it may be impossible to fully de-identify data of all _implictly_ or _theoretically_ identifiable information. For example, some rare diseases may be so rare that just knowing the disease and broad geographic location or age in years, may be enough for some specialists in the disease to be able to combine information to re-identify the individual. Investigators are not expected to de-identify data to such an extent that it would be impossible to re-identify the subjects by combining with other knowledge or out-of-band information. With this qualified definition in mind, investigators **MUST** de-identify data to the extent possible.

## Metadata

Metadata is defined as "data that describes other data". FaceBase provides a number of online forms for entering metadata, as described in the [FaceBase Documentation](docs.facebase.org). These forms cover details about experiments, biological samples, protocols, and other related information to help researchers understand and reuse your data. Investigators **SHOULD** submit _de-identified_ metadata for their data. Investigators **SHOULD** enter as much demographic, disease, phenotype, anatomic, and other biological characteristics and experimental metadata as possible, so long as it does not include any PII or PHI. In addition, Investigators **SHOULD NOT** include implicitly identifiable information on subjects that could be combined with other information to re-identify the data.

### Local Identifiers

Investigators **MAY** include a `Local Identifier` for each entry in the _Biosample_ metadata, if applicable. The `Local Identifier` serves two purposes. First, if we or the users of your data have questions regarding your study, we can use the `Local Identifier` as a way to reference the subject or sample in question. Second, the `Local Identifier` may be used for mapping your submitted data files to the dataset metadata online. In addition, investigators **MAY** include optional identifiers for `Subject ID` to support longitudinal studies and `Family ID` to support proband information. These are separate fields in the _Biosample_ metadata.

### Supplementary Metadata

The FaceBase online data entry forms cover details that help other investigators find and reuse data. Some datasets, however, may need additional attributes to fully describe aspects of the data that fall outside of what the FaceBase data entry forms are designed to support. Investigators **MAY** submit supplementary metadata in a structured file format, such as a Comma-Separated Values (CSV) formatted spreadsheet. Investigators **MAY** also include more sensitive information than would be allowed in the standard FaceBase metadata.


## Files

Investigators typically submit data files as part of their dataset submission. Files **MAY** be organized in an arbitrary file hierarchy with any practical depth of subdirectories under the dataset base directory. Files **MAY** use any file name with the exception of `checksums.md5` and `mappings.csv`, and file names **MUST NOT** include any explicit PII or PHI.

The structure follows the form:

```
dataset/
	    file1
		file2
		...
		fileN
```

For example:

```
1-2345/
	   mappings.csv
	   checksums.md5
	   dirA/
		   dirB/
			   fileA.ext
	   dirC/
		   fileB.ext
	   fileC.ext
	   dirZ/
		   fileD.ext
	   dirG/
		   fileE.ext
```


## File Mappings for Subject-Level Data

When submitting _subject-level_ data files, Investigators **MAY** also submit a file `mappings.csv` that maps the data files to the subject-level metadata in the FaceBase database via the `Local Identifier`. The mappings file **MUST** be named `mappings.csv` and be included in the top-level of the dataset upload directory. The format **MUST** be plain text Comma-Separated Values (CSV) with exactly two columns `local_identifier` and `filename`. The `local_identifier` **MUST** match a value that you entered in the online `Biosample` metadata. The `filename` **MAY** include a relative path (e.g., `path/to/file.ext`) and **MUST** match a filename under the dataset upload directory. Note that the `local_identifier` need not be unique within the context of the `mappings.csv` file, however, the `filename` field **MUST** be unique within the `mappings.csv` file.

Example of a valid `mappings.csv` file:

| `local_identifier` | `filename`            |
|--------------------|-----------------------|
| `Cohort1SubA7`     | `dirA/dirB/fileA.ext` |
| `Cohort1SubA7`     | `dirC/fileB.ext`      |
| `COHORT2SUB99`     | `fileC.ext`           |
| `siteA_Subj-H24`   | `dirZ/fileD.ext`      |
| `siteA_Subj-H24`   | `dirG/fileE.ext`      |


## Structured Data Files

When submitting "structured" data such as database extracts, spreadsheets, or other tabular data, Investigators **MUST** use standard Comma-Separated Values (CSV) format and **MUST** include a "Data Dictionary" to describe each file. Data dictionaries **MUST** be named `DD_table_name.ext` corresponding to a specific tabular data file named `table_name.csv`. Data dictionaries **MAY** be either CSV or Microsoft Excel Open XML Spreadsheet (XLSX) formatted. For example, if you submit tabular file `experiments.csv` then the data dictionary would be either `DD_experiments.csv` or `DD_experiments.xlsx` depending on the choice of format. While FaceBase does not currently dictate a precise schema for the data dictionary, it **MUST** include the data element _name_ (i.e., the table column name), data _type_, and _definition_ and **SHOULD** include _allowable values_, _format_, and any other relevant information to assist data consumers with using the table data. Data dictionaries **SHOULD** be column-major.


## File Checksums

Investigators **MAY** submit the checksums for all files in a file named `checksums.md5`. The checksums file should be formatted according to the standard output of the GNU `md5sum` utility. If you are not familiar with using this utility we will provide detailed instructions.

```
09f7e02f1290be211da707a266f153b3  dirA/dirB/fileA.ext
52f83ff6877e42f613bcd2444c22528c  dirc/fileB.ext
```
