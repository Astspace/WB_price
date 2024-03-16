import requests

cookies = {
    'BasketUID': '1789c197d1a3447e804361d440b7e316',
    '__wba_s': '1',
    '_wbauid': '9265152331710593349',
    '___wbu': '2687a62e-4f1c-4e64-b369-c9896264c8ac.1710593349',
    '___wbs': '8c27e7d2-1ed5-44ef-b616-cad69847618b.1710593349',
}

headers = {
    'authority': 'www.wildberries.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'BasketUID=1789c197d1a3447e804361d440b7e316; __wba_s=1; _wbauid=9265152331710593349; ___wbu=2687a62e-4f1c-4e64-b369-c9896264c8ac.1710593349; ___wbs=8c27e7d2-1ed5-44ef-b616-cad69847618b.1710593349',
    'referer': 'https://www.wildberries.ru/catalog/156549910/detail.aspx',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-spa-version': '9.4.24',
}

params = {
    'subject': '3274',
    'kind': '0',
    'brand': '27445',
}

response = requests.get(
    'https://www.wildberries.ru/webapi/product/156549910/data',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.status_code)
print(response.json())