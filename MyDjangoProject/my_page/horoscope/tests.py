from django.test import TestCase
from . import views
from django.urls import reverse


class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
                      response.content.decode())
    # self.client.get('/horoscope/libra/').content.decode()


    def test_signs(self):
        for i in views.signs:
            s = reverse('horoscope-name', args=[i])
            response = self.client.get(s)
            self.assertEqual(response.status_code, 200)
            self.assertIn(views.signs[i],
                          response.content.decode())


    def test_libra_redirect(self):
        for i in range(12):
            s = reverse('int-sign', args=[i + 1])
            response = self.client.get(s)
            self.assertEqual(response.status_code, 302)
            s2 = views.zodiacs[i]
            s1 = reverse('horoscope-name', args=[s2])
            self.assertEqual(response.url, s1)


