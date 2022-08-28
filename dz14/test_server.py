import unittest
import server

class TestServer(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_server_answer(self):
        name = 'Denis'
        message = 'hello'
        address = 'Elena'
        code = 202
        json_object = {
            'action':'msg_from_chat',
            'time':server.get_time(),
            'message':message,
            'user':
            {
            'name': name,
            'status':'online'
            },
            'address':address
        }
        result = server.get_answer(json_object)
        
        json_object_answer = {
            'responce':code,
            'time':server.get_time(),
            'user':
                {
                'name':name,
                'status':'online'
                },
            'message':message
            }
        self.assertEqual(json_object_answer, result)
        
if __name__ == '__main__':
    unittest.main()


