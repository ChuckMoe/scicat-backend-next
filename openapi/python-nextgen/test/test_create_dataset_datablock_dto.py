# coding: utf-8

"""
    SciCat backend API

    This is the API for the SciCat Backend  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

import datetime
import unittest

import scicat_openapi_client
from scicat_openapi_client.models.create_dataset_datablock_dto import \
    CreateDatasetDatablockDto  # noqa: E501


def make_instance(include_optional):
    """Test CreateDatasetDatablockDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
    if include_optional:
        return CreateDatasetDatablockDto(
            archive_id='',
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
                    chk='12345',
                    uid='1000',
                    gid='1000',
                    perm='1', )
            ]
        )
    else:
        return CreateDatasetDatablockDto(
            archive_id='',
            size=1.337,
            packed_size=1.337,
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
            ],
        )


class TestCreateDatasetDatablockDto(unittest.TestCase):
    """CreateDatasetDatablockDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequiredCreateDatasetDatablockDto(self):
        """Test CreateDatasetDatablockDto"""
        make_instance(include_optional=False)

    def testOptionalCreateDatasetDatablockDto(self):
        """Test CreateDatasetDatablockDto"""
        make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
