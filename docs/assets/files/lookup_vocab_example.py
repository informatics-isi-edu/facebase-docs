#!/usr/bin/env python

"""This script is an example of programmatically looking up a FaceBase vocabulary term.
"""

import argparse
import sys
from deriva.core import DerivaServer, get_credential


def lookup_vocab(vocab_table_name, term_id, hostname='www.facebase.org', catalog_id='1'):
    """Lookup vocabulary record in FaceBase.


    The `term_id` is a short identifier used in FaceBase for each vocabulary term 
    that can be found in a given `vocab_table_name` vocabulary table. For example, 
    the term `mandible` has a code of `UBERON:0001684` and is found in the `anatomy`
    table.

    :param vocab_table_name: the name of the vocabulary table
    :param term_id: id of the vocabulary term
    :param hostname: hostname of the facebase server (default: www.facebase.org)
    :param catalog_id: id of the database "catalog" on facebase server (default: 1)
    :return: list of matching vocabulary term records
    """

    server = DerivaServer('https', hostname)
    catalog = server.connect_ermrest(catalog_id)
    _ = catalog.getPathBuilder()

    # first get a handle to the vocabular table; this will fail if no such table exists.
    vocabulary = _.vocab.tables[vocab_table_name]

    # now lookup the term; this will return a `ResultSet` that behaves like a python 
    # sequence and it will not have any entries if there is no match for the `term_id`.
    terms = vocabulary.filter(vocabulary.id == term_id).entities()

    return terms


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hostname', help='hostname', default='www.facebase.org')
    parser.add_argument('--catalog_id', help='catalog identifier', default='1')
    parser.add_argument('--names_only', action='store_true', help='only print names', default=False)
    parser.add_argument('vocabulary_table', help='vocabulary table name')
    parser.add_argument('term_id', help='vocabulary term identifier')
    args = parser.parse_args()

    # lookup terms
    terms = lookup_vocab(args.vocabulary_table, args.term_id, hostname=args.hostname, catalog_id=args.catalog_id)

    # display them
    if args.names_only:
        print([term['name'] for term in terms])
    else:
        print(list(terms))

    return 0


if __name__ == '__main__':
    sys.exit(main())
