from bs4 import BeautifulSoup
import requests
import lxml
'''
cookies = {
    'qrator_ssid': '1680078281.190.cAbrmCmwLztZoSBI-khp3rii0778nij1rkbd1np0nc9pbnlei',
    'stest201': '0',
    'stest207': 'acc0',
    'stest209': 'ct2',
    'PHPSESSID': 'ba90695145b7bed8a146d83d8c5e2e41',
    'user_public_id': 'lz3Xq5z1qlOFkGZoeQgbQQxe%2B4HJPW4LJx21F4O6tbndNnYkT5kugTL1nzeRG3U%2F',
    '_gcl_au': '1.1.1163793153.1680078282',
    '_ym_uid': '1680078283262722222',
    '_ym_d': '1680078283',
    '_gid': 'GA1.2.1883685710.1680078283',
    'tmr_lvid': '83f0d5a00d677a374477e424c04129fe',
    'tmr_lvidTS': '1680078282725',
    '_ym_isad': '2',
    'afUserId': 'c652460a-678f-4506-9ba3-0c0aeb741b95-p',
    'AF_SYNC': '1680078283807',
    '_ym_visorc': 'b',
    'adrdel': '1',
    'adrcid': 'AttVDXQ4Op3SvF88531DPVQ',
    'tp_city_id': '38612',
    '_userGUID': '0:lftf8omo:8Zy4iiPmfYGo06GtXMoHCXlOtxmAmidn',
    'c2d_widget_id': '{%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%206a1e802425dd9f8ad2cb%22}',
    'dSesn': 'd77a4102-d468-c4ad-0556-6e75154effcb',
    '_dvs': '0:lftf8omo:yH2kk~~E3lQb5xaiTqeFAAyHxAXwIKkL',
    'promo1000closed': 'true',
    'pageviewTimerFired15': 'true',
    'pageviewTimerFired30': 'true',
    'pageviewTimerFired60': 'true',
    'visitedPagesNumber': '4',
    '_ga_RD4H4CBNJ3': 'GS1.1.1680078282.1.1.1680078639.2.0.0',
    '_ga': 'GA1.1.1231898450.1680078282',
    'mindboxDeviceUUID': 'bdb4d12d-c9b6-4539-bf95-956e83f53b9a',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22bdb4d12d-c9b6-4539-bf95-956e83f53b9a%22%7D',
    'tmr_detect': '0%7C1680078646953',
    'qrator_jsid': '1680078280.359.LNxy8b1LwQOVYjyj-1lltu0sjulansvtmf18kb0kpv9jljftn',
    'pageviewTimer': '669.9490000000001',
}

headers = {
    'authority': 'krasnodar.technopark.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'qrator_ssid=1680078281.190.cAbrmCmwLztZoSBI-khp3rii0778nij1rkbd1np0nc9pbnlei; stest201=0; stest207=acc0; stest209=ct2; PHPSESSID=ba90695145b7bed8a146d83d8c5e2e41; user_public_id=lz3Xq5z1qlOFkGZoeQgbQQxe%2B4HJPW4LJx21F4O6tbndNnYkT5kugTL1nzeRG3U%2F; _gcl_au=1.1.1163793153.1680078282; _ym_uid=1680078283262722222; _ym_d=1680078283; _gid=GA1.2.1883685710.1680078283; tmr_lvid=83f0d5a00d677a374477e424c04129fe; tmr_lvidTS=1680078282725; _ym_isad=2; afUserId=c652460a-678f-4506-9ba3-0c0aeb741b95-p; AF_SYNC=1680078283807; _ym_visorc=b; adrdel=1; adrcid=AttVDXQ4Op3SvF88531DPVQ; tp_city_id=38612; _userGUID=0:lftf8omo:8Zy4iiPmfYGo06GtXMoHCXlOtxmAmidn; c2d_widget_id={%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%206a1e802425dd9f8ad2cb%22}; dSesn=d77a4102-d468-c4ad-0556-6e75154effcb; _dvs=0:lftf8omo:yH2kk~~E3lQb5xaiTqeFAAyHxAXwIKkL; promo1000closed=true; pageviewTimerFired15=true; pageviewTimerFired30=true; pageviewTimerFired60=true; visitedPagesNumber=4; _ga_RD4H4CBNJ3=GS1.1.1680078282.1.1.1680078639.2.0.0; _ga=GA1.1.1231898450.1680078282; mindboxDeviceUUID=bdb4d12d-c9b6-4539-bf95-956e83f53b9a; directCrm-session=%7B%22deviceGuid%22%3A%22bdb4d12d-c9b6-4539-bf95-956e83f53b9a%22%7D; tmr_detect=0%7C1680078646953; qrator_jsid=1680078280.359.LNxy8b1LwQOVYjyj-1lltu0sjulansvtmf18kb0kpv9jljftn; pageviewTimer=669.9490000000001',
    'if-none-match': '"1444c7-h9pnkSoE7aNobrqRkm36+ZEayTA"',
    'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
}

response = requests.get('https://krasnodar.technopark.ru/smartfony/', cookies=cookies, headers=headers)

with open("technopark.html","w", encoding="UTF-8" ) as f:
    f.write(response.text)'''
with open("C:\\Users\\user\\Documents\\Parsing\\technopark.html","w",encoding='UTF-8') as f:
    page1 = f.read()
    soup = BeautifulSoup(page1,'lxml')
    countainer = soup.find('div', 'product-card-big-countainer')
    card = countainer.find_all('div','product-card-big__countainer')
    for c in card:
        name = c.find('div','product-card-big__name').text
        print(name)