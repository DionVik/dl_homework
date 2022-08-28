import unittest
import client

class TestClient(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_client_sending(self):
        name = 'Denis'
        message = 'hello'
        address = 'Elena'
        json_object = {
            'action':'msg_from_chat',
            'time':client.get_time(),
            'message':message,
            'user':
            {
            'name': name,
            'status':'online'
            },
            'address':address
        }
        result = client.json_data_for_sending(name, message, address)
        self.assertEqual(json_object , result)
        
if __name__ == '__main__':
    unittest.main()


