import requests

class APIHandler:

    base_url = "https://gorest.co.in/public/v2"
    user_endpoint = "/users"
    headers = {
        "Authorization": "Bearer ec35f44ea0dedd1727ded64288fb90653c6fbafff1ac34a1f52608b9124cee86"
    }

    def create_user(self, body, exppected_status_code = 201 ): #metoda przyjmujaca parametr o nazwie body
        res = requests.post(self.base_url+self.user_endpoint, json=body, headers=self.headers)
        assert res.status_code == exppected_status_code
        return res.json()


    def get_user_by_id(self, user_id, exppected_status_code = 200):
        res = requests.get(f"{self.base_url}{self.user_endpoint}/{user_id}", headers=self.headers)
        assert res.status_code == exppected_status_code
        return res.json()


    def update_user(self, user_id, body):
        pass

    def delete_user(self, user_id):
        pass


