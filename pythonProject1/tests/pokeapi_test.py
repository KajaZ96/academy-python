import unittest

import requests

from src.api_handler import APIHandler

class PokeAPITests(unittest.TestCase):

    def setUp(self) -> None:
        self.api_handler = APIHandler()
    def test_default_list_pokemons(self):
    #     res = requests.get(self.base_url)
    #     res_json = res.json()
    #     self.assertTrue(res_json)                          #sprawdzanie formatu json
    #     self.assertEqual(200, res.status_code)        #sprawdzanie statusu kodu
        res_json = self.api_handler.get_list_of_pokemons()
        self.assertEqual(1302, res_json["count"])

    def test_pokemon_list_with_pagination(self):
        params = {
            "limit" : 10,
            "offset" : 20
        }
        # res_json = requests.get(self.base_url, params=params).json()

        res_json = self.api_handler.get_list_of_pokemons(params)
        self.assertEqual(params["limit"], len(res_json["results"]))
        self.assertRegex(res_json["results"][0]["url"], f".*\/{params["offset"] + 1}\/.*") #1

        # url = res_json["results"][0]["url"]
        # id = url.split("/")[-2]
        # self.assertEqual("21", id) #2
        # self.assertIn("21", res_json["results"][0]["url"]) #3

    def test_shapes_and_ids(self):
        res_json = self.api_handler.get_list_of_shapes()
        self.assertEqual(res_json["count"], len(res_json["results"]))
        third_shape = res_json["results"][2]["name"]
        res_json = self.api_handler.get_shape_by_name(third_shape)
        self.assertEqual(3, res_json["id"])

if __name__ == '__main__':
    unittest.main()
