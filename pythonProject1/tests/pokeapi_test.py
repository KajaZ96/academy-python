import unittest

import requests


class PokeAPITests(unittest.TestCase):

    base_url = "https://pokeapi.co/api/v2/pokemon"
    def test_default_list_pokemons(self):
        res = requests.get(self.base_url)
        res_json = res.json()
        self.assertTrue(res_json)                          #sprawdzanie formatu json
        self.assertEqual(200, res.status_code)        #sprawdzanie statusu kodu
        self.assertEqual(1302, res_json["count"])

    def test_pokemon_list_with_pagination(self):
        params = {
            "offset" : 20,
            "limit" : 10
        }
        res_json = requests.get(self.base_url, params=params).json()
        self.assertEqual(params["limit"], len(res_json["results"]))
        self.assertRegex(res_json["results"][0]["url"], ".*\/21\/.*") #1

        url = res_json["results"][0]["url"]
        id = url.split("/")[-2]
        self.assertEqual("21", id) #2
        self.assertIn("21", res_json["results"][0]["url"]) #3

if __name__ == '__main__':
    unittest.main()
