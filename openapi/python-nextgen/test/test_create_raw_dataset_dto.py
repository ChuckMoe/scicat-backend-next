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
from scicat_openapi_client.models.create_raw_dataset_dto import \
    CreateRawDatasetDto  # noqa: E501


def make_instance(include_optional):
    """Test CreateRawDatasetDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
    random.seed(time.perf_counter())
    if include_optional:
        return CreateRawDatasetDto(
            owner_group='ingestor',
            access_groups=[
                'admin',
                'ingestor'
            ],
            instrument_group='instrument',
            pid=str(random.randint(0, 99999)),
            owner='ingestor',
            owner_email='pi@email.invalid',
            orcid_of_owner=str(random.randint(0, 99999)),
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
                    name='technique', )
            ],
            shared_with=[],
            relationships=[
                scicat_openapi_client.models.relationship_class
                .RelationshipClass(
                    pid=str(random.randint(0, 99999)),
                    relationship='relationship', )
            ],
            datasetlifecycle={},
            scientific_metadata={},
            comment='Comment',
            data_quality_metrics=1.337,
            principal_investigator='',
            end_time=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            creation_location='scicat',
            data_format='',
            proposal_id=str(random.randint(0, 99999)),
            sample_id=str(random.randint(0, 99999)),
            instrument_id=str(random.randint(0, 99999))
        )
    else:
        return CreateRawDatasetDto(
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
        )


class TestCreateRawDatasetDto(unittest.TestCase):
    """CreateRawDatasetDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequiredCreateRawDatasetDto(self):
        """Test CreateRawDatasetDto"""
        make_instance(include_optional=False)

    def testOptionalCreateRawDatasetDto(self):
        """Test CreateRawDatasetDto"""
        make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
