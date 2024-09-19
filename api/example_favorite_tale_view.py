from mixer.backend.django import mixer

from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from openai_app.models import Tale
from shop_app.models import TalePackageShop

User = get_user_model()


class TestFavoriteTaleViewTestCase(APITestCase):
    """ Тест добавления сказки в избранное """

    def setUp(self):
        self.user_1 = mixer.blend(User)
        self.user_2 = mixer.blend(User)
        self.client.force_authenticate(user=self.user_1)
        self.tale_1 = mixer.blend(Tale, user=self.user_1,
                                  published=Tale.PERSONAL, status=Tale.COMPLETED)
        self.tale_2 = mixer.blend(Tale, user=self.user_2,
                                  published=Tale.PUBLIC, status=Tale.COMPLETED)
        self.tale_3 = mixer.blend(Tale, user=self.user_2,
                                  published=Tale.PERSONAL, status=Tale.COMPLETED)

    def test_add_my_tale_to_favorite(self):
        """
        Добавляем свою сказку в избранное.
        Удаляем свою сказку из избранного.
        """
        url = reverse('api_v1:add_tale_to_favorite')
        request_data = {
            'tale_id': self.tale_1.pk
        }
        self.assertEqual(self.user_1.favorite_tales.count(), 0)

        # Добавляем сказку в избранное
        response = self.client.post(url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(self.user_1.favorite_tales.count(), 1)

        # Удаляем сказку из избранного
        response = self.client.post(url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(self.user_1.favorite_tales.count(), 0)

    def test_add_our_tale_to_favorite(self):
        """
        Добавляем пользователю доступ в ленту.
        Добавляем чужую сказку в избранное.
        Удаляем чужую сказку из избранного.
        """
        # Добавляем пользователю доступ в ленту.

        tale_package_shop = mixer.blend(
            TalePackageShop,
            tales_count=1,
            tale_balance=self.user_1.tale_balance,
            feed_days_count=10
        )
        tale_package_shop.is_paid = True
        tale_package_shop.save()

        url = reverse('api_v1:add_tale_to_favorite')
        request_data = {
            'tale_id': self.tale_2.pk
        }
        self.assertEqual(self.user_1.favorite_tales.count(), 0)

        # Добавляем чужую в избранное
        response = self.client.post(url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(self.user_1.favorite_tales.count(), 1)

        # Удаляем чужую из избранного
        response = self.client.post(url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(self.user_1.favorite_tales.count(), 0)

    def test_add_our_tale_to_favorite_without_access_to_feed(self):
        """
        Пытаемся добавить чужую сказку в избранное без доступа к ленте.
        """

        url = reverse('api_v1:add_tale_to_favorite')
        request_data = {
            'tale_id': self.tale_2.pk
        }
        self.assertEqual(self.user_1.favorite_tales.count(), 0)

        # Добавляем чужую в избранное
        response = self.client.post(url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.assertEqual(self.user_1.favorite_tales.count(), 0)

    def test_tale_not_exist(self):
        """
        Пытаемся добавить несуществующую сказку в избранное
        """

        url = reverse('api_v1:add_tale_to_favorite')
        request_data = {
            'tale_id': self.tale_2.pk + 100
        }
        self.assertEqual(self.user_1.favorite_tales.count(), 0)

        # Добавляем чужую в избранное
        response = self.client.post(url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        self.assertEqual(self.user_1.favorite_tales.count(), 0)

    def test_add_personal_tale(self):
        """
        Пытаемся добавить чужую личную сказку в избранное
        """
        # Добавляем пользователю доступ в ленту.

        tale_package_shop = mixer.blend(
            TalePackageShop,
            tales_count=1,
            tale_balance=self.user_1.tale_balance,
            feed_days_count=10
        )
        tale_package_shop.is_paid = True
        tale_package_shop.save()

        url = reverse('api_v1:add_tale_to_favorite')
        request_data = {
            'tale_id': self.tale_3.pk
        }
        self.assertEqual(self.user_1.favorite_tales.count(), 0)

        # Добавляем чужую в избранное
        response = self.client.post(url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.assertEqual(self.user_1.favorite_tales.count(), 0)
