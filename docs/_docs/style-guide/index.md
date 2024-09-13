---
title: FaceBase Documentation Style Guide
permalink: /docs/style-guide/
---

This style guide will describe how to write copy and format descriptions of interface elements in the FaceBase documentation.

## Contents

- [Writing Elements Guidelines](#writing-elements-guidelines)
  - [1. Tone and Voice](#1-tone-and-voice)
  - [2. Language and Terminology](#2-language-and-terminology)
  - [3. Formatting](#3-formatting)
  - [4. Lists](#4-lists)
  - [5. Links and Cross-References](#5-links-and-cross-references)
  - [6. Code and Commands](#6-code-and-commands)
  - [7. Images and Alt Text](#7-images-and-alt-text)
  - [8. Grammar and Punctuation](#8-grammar-and-punctuation)
  - [9. Examples and Use Cases](#9-examples-and-use-cases)
  - [10. Glossary](#10-glossary)
- [Interface Elements Formatting Guidelines](#interface-elements-formatting-guidelines)
  - [1. Field Names](#1-field-names)
  - [2. Buttons](#2-buttons)
  - [3. Section Headings on Forms](#3-section-headings-on-forms)
  - [4. Dropdown Lists](#4-dropdown-lists)
  - [5. Menu Navigation](#5-menu-navigation)

## Writing Elements Guidelines

These guidelines wlil help maintain consistency and clarity across all content.

### 1. Tone and Voice
- **Tone**: Professional yet approachable. The documentation should be easy to understand for non-experts but precise enough for expert users.
- **Voice**: Use active voice whenever possible. Keep sentences short and direct. For example:
  - **Active**: "Contributors submit data through the portal."
  - **Passive**: "Data is submitted by contributors through the portal."

### 2. Language and Terminology
- **Plain language**: Avoid jargon unless absolutely necessary. When you must use technical terms, provide brief explanations or a link to a glossary.
  - **Example**: "The ACAN gene is involved in cartilage formation, which is important in craniofacial development."
- **Consistency in terminology**: Always use the same terms for key concepts. For example:
  - "Dataset" not "data set."
  - "Programmatic access" not "API access."

### 3. Formatting
- **Headings**: Use sentence case for headings.
  - **Example**: “Exporting data from FaceBase,” not “Exporting Data From FaceBase.”
- **Bold for emphasis**: Use bold sparingly to highlight critical action points or terms.
  - **Example**: **Click** the “Export” button.
- **Italics for definitions**: Use italics to introduce definitions of terms.
  - **Example**: *Gene expression* refers to the process by which information from a gene is used in the synthesis of a functional gene product.

### 4. Lists
- **Bulleted lists**: Use for unordered items or step-by-step instructions.
  - **Example**:
    1. Click the dataset title.
    2. Select the “Export” button.
- **Numbered lists**: Use for sequences of actions.
  - **Example**:
    1. Download the file.
    2. Analyze the data.

### 5. Links and Cross-References
- **External links**: Use descriptive text for links rather than the raw URL.
  - **Example**: Visit the [FaceBase homepage](https://www.facebase.org).
- **Internal links**: Link to related sections within the documentation for further reading or deeper dives.
  - **Example**: For more on BAG file exports, visit the [Exporting with BAG](#link-to-bag-page) page.

### 6. Code and Commands
- **Code snippets**: Use monospace font for commands, code, and file paths.
  - **Example**: `python download_data.py`
- **Inline code**: Use backticks for inline code.
  - **Example**: To download files, use the `wget` command.

### 7. Images and Alt Text
- **Images**: Use images sparingly to illustrate complex processes or visualizations. Keep them clear and minimal.
- **Alt text**: Provide descriptive alt text for all images.
  - **Example**: "Screenshot of the Export button on a dataset detail page."

### 8. Grammar and Punctuation
- **Oxford comma**: Always use the Oxford comma in lists.
  - **Example**: "The dataset includes craniofacial data, dental models, and imaging files."
- **Capitalization**: Only capitalize proper nouns or key terms (e.g., FaceBase, ACAN gene, 3D Viewer).
- **Acronyms**: On first use, spell out the full term followed by the acronym in parentheses.
  - **Example**: "Binary Archive Graph (BAG)."

### 9. Examples and Use Cases
- **Examples**: Provide real-world examples that are relevant to craniofacial, dental, and oral research.
  - **Example**: "A researcher studying cleft palate can export gene expression data for further analysis."

### 10. Glossary
- **Key terms**: Maintain a glossary of technical terms used across the documentation, linking to it where appropriate.
  - **Example**: ACAN: A gene involved in cartilage formation and craniofacial development.



## Interface Elements Formatting Guidelines

When referring to interface elements in documentation, maintaining a consistent style is crucial for clarity. Use the following guidelines for referencing field names, buttons, section headings, and dropdown lists.

### 1. Field Names
When referring to a field name (e.g., input fields in forms), capitalize and use quotation marks to highlight the field name.
- **Example**: In the "Sample ID" field, enter the unique identifier for your sample.

#### 2. Buttons
When referring to buttons that users need to click, use bold for the button label.
- **Example**: Click **Save** to store your changes.

#### 3. Section Headings on Forms
When referring to section headings within forms or pages, use italics and capitalization as it appears in the interface.
- **Example**: Scroll down to the *Replicates* section to input data about biological replicates.

#### 4. Dropdown Lists
When users need to select a specific value from a dropdown list, format the field name in quotation marks and the value to be selected in bold.
- **Example**: In the "Status" field, select **Approved** from the dropdown list.

#### 5. Menu Navigation
For multi-step navigation, use `>` to indicate moving through menus or sections.
- **Example**: Navigate to **Export** > **BDBag** to download the Bag for bulk export of the dataset files.
