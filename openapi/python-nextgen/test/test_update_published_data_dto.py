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
import unittest

from scicat_openapi_client.models.update_published_data_dto import \
    UpdatePublishedDataDto  # noqa: E501


def make_instance(include_optional):
    """Test UpdatePublishedDataDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
    if include_optional:
        return UpdatePublishedDataDto(
            id=str(random.randint(0, 99999)),
            doi=str(random.randint(0, 99999)),
            affiliation='scicat',
            creator=[
                'ingestor'
            ],
            publisher='scicat',
            publication_year=1.337,
            title='Title',
            url='http://scicat.invalid',
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
        return UpdatePublishedDataDto()


class TestUpdatePublishedDataDto(unittest.TestCase):
    """UpdatePublishedDataDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequiredUpdatePublishedDataDto(self):
        """Test UpdatePublishedDataDto"""
        make_instance(include_optional=False)

    def testOptionalUpdatePublishedDataDto(self):
        """Test UpdatePublishedDataDto"""
        make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()