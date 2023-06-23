from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack


# Create your tests here.

class SnacksTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a snack
        Snack.objects.create(name='Chips', purchaser=user, desc='Delicious salty snack')

    def test_snack_str(self):
        snack = Snack.objects.get(id=1)
        expected_name = f'{snack.name}'
        self.assertEqual(str(snack), expected_name)

    def test_snack_defaults(self):
        snack = Snack.objects.get(id=1)
        self.assertEqual(snack.desc, 'Delicious salty snack')
        self.assertEqual(snack.image.url, 'static/default.jpg')
        
    def setUp(self):
        purchaser = get_user_model().objects.create(username="tester",password="tester")
        Snack.objects.create(name="rake", purchaser=purchaser)

    def test_list_page_status_code(self):
        url = reverse('Snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('Snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('Snacks')
        response = self.client.get(url)
        Snacks = response.context['Snacks']
        self.assertEqual(len(Snacks), 1)
        self.assertEqual(Snacks[0].name, "rake")
        self.assertEqual(Snacks[0].rating, 0)
        self.assertEqual(Snacks[0].purchaser.username, "tester")

    def test_detail_page_status_code(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_details.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        Snack = response.context['Snack']
        self.assertEqual(Snack.name, "rake")
        self.assertEqual(Snack.rating, 0)
        self.assertEqual(Snack.purchaser.username, "tester")
