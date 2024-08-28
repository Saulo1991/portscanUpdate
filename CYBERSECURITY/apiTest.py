import requests

# Lista de códigos de status HTTP e suas descrições
status_codes = {
    100: "Continue",
    101: "Switching Protocols",
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    304: "Not Modified",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    408: "Request Timeout",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout"
}

def fetch_status_description(code):
    """Retorna a descrição do código de status HTTP."""
    return status_codes.get(code, "Desconhecido")

def fetch_cat_facts():
    """Faz uma requisição à API e imprime o código de status e descrição."""
    try:
        res = requests.get('https://meowfacts.herokuapp.com/')
        res.raise_for_status()  # Levanta um erro para status codes 4xx/5xx

        # Obtém o código de status e a descrição
        status_code = res.status_code
        description = fetch_status_description(status_code)
        
        print(f"Status Code: {status_code} - {description}")
        data = res.json()
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")

if __name__ == "__main__":
    fetch_cat_facts()
