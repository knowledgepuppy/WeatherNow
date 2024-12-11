import unittest
from unittest.mock import patch, Mock
from GetData import GetData

class TestGetData(unittest.TestCase):

    @patch('requests.get')
    def test_get_success(self, mock_get):
        # Arrange
        url = "http://example.com"
        expected_content = "Example content"
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content.decode.return_value = expected_content
        mock_get.return_value = mock_response

        get_data = GetData(url)

        # Act
        result = get_data.Get()

        # Assert
        self.assertEqual(result, expected_content)
        mock_get.assert_called_once_with(url=url, headers=get_data.headers)
        print("Test get_success passed.")

    @patch('requests.get')
    def test_get_failure(self, mock_get):
        # Arrange
        url = "http://example.com"
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.content.decode.return_value = "Not Found"
        mock_get.return_value = mock_response

        get_data = GetData(url)

        # Act
        result = get_data.Get()

        # Assert
        self.assertEqual(result, "Not Found")
        mock_get.assert_called_once_with(url=url, headers=get_data.headers)
        print("Test get_failure passed.")

if __name__ == '__main__':
    unittest.main()