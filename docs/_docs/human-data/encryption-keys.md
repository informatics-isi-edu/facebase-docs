---
title: D. Creating and uploading your encryption keys
permalink: /docs/human-data/encryption-keys/
---

If your request is approved, you will receive email from the FaceBase Hub and will be requested to create and upload your encryption in order to access the data.

## Creating your Encryption Keys

FaceBase controlled access data must be delivered in encrypted form. We use PGP Public Key encryption, which involves the generation of an encryption key pair consisting of a Private Key file and a Public Key file.

In order to encrypt the requested data, you need to submit a PGP Encryption Public Key file (see section below on how to upload that file) and keep it in a secure location in your computer the private key file and the associated passphrase. **Never submit your Private Key file, only the Public Key file must be uploaded**.

If you already have a pair of PGP Encryption key, then you can just upload your existing Public Key file.

If you don't have a PGP Encryption key pair, then follow the instructions given in this document: [FaceBase Create Encryption Keys Document (pdf)]({{ "/assets/files/facebase_create_encryption_keys.pdf" | relative_url }}).

## Upload your Encryption Public Key

1. Scroll down to the *Encryption Public Key* section of the page and click on the **+ Add Record** button.
    ![TBD]({{ "/assets/img/add_key1.png" | relative_url }})

2. Then click on the **Select file** button to pick the PGP Public Encryption file from your local file system and then click **Save** on the top right corner of the page to upload the file.
    ![TBD]({{ "/assets/img/add_key2.png" | relative_url }})

3. At any moment you can only have one encryption key associated to a given DAR, so if you need to update your key, first delete the current entry and then add the new one.

4. You can upload your key at any moment, but need to be present once the DAR is approved so that the Hub can generate your file(s) to download.
