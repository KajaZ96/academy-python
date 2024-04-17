import unittest
import requests
from faker import Faker  # importowanie nowej biblioteki
from src.gorest_handler import APIHandler


class GoRestTest(unittest.TestCase):

    def setUp(self) -> None:
        self.api_handler = APIHandler()

    def test_create_user(self):
        body = {
            "name": Faker().name(), # obiekt typu Faker i wywołanie na nim metody, dzięki nawiasą tworzenie nowych obiektów
            "gender": "male",
            "email": Faker().email(),
            "status": "active"
        }

        res_body = self.api_handler.create_user(body) #tworzenie użytkownika z body ze słownika
        self.assertEqual(int, type(res_body["id"]))  #sprawdzenie, czy id istnieje
        # self.assertDictContainsSubset(body, res_body)
        res_body = self.api_handler.get_user_by_id(res_body["id"]) #wysłanie prośby o pobranie tego użytkownika
        self.assertDictContainsSubset(body, res_body)
    def test_invalid_user_creation(self):
        body = {
            "name": Faker().name(),
            "gender": "male",
            "email": Faker().name(),
            "status": "active"
        }
        self.api_handler.create_user(body, exppected_status_code=422)

    def test_e2e_flow(self):
        self.api_handler.create_user()
        self.api_handler.get_user_by_id()
        self.api_handler.update_user()
        self.api_handler.get_user_by_id()
        self.api_handler.delete_user()
        self.api_handler.get_user_by_id()



if __name__ == '__main__':
    unittest.main()
