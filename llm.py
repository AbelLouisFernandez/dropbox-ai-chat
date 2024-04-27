import requests

url = "http://localhost:8080"  # Make sure to include the protocol (http:// or https://)
query = "hello world"
data = {"query": query}

try:
    response = requests.post(url, json=data,timeout=100) # Adjust the timeout value as needed
    print(response.text)
except requests.exceptions.Timeout:
    print("Timeout occurred while connecting to the server")
except requests.exceptions.ConnectionError as e:
    print("Connection error:", e)
