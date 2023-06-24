from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack

class SnacksTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='testpassword')
        Snack.objects.create(name='Chips', purchaser=user, desc='Delicious salty snack')

    def test_snack_model_string_representation(self):
        snack = Snack.objects.get(id=1)
        expected_name = snack.name
        self.assertEqual(str(snack), expected_name)

    def test_snack_defaults(self):
        snack = Snack.objects.get(id=1)
        self.assertEqual(snack.desc, 'Delicious salty snack')
        self.assertEqual(snack.image.url, '/static/default.jpg')

    def test_list_page_status_code(self):
        url = reverse('snack-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snack-list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('snack-list')
        response = self.client.get(url)
        snack_list = response.context['snacks']
        self.assertEqual(len(snack_list), 1)
        self.assertEqual(snack_list[0].name, "Chips")
        self.assertEqual(snack_list[0].desc, "Delicious salty snack")
        self.assertEqual(snack_list[0].purchaser.username, "testuser")

    def test_detail_page_status_code(self):
        url = reverse('snack-detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snack-detail', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('snack-detail', args=(1,))
        response = self.client.get(url)
        snack = response.context['snack']
        self.assertEqual(snack.name, "Chips")
        self.assertEqual(snack.desc, "Delicious salty snack")
        self.assertEqual(snack.purchaser.username, "testuser")
