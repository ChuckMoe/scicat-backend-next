# coding: utf-8

"""
    SciCat backend API

    This is the API for the SciCat Backend  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""
import random
import time
import unittest

from scicat_openapi_client.models.instrument import Instrument  # noqa: E501


def make_instance(include_optional):
    """Test Instrument
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
    random.seed(time.perf_counter())
    if include_optional:
        return Instrument(
            pid=str(random.randint(0, 99999)),
            unique_name=str(random.randint(0, 99999)),
            name='instrument',
            custom_metadata={}
        )
    else:
        return Instrument(
            pid=str(random.randint(0, 99999)),
            unique_name=str(random.randint(0, 99999)),
            name='instrument',
        )


class TestInstrument(unittest.TestCase):
    """Instrument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequiredInstrument(self):
        """Test Instrument"""
        make_instance(include_optional=False)

    def testOptionalInstrument(self):
        """Test Instrument"""
        make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()