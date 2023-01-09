import requests
from apikey import api_key
if __name__ == "__main__":
    # params = {"q": "Новосибирск", "appid": api_key, "units": "metric"}
    #
    response = requests.get("https://deployhoroscope.ru/")

    # print(response.status_code)
    # print(response.headers)
    print(response.text)
    # x = response.json()
    # print("погода", x["main"]["temp"])
    # print()

data = {
    "custname": "login",
    "custtel": "78882221122",
    "size": "medium",
    "topping": "bacon",
    "delivery": "",
    "comments": ""
}
params = {"q": "Новосибирск", "appid": api_key, "units": "metric"}
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Sec-Ch-Ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-638f469d-468cea8955157b2505cadb90"
  }

# veriable = requests.Session()
# rep = veriable.get("https://deployhoroscope.ru/")
# print(veriable.headers)
# response = veriable.post("https://esia.gosuslugi.ru/login/", headers=headers, data=data)
# print(rep.text)
# print(response.status_code)