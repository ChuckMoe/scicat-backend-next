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

from scicat_openapi_client.models.sample_class import SampleClass  # noqa: E501


def make_instance(include_optional):
    """Test SampleClass
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
    if include_optional:
        return SampleClass(
            created_by='',
            updated_by='',
            created_at=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            updated_at=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            owner_group='',
            access_groups=[
                ''
            ],
            instrument_group='',
            is_published=True,
            sample_id='',
            owner='',
            description='',
            sample_characteristics=None
        )
    else:
        return SampleClass(
            created_by='',
            updated_by='',
            created_at=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            updated_at=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            owner_group='',
            access_groups=[
                ''
            ],
            is_published=True,
            sample_id='',
        )


class TestSampleClass(unittest.TestCase):
    """SampleClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequiredSampleClass(self):
        """Test SampleClass"""
        make_instance(include_optional=False)

    def testOptionalSampleClass(self):
        """Test SampleClass"""
        make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
