# FaceBase Curation

This is the home for documentation and issue tracking for the [FaceBase Data Hub](https://www.facebase.org). For help, please contact the [help mail list](mailto:help@facebase.org).

# Data Curation Guide

For step-by-step instructions on how to submit data to FaceBase, see our [Data Curation Guide](https://github.com/informatics-isi-edu/facebase-curation/wiki).

# Issue Tracker

If you have already contacted the help email list above and have been given an issue tracking number, you may check its status and follow its progress on our [Issue Tracker](https://github.com/informatics-isi-edu/facebase-curation/issues).

# Documentation Site

This repo includes the source files for the FaceBase documentation site, published via GitHub Pages:

- Find the published content at https://informatics-isi-edu.github.io/facebase-curation/docs/home/
- Source files are found in: `/docs/_docs/`
- The order of docs and sidebar navigation is managed at: `/docs/_data/docs.yml`
    - If you are adding a new page, you must edit this to refer to the new file or it will not appear on the docs site.
- There are folders that organize the source docs, but the folders do not dictate the hierarchy. Just makes it easier to find the source doc you need.
-  Once you commit changes under the `/docs/` directory, changes are updated live within a few minutes.
-  This site is based on a template and customized in the `/docs/_includes/`, `/docs/_layouts/` and `/docs/_sass/` directories.
-  You can learn more about the jekyll template at this [README](https://github.com/informatics-isi-edu/facebase-curation/blob/master/docs/README.md).
