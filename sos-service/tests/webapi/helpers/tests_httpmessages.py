from unittest import TestCase
from webapi.helpers.httpmessages import *


class HttpMessages(TestCase):
    """Tests to verify the correct functioning of the httpmessages helpers"""
    defaultmessage = "default log message"
    
    def test_badrequest_withmessage_returnobject(self):
        message = badrequest(self.defaultmessage)

        self.assertEqual(message.status_code, 400)
        self.assertEqual(message.log_message, self.defaultmessage)

    def test_badrequest_withoutmessage_raiseerror(self):
        with self.assertRaises(TypeError):
            message = badrequest()
