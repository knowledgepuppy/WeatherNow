import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from Data2CSV import remove_units, url_process, data2csv

class TestData2CSV(unittest.TestCase):

    def test_remove_units(self):
        data = ["10mm", "20%", "-", "Tr", "30.5C"]
        expected = ["10", "20", "3", "2", "30.5"]
        result = remove_units(data)
        self.assertEqual(result, expected)

    @patch('Data2CSV.datetime')
    def test_url_process(self, mock_datetime):
        mock_datetime.today.return_value = datetime(2024, 11, 14)
        years = [1, 0]
        days = [10, 5]
        expected_url = ("http://www.meteomanz.com/sy2?l=1&cou=2250&ind=57687&d1=04&m1=11&y1=2023&d2=19&m2=11&y2=2024")
        result = url_process(years, days)
        self.assertEqual(result, expected_url)

    @patch('Data2CSV.GetData')
    @patch('Data2CSV.etree.HTML')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_data2csv(self, mock_open, mock_etree, mock_getdata):
        mock_getdata.return_value.Get.return_value = '<html><body><td>10mm</td><td>20%</td><td>-</td><td>Tr</td><td>30.5C</td><td>10mm</td><td>20%</td><td>-</td><td>Tr</td><td>30.5C</td></body></html>'
        mock_etree.return_value.xpath.return_value = [MagicMock(text='10mm'), MagicMock(text='20%'), MagicMock(text='-'), MagicMock(text='Tr'), MagicMock(text='30.5C'), MagicMock(text='10mm'), MagicMock(text='20%'), MagicMock(text='-'), MagicMock(text='Tr'), MagicMock(text='30.5C')]
        years = [1, 0]
        days = [10, 5]
        filename = "test.csv"
        data2csv(years, days, filename)
        mock_open.assert_called_once_with("db/test.csv", 'w', newline='')
        handle = mock_open()
        handle.write.assert_called()
        handle.writelines.assert_called()

if __name__ == '__main__':
    unittest.main()