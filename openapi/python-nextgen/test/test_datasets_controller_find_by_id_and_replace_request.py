# coding: utf-8

"""
    SciCat backend API

    This is the API for the SciCat Backend  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

import datetime
import random
import time
import unittest

import scicat_openapi_client
from scicat_openapi_client.models. \
    datasets_controller_find_by_id_and_replace_request import \
    (
    DatasetsControllerFindByIdAndReplaceRequest)  # noqa: E501


def make_instance(include_optional):
    """Test DatasetsControllerFindByIdAndReplaceRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
    random.seed(time.perf_counter())
    if include_optional:
        return DatasetsControllerFindByIdAndReplaceRequest(
            owner_group='ingestor',
            access_groups=[
                'admin',
                'ingestor'
            ],
            instrument_group='instrument',
            pid=str(random.randint(0, 99999)),
            owner='ingestor',
            owner_email='pi@email.invalid',
            orcid_of_owner='',
            contact_email='pi@email.invalid',
            source_folder='/',
            source_folder_host='http://folder.invalid',
            size=1.337,
            packed_size=1.337,
            number_of_files=1.337,
            number_of_files_archived=1.337,
            creation_time=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            type='raw',
            validation_status='',
            keywords=[
                'test'
            ],
            description='Description',
            dataset_name='Dataset Name',
            classification='Classification',
            license='License',
            version='1',
            is_published=True,
            techniques=[
                scicat_openapi_client.models.technique_class.TechniqueClass(
                    pid=str(random.randint(0, 99999)),
                    name='Technique', )
            ],
            shared_with=[],
            relationships=[
                scicat_openapi_client.models.relationship_class
                .RelationshipClass(
                    pid=str(random.randint(0, 99999)),
                    relationship='', )
            ],
            datasetlifecycle={},
            scientific_metadata={},
            comment='Comment',
            data_quality_metrics=1.337,
            principal_investigator='ingestor',
            end_time=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            creation_location='scicat',
            data_format='',
            proposal_id=str(random.randint(0, 99999)),
            sample_id=str(random.randint(0, 99999)),
            instrument_id=str(random.randint(0, 99999)),
            id=str(random.randint(0, 99999)),
            created_at='',
            updated_at='',
            created_by='',
            updated_by='',
            history='',
            attachments=[
                scicat_openapi_client.models.attachment.Attachment(
                    created_by='ingestor',
                    updated_by='ingestor',
                    created_at=datetime.datetime.strptime(
                        '2013-10-20 19:20:30.00',
                        '%Y-%m-%d %H:%M:%S.%f'),
                    updated_at=datetime.datetime.strptime(
                        '2013-10-20 19:20:30.00',
                        '%Y-%m-%d %H:%M:%S.%f'),
                    owner_group='ingestor',
                    access_groups=[
                        'admin',
                        'ingestor'
                    ],
                    instrument_group='instrument',
                    is_published=True,
                    id=str(random.randint(0, 99999)),
                    thumbnail='Thumbnail',
                    caption='Caption',
                    dataset_id=str(random.randint(0, 99999)),
                    proposal_id=str(random.randint(0, 99999)),
                    sample_id=str(random.randint(0, 99999)), )
            ],
            origdatablocks=[
                scicat_openapi_client.models.orig_datablock.OrigDatablock(
                    created_by='ingestor',
                    updated_by='ingestor',
                    created_at=datetime.datetime.strptime(
                        '2013-10-20 19:20:30.00',
                        '%Y-%m-%d %H:%M:%S.%f'),
                    updated_at=datetime.datetime.strptime(
                        '2013-10-20 19:20:30.00',
                        '%Y-%m-%d %H:%M:%S.%f'),
                    owner_group='ingestor',
                    access_groups=[
                        'admin',
                        'ingestor'
                    ],
                    instrument_group='instrument',
                    is_published=True,
                    _id=str(random.randint(0, 99999)),
                    dataset_id=str(random.randint(0, 99999)),
                    size=1.337,
                    chk_alg='sha512',
                    data_file_list=[
                        scicat_openapi_client.models.data_file.DataFile(
                            path='/',
                            size=1.337,
                            time=datetime.datetime.strptime(
                                '2013-10-20 19:20:30.00',
                                '%Y-%m-%d %H:%M:%S.%f'),
                            chk='sha512',
                            uid='1000',
                            gid='1000',
                            perm='1', )
                    ], )
            ],
            datablocks=[
                scicat_openapi_client.models.datablock.Datablock(
                    created_by='ingestor',
                    updated_by='ingestor',
                    created_at=datetime.datetime.strptime(
                        '2013-10-20 19:20:30.00',
                        '%Y-%m-%d %H:%M:%S.%f'),
                    updated_at=datetime.datetime.strptime(
                        '2013-10-20 19:20:30.00',
                        '%Y-%m-%d %H:%M:%S.%f'),
                    owner_group='ingestor',
                    access_groups=[
                        'admin',
                        'ingestor'
                    ],
                    instrument_group='instrument',
                    is_published=True,
                    _id=str(random.randint(0, 99999)),
                    dataset_id=str(random.randint(0, 99999)),
                    archive_id=str(random.randint(0, 99999)),
                    size=1.337,
                    packed_size=1.337,
                    chk_alg='sha512',
                    version='1',
                    data_file_list=[
                        scicat_openapi_client.models.data_file.DataFile(
                            path='/',
                            size=1.337,
                            time=datetime.datetime.strptime(
                                '2013-10-20 19:20:30.00',
                                '%Y-%m-%d %H:%M:%S.%f'),
                            chk='sha512',
                            uid='1000',
                            gid='1000',
                            perm='1', )
                    ], )
            ],
            investigator='ingestor',
            input_datasets=[
                str(random.randint(0, 99999))
            ],
            used_software=[
                'scicat'
            ],
            job_parameters={},
            job_log_data='log'
        )
    else:
        return DatasetsControllerFindByIdAndReplaceRequest(
            owner_group='ingestor',
            owner='ingestor',
            contact_email='pi@email.invalid',
            source_folder='/',
            number_of_files_archived=1.337,
            creation_time=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            type='raw',
            principal_investigator='ingestor',
            creation_location='scicat',
            investigator='ingestor',
            input_datasets=[
                str(random.randint(0, 99999))
            ],
            used_software=[
                'scicat'
            ],
        )


class TestDatasetsControllerFindByIdAndReplaceRequest(unittest.TestCase):
    """DatasetsControllerFindByIdAndReplaceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequiredDatasetsControllerFindByIdAndReplaceRequest(self):
        """Test DatasetsControllerFindByIdAndReplaceRequest"""
        make_instance(include_optional=False)

    def testOptionalDatasetsControllerFindByIdAndReplaceRequest(self):
        """Test DatasetsControllerFindByIdAndReplaceRequest"""
        make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
