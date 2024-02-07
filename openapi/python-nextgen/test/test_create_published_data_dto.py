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

from scicat_openapi_client.models.create_published_data_dto import \
    CreatePublishedDataDto  # noqa: E501


def make_instance(include_optional):
    """Test CreatePublishedDataDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
    random.seed(time.perf_counter())
    if include_optional:
        return CreatePublishedDataDto(
            id=str(random.randint(0, 99999)),
            doi=str(random.randint(0, 99999)),
            affiliation='scicat',
            creator=[
                'ingestor'
            ],
            publisher='scicat',
            publication_year=1.337,
            title='Title',
            url='http://scicat.com',
            abstract='Abstract',
            data_description='Description',
            resource_type='raw',
            number_of_files=1.337,
            size_of_archive=1.337,
            pid_array=[
                ''
            ],
            authors=[
                'ingestor'
            ],
            registered_time=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            status='archived',
            scicat_user='ingestor',
            thumbnail='Thumbnail',
            related_publications=[],
            download_link='http://some.link'
        )
    else:
        return CreatePublishedDataDto(
            creator=[
                'ingestor'
            ],
            publisher='scicat',
            publication_year=1.337,
            title='Title',
            abstract='Abstract',
            data_description='Description',
            resource_type='rae',
            pid_array=[
                ''
            ],
        )


class TestCreatePublishedDataDto(unittest.TestCase):
    """CreatePublishedDataDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequiredCreatePublishedDataDto(self):
        """Test CreatePublishedDataDto"""
        make_instance(include_optional=False)

    def testOptionalCreatePublishedDataDto(self):
        """Test CreatePublishedDataDto"""
        make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
