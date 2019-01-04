import urllib
import requests
import bs4

params      = dict()
_url        = "http://openapi.customs.go.kr/openapi/service/newTradestatistics/getitemtradeList?"

params["searchBgnDe"]   = "201001"
params["searchEndDe"]   = "201705"
params["searchItemCd"]  = "0803000000"
params["serviceKey"]    = "O3pn45WEu%2FBqli3ighFdTaTWSEI%2F1ujcAfNF0e46w%2BTpHSyunMKjHnErWxFw9t%2Fzrb5htgLVe4CYySaHqJoYyQ%3D%3D"

fullUrl =   _url +\
            "searchBgnDe"   + "=" + params["searchBgnDe"]   + "&" +\
            "searchEndDe"   + "=" + params["searchEndDe"]   + "&" +\
            "searchItemCd"  + "=" + params["searchItemCd"]  + "&" +\
            "serviceKey"    + "=" + params["serviceKey"]

htmlStr = urllib.request.urlopen(fullUrl).read().decode('utf-8')

soup    = bs4.BeautifulSoup(htmlStr, "html.parser")

print(fullUrl)


# testUrl = "http://openapi.customs.go.kr/openapi/service/newTradestatistics/getkindtradeList?serviceKey=O3pn45WEu%2FBqli3ighFdTaTWSEI%2F1ujcAfNF0e46w%2BTpHSyunMKjHnErWxFw9t%2Fzrb5htgLVe4CYySaHqJoYyQ%3D%3D"
# rlt = urllib.request.urlopen(testUrl).read().decode('utf-8')
#
# soup = bs4.BeautifulSoup(rlt,"html.parser")
#
# rltList = soup.findAll('cnt')
# print(rltList[0].text)

# print (serviceKey)
