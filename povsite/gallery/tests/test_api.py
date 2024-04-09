from django.urls import reverse
from rest_framework.test import APITestCase


class GalleryApiTestCase(APITestCase):

    def test_get(self):
        """
        Этот код определяет тест с именем test_get в классе GalleryApiTestCase.
        Он выполняет запрос GET к URL-адресу «списка галереи», проверяет, равен ли код состояния ответа 200
        """
        url = reverse('gallery-list')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code, response)
