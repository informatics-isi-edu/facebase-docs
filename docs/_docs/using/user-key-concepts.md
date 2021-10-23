---
title: Key Concepts for FaceBase Users
permalink: /docs/user-key-concepts/
---

## How data is organized (ie., Data Model)

Per deployment, data is organized in a model that describes different metadata, data types and their relationship to each other in order to accurately represent the mechanics of actual experiments.

In the FaceBase Data Browser, data is organized into a hierarchy based on the concept of a Study (**update for FB**):

- A **Study** describes high-level objectives and the overall design of one or more experiments.

- An **Experiment** describes the molecule type and cell count of an experiment applied to one or more Replicates.

- A **Replicate** contains basic information about the bio-sample used in the experiment as well as its biological and technical replicate numbers. It is the linking record for the Specimen record (ie, the input of the experiment) and the Data File(s) (ie, the output of the experiment).

- A **Specimen** contains full information about a biosample (species, age stage, assay type, etc) and connects to the experiment via the Replicate record.

- The **File** record contains the data file and is linked to the Replicate record of an experiment.

You can view the diagram model on **add diagram model from Submitters info**

## Data Browser URLs (not sure if we're keeping this)

The user interface to the data catalog is referred to as the Data Browser or something similar. Chaise has a specific layout and look and feel that are similar across all deployments.

![screenshot of a typical Chaise landing page](/images/chaise-landing-page-example.png)

The Data Browser is powered by Chaise (from DERIVA) which you'll notice in the data URLs **update with FB example**:

```
https://www.facebase.org/chaise/recordset/#1/Data:Specimen
```

Which follows the general syntax:

```
facebase.org/chaise/<page type>/#<catalog number>/<data namespace>
```

Where:

* `facebase.org` is the deployment's domain,
* `chaise` is the default top-level directory going into the Data Browser
* `<page type>` is one of the following types of pages used in Chaise to display or interact with data.
* `#<catalog number>` is the number of the data catalog. This can be any number but is always preceded by a hashtag. It's not important to know much about this as a user except to realize that if a major change occurs that requires a different catalog be used, this number could change (although it's not likely).
* `<data namespace>` is the namespace of a Chaise database table that represents an element of the data model. In the example above, the URL is taking you to all of the Specimen records in the catalog.

URL paramaters in Search queries that you'll frequently see:
* `@sort(RID)` - Enforces sorting for the search results. In this case, rows will be sorted by [RID (or Record ID) TBD](link below).
* `*::facets::<string>` - As the user applies filters and text searches to a Search page, the URL will includes [TBD - I forgot, what's the technical name for the long string in the URLs?].

## Page types

Here are the different page types within the repository and you'll notice in the Data Browser URLs:

| Page type     | Common name | Description                                                                                                                                                                          |
|--------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `recordset`  | Search page | Displays a set of records (Detail pages) that match a search query and may be filtered.                                                                                              |
| `record`     | Detail page | Captures all of the available metadata and known related data for a particular unit of data.                                                                                         |
| `recordedit` | Edit page   | Displays the Detail page in editing mode, for creating or editing a data record. This is only available for those with editing rights (ie, data submitters, programmers and admins). |

## Related tables/linked records

To allow deep interlinking between data records, data from various labs may be linked together and discovered via search and filtering.

On many record pages, you'll find a list of metadata at the top of the page (the *Summary*) and then there are *Sections* listed underneath with their own tabular rows of data. These represent records from a different table that have been associated with this record.

## FAIR Principles

The FaceBase Data Browser promotes FAIR data production by:

* **F**: providing rich metadata using an Entity-Relationship model to express relationships between diverse data elements;
* **A**: offering rich access control and access to metadata via standard HTTP web service interfaces;
* **I**: integrating with standardized terms defined by collaborators, consortium or communities; and
* **R**: supporting dynamic model evolution so that the data presented accurately represents the current structure and state of knowledge within an investigation.

To support these principals, FaceBase emphasizes well-defined metadata and data models, the use of controlled vocabularies and ontologies, and any other ways to include enough measurable metadata for all data entered to allow the appropriate data to show up in searches, and allow others to reproduce and verify experiments.

## RID (Resource IDentifier)

Every record within Chaise has its own unique identifier, the **Resource IDentifier (or RID)**. This is a permanent, citable, globally unique identifier displayed for every data record, much like an Accession number. Such identifiers are a critical part of making data FAIR.
