import json


def str_to_json(str_json):
    json_str = json.loads(str_json)
    return json_str


test_str = """
{
  "current_page": 1,
  "per_page": 2,
  "total_orders": 940,
  "total_pages": 470,
  "orders": [
    {
      "id": 1195862,
      "status": "new",
      "price_currency": "USD",
      "price_amount": "2000.0",
      "receive_currency": "EUR",
      "receive_amount": "",
      "created_at": "2018-04-25T13:28:16+00:00",
      "order_id": "111",
      "payment_url": "https://coingate.com/invoice/6003de09-ee9a-4584-be0e-5c0c71c5e497"
    },
    {
      "id": 1195824,
      "status": "paid",
      "price_currency": "EUR",
      "price_amount": "10.0",
      "pay_currency": "BTC",
      "pay_amount": "0.001281",
      "receive_currency": "EUR",
      "receive_amount": "9.9",
      "created_at": "2018-04-24T23:43:14+00:00",
      "expire_at": "2018-04-25T00:05:40+00:00",
      "payment_address": "38gmr5MujyDxcEhaqFfC5P9K6bhJo548gu",
      "order_id": "110",
      "payment_url": "https://coingate.com/invoice/4f5e5a63-5270-435d-bf05-eec369b0fdba"
    }
  ]
}"""

test = str_to_json(test_str)
print(test)
