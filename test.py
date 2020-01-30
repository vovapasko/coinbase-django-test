import requests

headers = {
    'Authorization': 'Token _6ZFr1vZWkuW6HHoHe-Hap6QnnKxo8-u7YV3T3J7',
}

params = (
    ('order_id', '100'),
    ('price_amount', '15.23'),
    ('price_currency', 'BTC'),
    ('receive_currency', 'EUR'),
    ('receive_amount', '12')
)

response = requests.post('https://api-sandbox.coingate.com/v2/orders', headers=headers, params=params)
print(response.url)
print(response.json())
print(response.json()['errors'])

print(response.status_code)
# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://api.coingate.com/v2/orders?per_page=2&page=1&sort=created_at_desc', headers=headers)
