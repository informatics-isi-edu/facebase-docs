---
title: B. Complete the online Data Access Request (DAR) form
permalink: /docs/dar/
---

## Create new DAR request

Go to the [Data Access Request (DAR) page](https://www.facebase.org/chaise/recordset/#1/isa:data_access_request), log in and click the **+ Create** button at the top right corner of the page (The DAR form will open in a new tab).

![The Data Access Request page with the + Create button at the top right]({{ "/assets/img/dar-create.png" | relative_url }})

**You must first login with your FaceBase User account** in order to edit or start a new DAR form. If you are not registered as a FaceBase user, click on the **Sign Up** link at the top-right corner of the page and follow the instructions to log in through Globus and join the "FaceBase Users" group. You will receive email notification once your request is approved by the FaceBase Hub.

## Complete fields (1) to (24) on the DAR form

<div class="row">
  <div class="col-sm-4">
    <a href="{{ '/assets/img/dar-form-1.png' | relative_url }}" class="thumbnail" target="_blank">
      <img src="{{ '/assets/img/dar-form-1.png' | relative_url }}" alt="DAR form, fields 1 to 11">
    </a>
    <p class="text-center"><small>Fields 1–11</small></p>
  </div>
  <div class="col-sm-4">
    <a href="{{ '/assets/img/dar-form-2.png' | relative_url }}" class="thumbnail" target="_blank">
      <img src="{{ '/assets/img/dar-form-2.png' | relative_url }}" alt="DAR form, fields 12 to 21">
    </a>
    <p class="text-center"><small>Fields 12–21</small></p>
  </div>
  <div class="col-sm-4">
    <a href="{{ '/assets/img/dar-form-3.png' | relative_url }}" class="thumbnail" target="_blank">
      <img src="{{ '/assets/img/dar-form-3.png' | relative_url }}" alt="DAR form, fields 22 to 26 and Status">
    </a>
    <p class="text-center"><small>Fields 22–26 and Status</small></p>
  </div>
</div>

- A red asterisk denotes the field is required to create the request. Other fields can initially be left blank and completed at a later time.
- Fields marked **Renewal or Revision only** can be left blank when you start a new DAR. They are described under [Renewal or Revision requests](#renewal-or-revision-requests) below.

If you are starting a new DAR, complete the following fields:

| Field | What to enter |
|---|---|
| *(1) Record ID* | Nothing. This is generated automatically. |
| *(2) New DAR, Revision or Renewal?* | Select **New DAR**. |
| *(4) Title of Proposed Project* | The title of your project. |
| *(6) Principal Investigator* | The PI associated with this DAR. If the PI is not listed, create a new entry (see below). |
| *(7) Requesting Organization/Corporation* | The name of the organization or corporation requesting the data. |
| *(9) Research Use Statement (RUS)* | Your Research Use Statement. |
| *(10) Non-technical Research Summary* | A summary of your research in non-technical language. |
| *(11) How is the proposed research consistent with the data use limitations for the requested data?* | How your research is consistent with the data use limitations of the data you are requesting. |
| *(13) Describe data security measures to be implemented by the investigator* | The security measures you will use. For more information, see the FaceBase Data Use Certification document. |
| *(15) List all collaborators at your organization who will have access to the data* | Everyone at your organization who will have access to the data. |
| *(17) List all collaborators from other organizations involved in the project* | Your collaborators at other organizations and any planned data sharing among them. Collaborators listed here who wish to have access to the data must submit their own DARs. The DARs can be submitted simultaneously or sequentially, but neither project will be granted access until both are approved. |
| *(22) Do you have local IRB approval for this project?* | Your answer. If yes, also complete *(22a) IRB Protocol #*, *(22b) IRB Approval Expiration Date* and *(22c) Federalwide Assurance Number (FWA#)*. If you have questions about your institution's FWA#, contact your institution's Office of Research. |
| *(23) Submit a copy of the IRB approval letter* | The IRB approval letter, if required (see below). |
| *(24) Submit a copy of the IRB-approved protocol that documents approval to use FaceBase data* | The IRB-approved protocol, if required (see below). |

Some of these fields need additional steps:

- In field *(6) Principal Investigator*, if you don't find the PI's name listed there, click on the **+ Create new** button to create a new person record in the system. Then select the newly created record from the list of investigators.

<div class="row">
  <div class="col-sm-6">
    <a href="{{ '/assets/img/dar-create-person-1.png' | relative_url }}" class="thumbnail" target="_blank">
      <img src="{{ '/assets/img/dar-create-person-1.png' | relative_url }}" alt="The list of investigators with the + Create new button">
    </a>
    <p class="text-center"><small>List of investigators with the Create button highlighted.</small></p>
  </div>
  <div class="col-sm-6">
    <a href="{{ '/assets/img/dar-create-person-2.png' | relative_url }}" class="thumbnail" target="_blank">
      <img src="{{ '/assets/img/dar-create-person-2.png' | relative_url }}" alt="The Create new Person form">
    </a>
    <p class="text-center"><small>The Create new Person form</small></p>
  </div>
</div>

- If the dataset requires IRB approval (per the *Data Use Limitations* field), then in fields *(23) Submit a copy of the IRB approval letter...* and *(24) Submit a copy of the IRB-approved protocol...* click on the **Select file** button to the right of each field and select the file to upload from your local file system. The files will be uploaded to the FaceBase site once you save the form. The Data Access Committee (DAC) will not review your request without this documentation.
    **[QUESTION: Where should requesters look to find out whether a dataset requires IRB approval?]**
- Fields *(25) Upload the signed Data Use Certification Agreement* and *(26) Upload the signed copy of the Data Access Request (DAR)* should initially be left blank. **Once you print the complete DUC and DAR forms and obtain all required signatures you must edit this form to add the signed documents to these fields**.
- Leave *Approval Date* and *Expiration Date* blank.

## Save the form

- Make sure the *Status* field remains "In progress (Pending Signature)". Update it to "Completed" only when you have finished all fields and attachments, **including the signed documents**.
- Click the **Save** button in the upper right corner to save all information entered in the form at this point.

## Next step: Select your datasets

**Your request is not finished yet.** This step creates the basic DAR form, but the form does not yet include the datasets you are requesting, and it has not been submitted. Next, [select the requested datasets]({{ "/docs/select-datasets/" | relative_url }}).

## Renewal or Revision requests

To renew or revise an existing DAR, select **Renewal** or **Revision** in field *(2)*, then select the original DAR in field *(3) Parent DAR*. In field *(4) Title of Proposed Project*, use a title that differs from the original and includes "Renewal" or "Revision" to make this explicit.

Then complete the following fields in addition to the fields listed above:

| Field | What to enter |
|---|---|
| *(5) Changes to key administrative contact* | Whether there have been any changes to the key administrative contact associated with this request, the PI, Signing Official (SO) or IT Director (ITD). If yes, update the relevant fields. |
| *(8) Are there key changes to the Research Use Statement* | Whether the research objectives, aims, study design or analysis plan have changed from your previously approved request. If yes, update the RUS and, if applicable, the non-technical research summary and the description of how the proposed research is consistent with the data use limitations. |
| *(12) Key changes to data security measures* | Whether there have been any changes to key data security measures. If yes, describe them in field *(13)*. |
| *(14) Key changes to list of collaborators in your organization* | Whether the collaborators at your organization who have access to the data have changed. If yes, update field *(15)*. |
| *(16) Key changes to list of collaborators in other organizations* | Whether the collaborators from other organizations have changed. If yes, update field *(17)*. All external collaborators are expected to secure their own approved DAR. |
| *(18) Research Progress* | Your use of FaceBase data, any findings from studies conducted in the past year, and your research plans for the next year. |
| *(19) List of manuscripts* | Any manuscripts resulting from studies using FaceBase data, including manuscripts in press. |
| *(20) Describe any data security incidents* | Any data security incidents involving FaceBase data, such as breaches, unintentional data release or unauthorized data sharing. Include the date the NIH and the DAC were first notified, the steps taken to remedy the situation and the steps taken to prevent future occurrences. For reporting expectations, see the FaceBase Data Use Certification. |
| *(21) Have you combined the FaceBase datasets with datasets from other sources?* | Whether you have combined FaceBase datasets with datasets from other sources that were not described in the approved RUS. If yes, briefly describe the sources of the non-FaceBase datasets and amend your RUS before submitting the request. |

## If you are a researcher at an academic institute outside the US or if you are unfamiliar with IRBs...

[Please see our relevant FAQ on the main FaceBase site](https://www.facebase.org/help/faqs/#irb) that points you to resources at the US NIH website for more information on IRBs. For institutes outside the US, they usually have a comparable “ethics board” or something similar that can provide the necessary information. You may also contact your own university offices that deal with research on human subjects and they should provide guidance.
