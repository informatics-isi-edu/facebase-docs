#!/usr/bin/env python

"""This script is an example of programmatically creating a FaceBase dataset record.

   Prerequisites:
    - Authorization to add datasets to a FaceBase project.
    - If you do not have authorization, contact help@facebase.org.
"""

import argparse
import sys
from deriva.core import DerivaServer, get_credential


def create_dataset(hostname, catalog_id, project_rid, metadata):
    """Create a new dataset record in FaceBase.

    This function should only be called once to create a dataset. Each invocation
    will create a new dataset record and return a new RID.

    The `metadata` is a dictionary structure that includes the key-value pairs to
    be included in the dataset.
      - `project`: the numeric identifier for the project
      - `title`: short text title for the dataset
      - `description`: verbose description (paragraph or more of text recommended)
      - `protected_human_subjects`: boolean flag
      - `study_design`: (optional) summary of the study protocol

    The `description` and `study_design` allow markdown text for formatted output.

    :param hostname: hostname of the facebase server
    :param catalog_id: id of the database "catalog" on facebase server
    :param metadata: metadata for the dataset
    :return: dataset record
    """

    credential = get_credential(hostname)
    server = DerivaServer('https', hostname, credential)
    catalog = server.connect_ermrest(catalog_id)
    _ = catalog.getPathBuilder()

    # For historical reasons, the dataset record references the project using
    # the project's older numeric identifier. The older 'id' fields are not
    # displayed on the FaceBase website, therefore we first need to translate
    # the current project 'RID' into its legacy 'id'.
    projects = _.isa.project.filter(_.isa.project.RID == project_rid).entities()
    if not projects:
        raise Exception(f'Error: no project found with {project_rid}. Are you logged in?')
    
    # add the project reference to the `metadata`
    metadata['project'] = projects[0]['id']

    # insert the dataset record in the FaceBase catalog (ie, database)
    dataset_records = _.isa.dataset.insert([metadata], defaults={'id', 'accession', 'released', 'release_date'})
    assert dataset_records, 'this should never be empty if no exception was raised'
    return dataset_records[0]


def main():
    parser = argparse.ArgumentParser(description='Example of creating a dataset (metadata) record in FaceBase')
    parser.add_argument('--hostname', help='hostname', default='www.facebase.org')
    parser.add_argument('--catalog_id', help='catalog identifier', default='1')
    parser.add_argument('--controlled_access', action='store_true', help='controlled access dataset')
    parser.add_argument('project_rid', help='project record ID (RID)')
    parser.add_argument('title', help='dataset title')
    parser.add_argument('description', help='dataset description')
    args = parser.parse_args()
    print(args)
    dataset_record = create_dataset(args.hostname, args.catalog_id, args.project_rid, {'title': args.title, 'description': args.description, 'protected_human_subjects': args.controlled_access})
    print(dataset_record)
    return 0


if __name__ == '__main__':
    sys.exit(main())
