# coding: utf-8

"""
    SciCat backend API

    This is the API for the SciCat Backend  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

import unittest

from scicat_openapi_client.models.search_dto import SearchDto  # noqa: E501


def make_instance(include_optional):
    """Test SearchDto
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
    if include_optional:
        return SearchDto(
            text='',
            owner_group=[
                ''
            ],
            creation_location=[
                ''
            ],
            type=[
                ''
            ],
            keywords=[
                ''
            ],
            is_published=True,
            scientific=[
                ''
            ]
        )
    else:
        return SearchDto()


class TestSearchDto(unittest.TestCase):
    """SearchDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequiredSearchDto(self):
        """Test SearchDto"""
        make_instance(include_optional=False)

    def testOptionalSearchDto(self):
        """Test SearchDto"""
        make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
