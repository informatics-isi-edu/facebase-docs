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

You may begin your search with the [BROWSE ALL DATASETS link from the homepage](https://www.facebase.org/chaise/recordset/#1/isa:dataset). You can also start with a narrowed search by species. These are available in the top navigation menu.

![FaceBase Data menu]({{ "/assets/img/data-menu.png" | relative_url }})

## General search

What you see when you start searching the data browser are:

* Search results based on filters
* Faceted navigation sidebar on the left
* Search bar above the results

![FaceBase Data Browser search page]({{ "/assets/img/search-page.png" | relative_url }})

The columns of the search results include the *RID*, *Title*, *Experiment Types*, *Species*, *Stage(s)*, *PI(s)* and *Release Date* for the datasets. By default, the data is sorted to display the most recently released data first.

On the left side is the faceted navigation based on characteristics of the data and experiments.

![FaceBase Data Browser search page]({{ "/assets/img/filtering-sidebar.png" | relative_url }})

Scroll down to see all of the categories of facets available to narrow down your search.

Only the first few categories are open by default. As you scroll, you can click on each category to open the list of facets. Then click on the desired facets and the search results on the right will automatically update.

For long lists of facets, you have two options:

* Use the small search box just above the facets.
* click the **Show more** link to open a window where you can browse the complete list (including synonyms and other information from the related controlled vocabularies or ontologies).

Note: One of the facets is "Protected Human Data". This refers to [controlled-access data]({{ "/docs/human-data/" | relative_url }}), which [requires going through the Data Access Request process]({{ "/docs/human-data/" | relative_url }}).

You may choose any of the facets in any order. You may also choose as many facets within a category as you'd like.

As you choose facets, you will see them displayed as buttons above the search results.

## Image Search

If you are interested in browsing through the large amount of imaging data available, you can use the Image Search (available on the homepage or through the DATA top navigation menu).

![Image Search on the homepage]({{ "/assets/img/image-search-homepage.png" | relative_url }})

It's the same type of searching as described before, but filtered for the data files from imaging experiments. Note that there are examples of imaging data that do not result in an image, such as landmark data, some metadata, etc.

But where there is an image, a thumbnail will appear for each record.

You can filter further by experiment types (fluorescences microscopy, microCT, etc), species, age stages, etc.

Once you find an image of interest, there is a link to the related Dataset record where you can find more information about the study and experiment as well as any other related data.

There is also the ["Share and cite" button]({{ "/docs/sharing-and-citing-data/" | relative_url }}) that provides a permanent link as well as a publication-level citation for the dataset.
