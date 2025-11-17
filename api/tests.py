from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse("books-list")

    def test_list_books(self):
        """Testa listar livros com paginação"""

        Book.objects.create(title="Livro 1", author="Autor 1", price=10.50)

        response = self.client.get(self.list_url)

        # Verifica status HTTP
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica estrutura da paginação
        self.assertIn("count", response.data)
        self.assertIn("results", response.data)

        # Deve haver exatamente 1 livro
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(len(response.data["results"]), 1)

    def test_create_book(self):
        """Testa criar um livro via POST"""

        data = {"title": "Novo Livro", "author": "Autor X", "price": "25.90"}
        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.first().title, "Novo Livro")

    def test_retrieve_book(self):
        """Testa detalhe de um livro"""

        book = Book.objects.create(title="Livro A", author="Autor A", price=30.00)

        url = reverse("books-detail", args=[book.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Livro A")

    def test_update_book(self):
        """Testa atualizar um livro via PUT"""

        book = Book.objects.create(title="Original", author="Autor", price=50.00)

        url = reverse("books-detail", args=[book.id])
        data = {"title": "Atualizado", "author": "Autor", "price": "50.00"}

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, "Atualizado")

    def test_delete_book(self):
        """Testa deletar um livro"""

        book = Book.objects.create(title="AAA", author="BBB", price=10.00)

        url = reverse("books-detail", args=[book.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
