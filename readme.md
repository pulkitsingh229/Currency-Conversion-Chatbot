# Currency Conversion Chatbot

This is a simple Flask application that converts a specified amount from one currency to another using an external API. It is designed to be used as a chatbot that can be integrated with messaging platforms like Facebook Messenger or Telegram.

### **Installation**
To install the dependencies for this application, you can use pip:

pip install -r requirements.txt

### **Usage**
To start the application, you can run the following command:

python app.py

This will start the Flask development server and the application will be accessible at http://localhost:5000.

To use the chatbot, you can send a POST request to the application with the following JSON payload:

{
  "queryResult": {
    "parameters": {
      "unit-currency": {
        "amount": 100,
        "currency": "USD"
      },
      "currency-name": "EUR"
    }
  }
}

The amount key specifies the amount to be converted, and the currency key specifies the source currency. The currency-name key specifies the target currency.

The application will then use an external API to fetch the conversion rate between the source and target currencies, and return the converted amount in the response.

### **API Reference**

This application uses the apilayer Exchange Rates API to fetch the conversion rate between currencies. You will need to sign up for an API key to use this API.