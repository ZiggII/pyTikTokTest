from pytiktok import Tikvideo

Video = Tikvideo()


k = Video.tiktok("https://www.tiktok.com/@priyakaede/video/7173389471017110790?is_from_webapp=1&sender_device=pc0",True)

print(k["ok"])

print(k["link"])

