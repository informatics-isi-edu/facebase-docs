#!/usr/bin/env python

"""This script is an example of programmatically uploading files for a FaceBase dataset.

   Prerequisites:
    - Files stored in a subdir named according to a valid dataset Record ID (RID).
    - Authorization to add files to the FaceBase dataset identitied by its RID.
"""

import argparse
import sys
from deriva.transfer import GenericUploader


def upload_files(hostname, catalog_id, path):
    """Upload file for a dataset in FaceBase.

    The data files must be located in a directory name `./path/to/dataset_rid`. The
    `dataset_rid` must be the last subdirectory in the `path` though there may be
    additional subdirectories under `path`. E.g., `./path/to/dataset_rid/A/B/C.nii.gz`.

    This function may be called multiple time for a dataset. The function is idempotent;
    i.e., it will skip files that were already uploaded to the dataset and upload only the
    new (new to the datset) files. It can also be called to retry failed uploads for files
    that were already attempted unsuccessfully.

    The result returned is a list of OrderedDict objects, with fields:
      - `State`: numeric enum code, see `deriva.transfer.upload.deriva_upload.UploadState`
      - `Status`: informal, readable, text code
      - `Results`: per-file metadata record created in FaceBase catalog

    :param hostname: hostname of the facebase server
    :param catalog_id: id of the database "catalog" on facebase server
    :param path: path for the dataset directory containing files for upload
    :return: results objects for the upload task
    """
    
    server={
        "host": hostname,
        "protocol": "https",
        "catalog_id": catalog_id,
    }
    uploader = GenericUploader(server=server)
    try:
        uploader.getUpdatedConfig()
        uploader.scanDirectory(path)
        results = uploader.uploadFiles()
        print(results)
        return results
    except Exception as e:
        print(e)
    finally:
        uploader.cleanup()

        
def main():
    parser = argparse.ArgumentParser(description='Example of uploading files to FaceBase')
    parser.add_argument('--hostname', help='hostname', default='www.facebase.org')
    parser.add_argument('--catalog_id', help='catalog identifier', default='1')
    parser.add_argument('path')
    args = parser.parse_args()
    print(args)    
    upload_files(args.hostname, args.catalog_id, args.path)
    return 0


if __name__ == '__main__':
    sys.exit(main())
