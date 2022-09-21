import unittest
from parameterized import parameterized
from mock import patch
from main1 import name, list, shelf, add, delete


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

class TestFunction (unittest.TestCase):
    # def test_list(self):
    #
    #     etalon = ['passport, 2207 876234, Василий Гупкин', 'invoice, 11-2, Геннадий Покемонов', 'insurance, 10006, Аристарх Павлов']
    #
    #     result = list(documents)
    #     self.assertEqual(result, etalon)
    #     print("test_list выполнен")
##--------------------------------------------------------------------------
    # @parameterized.expand(
    #     [
    #         ('2207 876234', 'Василий Гупкин'),
    #         ('11-2', 'Геннадий Покемонов'),
    #         ('10006', 'Аристарх Павлов')
    #     ]
    # )
    # def test_name(self, number, result):
    #     result1 = name(documents, number)
    #     self.assertEqual(result1, result)
    #     print("test_name выполнен")
# ##--------------------------------------------------------------------------
#     @parameterized.expand(
#         [
#             ('2207 876234', '1'),
#             ('11-2', '1'),
#             ('5455 028765', '1'),
#             ('10006', '2')
#         ]
#     )
#     def test_shelf(self, number, result):
#         result1 = shelf(directories, number)
#         self.assertEqual(result1, result)
#         print("test_shelf выполнен")
##--------------------------------------------------------------------------
    # @parameterized.expand(
    #     [
    #         ('012345', 'pass', 'Олег', '2', ([
    # {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    # {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    # {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    # {"type": 'pass', "number": "012345", "name": 'Олег'},
    #  ],  {'1': ['2207 876234', '11-2', '5455 028765'],
    # '2': ['10006', '012345'],
    # '3': []}) )
    #     ]
    # )
    # def test_add(self, number, type, name, shelf, result):
    #     result_add = add(documents, directories, number, type, name, shelf)
    #     self.assertEqual(result_add, result)
    #     print("test_add выполнен")
##--------------------------------------------------------------------------
    @parameterized.expand(
        [
            ('2207 876234', ([
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
     ],  {'1': ['11-2', '5455 028765'],
          '2': ['10006', ],
          '3': []}) )
        ]
    )
    def test_delete(self, number, result):
        result_delete = delete(documents, directories, number)
        self.assertEqual(result_delete, result)
        print("test_delete выполнен")
# #----------------------------------------------------------------------