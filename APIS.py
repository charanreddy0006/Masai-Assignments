import requests

def fetch_country_facts(country_names: list) -> dict:
    results = {}

    for country_name in country_names:
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            results[country_name] = {
                "name": data[0]["name"]["common"],
                "capital": data[0]["capital"][0],
                "population": data[0]["population"],
                "region": data[0]["region"]
            }

        elif response.status_code == 404:
            results[country_name] = "Country not found"

        else:
            results[country_name] = f"Error: {response.status_code}"

    return results


if __name__ == "__main__":
    countries = ["India", "France", "Wakanda", "Brazil"]

    result = fetch_country_facts(countries)

    for name, facts in result.items():
        print(f"{name}: {facts}")