import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?lang=fr"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["type"] == "single":
            print(f"😄 {data['joke']}")
        else:
            print(f"😄 {data['setup']}")
            print(f"➡️  {data['delivery']}")
    else:
        print("Erreur lors de la récupération de la blague.")

if __name__ == "__main__":
    get_joke()

