from flask import Flask,request,jsonify
import requests

app=Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    source_currency=data['queryResult']['parameters']['unit-currency']['currency']
    amount=data['queryResult']['parameters']['unit-currency']['amount']
    target_currency=data['queryResult']['parameters']['currency-name']

    print(source_currency)
    print(amount)
    print(target_currency)

    cf=fetch_conversion_factor(source_currency,target_currency)
    final_amount=amount*cf

    response={'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)}


    return jsonify(response)

def fetch_conversion_factor(source,target):
    url = "https://api.apilayer.com/exchangerates_data/convert?to={}&from={}&amount=1&apikey=78j3AI7Waz9T9hraaW1J1PrPmLyUtEYS".format(target,source)

    response=requests.get(url)
    response=response.json()
    response=response['info']['rate']
    return response

if __name__=="__main__":
    app.run(debug=True)