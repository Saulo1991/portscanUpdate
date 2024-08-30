import requests
from bs4 import BeautifulSoup

# List of characters to test in inputs
bad_char = ["'", "<", ">", "(", ")", ";"]

def spider_inputs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    form = soup.find('form')
    
    if not form:
        print('No form was found')
        return None
    
    inputs = form.find_all('input')
    input_names = [input.get('name') for input in inputs if input.get('name')]
    
    return input_names

def test_inputs(url, inputs):
    results = {}
    
    for input_name in inputs:
        for char in bad_char:
            payload = {input_name: char}
            try:
                response = requests.post(url, data=payload)
                results[input_name] = response.status_code
            except requests.RequestException as e:
                print(f"Request failed: {e}")
                results[input_name] = None
    
    return results

def main():
    url = input('Enter URL to scan: ')
    
    inputs = spider_inputs(url)
    if not inputs:
        return
    
    results = test_inputs(url, inputs)
    for key, value in results.items():
        print(f'Input field "{key}" responded with status code {value}')
        
if __name__ == '__main__':
    main()
