import unittest
from YaUploader import YaUploader

with open('token_ya.txt', "r") as file_object:
    token_ya = file_object.read().strip()
print(token_ya)

folder_name = "000101"

class TestFunction (unittest.TestCase):


    def test(self):
        ya = YaUploader(token_ya)
        res = str(ya.create_folder(folder_name))
        res_code = "<Response [201]>"
        self.assertEqual(res, res_code)

