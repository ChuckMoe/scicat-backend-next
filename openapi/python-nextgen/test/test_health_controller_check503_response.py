# coding: utf-8

"""
    SciCat backend API

    This is the API for the SciCat Backend  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

import unittest

from scicat_openapi_client.models.health_controller_check503_response import \
    HealthControllerCheck503Response  # noqa: E501


def make_instance(include_optional):
    """Test HealthControllerCheck503Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
    if include_optional:
        return HealthControllerCheck503Response(
            status='error',
            info={"database": {"status": "up"}},
            error={
                "redis": {"status": "down", "message": "Could not connect"}
            },
            details={
                "database": {"status": "up"},
                "redis": {"status": "down", "message": "Could not connect"}
            }
        )
    else:
        return HealthControllerCheck503Response()


class TestHealthControllerCheck503Response(unittest.TestCase):
    """HealthControllerCheck503Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequiredHealthControllerCheck503Response(self):
        """Test HealthControllerCheck503Response"""
        make_instance(include_optional=False)

    def testOptionalHealthControllerCheck503Response(self):
        """Test HealthControllerCheck503Response"""
        make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
