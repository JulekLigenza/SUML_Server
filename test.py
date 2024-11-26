import requests


url = "http://127.0.0.1:5000/predict"


data = {
    "RAM": 16,
    "Storage": 512,
    "Screen": 15.6,
    "Brand": "Dell",
    "CPU": "Intel Core i7",
    "GPU": "NVIDIA GTX 1650",
    "Storage type": "SSD",
    "Status": "New",
    "Model": "XPS 15"
}

try:

    response = requests.post(url, json=data)


    if response.status_code == 200:
        print("Test passed! Server responded successfully.")
        print("Predictions:", response.json())
    else:
        print(f"Test failed with status code {response.status_code}")
        print("Error:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Test failed: {e}")
