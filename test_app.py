import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('requests.get')
    def test_get_recommendations_valid_user(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'recommended_articles': [{'article_id': 'Article 1'}, {'article_id': 'Article 2'}, {'article_id': 'Article 3'}]
        }
        mock_get.return_value = mock_response

        response = self.app.post('/', data={'userid': '123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Utilisateur dont l\'user_id est : 123', response.data.decode('utf-8'))
        self.assertIn('Article 1', response.data.decode('utf-8'))
        self.assertIn('Article 2', response.data.decode('utf-8'))
        self.assertIn('Article 3', response.data.decode('utf-8'))

    @patch('requests.get')
    def test_get_recommendations_no_articles(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'recommended_articles': []}
        mock_get.return_value = mock_response

        response = self.app.post('/', data={'userid': '456'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Utilisateur dont l\'user_id est : 456', response.data.decode('utf-8'))
        self.assertIn('Aucune recommandation trouvée pour cet utilisateur.', response.data.decode('utf-8'))

    @patch('requests.get')
    def test_get_recommendations_api_error(self, mock_get):
        mock_get.side_effect = Exception('API error')

        response = self.app.post('/', data={'userid': '123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Aucune recommandation trouvée pour cet utilisateur.', response.data.decode('utf-8'))

    def test_get_recommendations_invalid_input(self):
        response = self.app.post('/', data={'userid': 'abc'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('ID utilisateur non valide.', response.data.decode('utf-8'))

    def test_get_recommendations_get_request(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Entrez votre ID utilisateur', response.data.decode('utf-8'))
        self.assertIn('Livre', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
