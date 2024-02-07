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

from scicat_openapi_client.models.job_class import JobClass  # noqa: E501


def make_instance(include_optional):
    """Test JobClass
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
    random.seed(time.perf_counter())
    if include_optional:
        return JobClass(
            id=str(random.randint(0, 99999)),
            email_job_initiator='',
            type='',
            creation_time=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            execution_time=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            job_params={},
            job_status_message='',
            dataset_list=[
                str(random.randint(0, 99999))
            ],
            job_result_object={},
            owner_group='ingestor'
        )
    else:
        return JobClass(
            id=str(random.randint(0, 99999)),
            email_job_initiator='',
            type='',
            creation_time=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            execution_time=datetime.datetime.strptime(
                '2013-10-20 19:20:30.00',
                '%Y-%m-%d %H:%M:%S.%f'),
            job_params={},
            job_status_message='',
            dataset_list=[
                str(random.randint(0, 99999))
            ],
            job_result_object={},
            owner_group='ingestor'
        )


class TestJobClass(unittest.TestCase):
    """JobClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRequiredJobClass(self):
        """Test JobClass"""
        make_instance(include_optional=False)

    def testOptionalJobClass(self):
        """Test JobClass"""
        make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
