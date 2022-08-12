---
title: Browsing and Filtering Data
permalink: /docs/discovering-data/
---

The FaceBase Data Browser is a model-driven web interface for data discovery, analysis, visualization, editing, sharing and collaboration over tabular data to allow users to:

* Search, explore, and browse collections of data
* Navigate from one data record to the next by following their relationships
* Explore and export data collections
* Share and cite data with other users or for use in publications

The Data Browser represents data via records that can be filtered with attributes in the sidebar much like you would in an online shopping site.

## Beginning your search

You may begin your search with the [All datasets link](https://www.facebase.org/chaise/recordset/#1/isa:dataset@sort(release_date::desc::,RID)). You can also start with a narrowed search by species. These are available in the top navigation menu.

<!--

Your search will start with the resulting search page, where you may then further refine your search with the filtering sidebar and then you can drill down to a specific dataset on the detail page.

* [Search page](../search-page/) - This page shows the records available in the deployment and the records that match filters.
* [Detail page](../detail-page/) - This page shows the details for an individual record and its related tables.
-->

## General search

![FaceBase Data Browser search page]({{ "/assets/img/search-page.png" | relative_url }})

What you see when start searching are:

* Search results based on filters.
* Faceted navigation sidebar on the left
* Search bar above the results


The columns of the search results include the RID, Title, summary of Experiment Types, species, age stages, PIs and release date for the datasets. By default the data is sorted to display the most recently released data first.

On the left side is the faceted navigation based on characteristics of the data and experiments. If you'll scroll down, you'll see all of the categories of facets available to narrow down your search. Only the first few are open, so as you scroll, you can click on a category to open the list of attributes. Then click on the desired attributes and the search results on the right will automatically update.

For long lists of attributes, click the "Show more" link to open a window where you can access the complete list (including synonyms and other information from the related controlled vocabularies or ontologies).

You can also use the small search box just above the facets to use a free text search.

Note: One of the facets is "Protected Human Data". This refers to [controlled-access data](https://www.facebase.org/access/policies/), which [requires going through the Data Access Request process](https://www.facebase.org/access/request/).

You can choose any of the facets in any order. You can also choose as many facets within a category as you'd like.

As you choose facets, you can see your choices displayed in buttons above the search results.

## Image Search

If you are interested in browsing through the large amount of imaging data available, you can use the Image Search (available as a link on the homepage or through the Browse Data top navigation menu).

It's the same type of searching as described above, but specific only to the data files from imaging experiments. Note that there are examples of imaging data that do not result in an image: landmark data, some metadata, etc.

But where there is an image, a thumbnail will appear for each record.

You can filter by experiment types (fluorescences microscopy, microCT, etc), species, age stages, etc.

Once you find an image of interest, there is a link to the related Dataset record where you can find more information about the study and experiment as well as any other related data.

There is also the ["Share and cite" button]({{ "/docs/sharing-and-citing-data/" | relative_url }}) that provides a permanent link as well as a publication-level citation for the dataset.
