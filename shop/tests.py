from django.test import TestCase
from .models import Product
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

class ProductTest(TestCase):
    def test_get_products(self):
        upload = SimpleUploadedFile('test.jpg', content=b'file_content', content_type='image/jpeg')
        product_one = Product.objects.create(
            name='nike 1',
            slug='nike_1',
            image=upload,
            description='desc',
            price=1.0,
            stock=3,
            category=1
        )
        product_two = Product.objects.create(
            name='nike 2',
            slug=2,
            image=upload,
            description='desc2',
            price=5.0,
            stock=5,
            category=2
        )
        resp = self.client.get(reverse('shop:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['products'].count(), 2)
        self.assertContains(resp, product_one)
        self.assertContains(resp, product_two)