from django.shortcuts import render, redirect
import requests

def index(request):
    if request.method == 'GET':
        print("Get Method Working")
    elif request.method == 'POST':
        url = "http://192.168.68.118:9000/api/v1/payment/create/"
        headers = {
            "API-KEY": "bVgVaxpaZ17IvlkDk_0jQUQ5J0EHJSyz85WRVcQ_5zg",
            "SECRET-KEY": "pbkdf2_sha256$1000000$WY7VZOf5cCVhd8Yc1J9Q5t$P2IJy0A05LXOknLp5qSYMRDypISfyuasJTOGv5clbSw="
        }
        # response = requests.post(url=url, headers=headers, data=request.POST)
        try:
            response = requests.post(url=url, headers=headers, data=request.POST)
            response_data = response.json()
            
            print("Response JSON:", response_data)
            
            payment_url = response_data.get("paymentURL")
            if payment_url:
                return redirect(payment_url)
            
        except requests.exceptions.RequestException as e:
            print("Error sending request:", e)
    return render(request, "index.html")
