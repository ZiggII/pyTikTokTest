import requests

headers_by_me = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'referer': "https://www.tiktok.com/"
    }
request = requests.get("https://p77-sign-va.tiktokcdn.com/tos-maliva-avt-0068/df0efa9bc4469899e2a4da0501de49e3~c5_100x100.jpeg?x-expires=1672578000&x-signature=hdbFX0Zw635bhMXc9lO%2BD3vikAU%3D", headers= headers_by_me)

with open("image_shakes_and_fidget.png", "wb") as image:
    image.write(request.content)