def clean_name(name):
    return "".join([c for c in name if c.isalpha()])


def req_json(endpoint):
    import requests
    url = f"http://localhost:8000/api/{endpoint}"
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    return response


def last_info(attribute, search, data):
    # busca por todas as recorrencias do requerimento no json de acordo com slot preenchido e visibulidade
    req = [x for x in data if (
        x[attribute] == search and x["visivel"] == True)]
    # seleciona a primeira ocorrencia na lista ordenada
    req = req[0]
    return req
