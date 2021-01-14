def script(**kwargs):
    import requests

    if kwargs["PARM"]:
        number = kwargs["PARM"]
    else:
        from random import randrange
        number = randrange(1, 898)

    url = f"http://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(url=url)
    json_response = response.json()
    name = json_response["forms"][0]["name"]
    name = str(name).title()
    image = json_response["sprites"]["front_default"]
    binds = {}
    binds["name"] = name
    binds["image"] = image
    return binds


if __name__ == '__main__':
    a = script()
    print(a)
    print(f'{name} - {image}' % a)
