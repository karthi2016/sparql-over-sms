from unittest import TestCase
from utilities.messaging.extraction import *


class Extraction(TestCase):
    """Tests to verify the correct functioning of the extraction helpers"""
    sample_correlationid = 'abc'
    sample_category = '1'
    sample_position = '0'
    sample_body = 'XXXXXX'
    sample_validmessage = ''.join([sample_correlationid, sample_category, sample_position, sample_body])

    def test_extractall_validmessage_returns(self):
        # arrange
        message = self.sample_validmessage

        # act
        a, b, c, d = extract_all(message)

        # assert
        self.assertEqual(a, self.sample_correlationid)
        self.assertEqual(b, self.sample_category)
        self.assertEqual(c, self.sample_position)
        self.assertEqual(d, self.sample_body)

    def test_extractmetadata_validmessage_returns(self):
        # arrange
        message = self.sample_validmessage

        # act
        a, b, c = extract_metadata(message)

        # assert
        self.assertEqual(a, self.sample_correlationid)
        self.assertEqual(b, self.sample_category)
        self.assertEqual(c, self.sample_position)

    def test_extractbody_validmessage_returns(self):
        # arrange
        message = self.sample_validmessage

        # act
        a = extract_body(message)

        # assert
        self.assertEqual(a, self.sample_body)
