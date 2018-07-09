# 사과 주산지 시군 재배 면적
import requests

#=========== 클래스 =====================================================
class Row:
	
	def __init__(self, place, area, realArea):
		self.place = place
		self.area = area
		self.realArea = realArea

##=========================================================================


years	= [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
months	= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 

# final_Result 	= list()
apple_List		= list()
tangerine_List	= list()
plum_List		= list()

params_create	= dict() # 재배지

URL_create = "http://kosis.kr/openapi/statisticsData.do?"

params_create["method"]			= "getList"
params_create["apiKey"]			= "OGZmODFkYWZhZDA5MWVmMzU0MzljM2YyZWRlN2EzZmE="
params_create["format"]			= "json"
params_create["jsonVD"]			= "Y"
params_create["userStatsId"]	= "yjw5344/101/DT_1ET0014/2/1/20170928003418"
params_create["prdSe"]			= "Y"

for year in years:

	params_create["startPrdDe"]	= str(year)
	params_create["endPrdDe"]	= str(year)

	fullUrl_create = URL_create +\
 			"method" 		+ "=" + params_create["method"]			+ "&" + \
        	"apiKey"		+ "=" + params_create["apiKey"]			+ "&" + \
            "format"		+ "=" + params_create["format"]			+ "&" + \
            "jsonVD"		+ "=" + params_create["jsonVD"]			+ "&" + \
            "userStatsId"	+ "=" + params_create["userStatsId"]	+ "&" + \
            "prdSe"			+ "=" + params_create["prdSe"]			+ "&" + \
            "startPrdDe"	+ "=" + params_create["startPrdDe"]		+ "&" + \
            "endPrdDe"		+ "=" + params_create["endPrdDe"]

	response = requests.get(fullUrl_create)
	targetJsonData = response.json()   # 해당 연도의 사과 자두 감귤의 재배지 면적의 JSON

	print(len(targetJsonData))

	for target in range(0, len(targetJsonData)+1):

		if target%6 == 0:
			apple_Place = targetJsonData[target]["C1_NM"]
			apple_Area	= targetJsonData[target]["DT"]
		elif target%6 == 1: #사과
			apple_RealArea	= targetJsonData[target]["DT"]
			Apple = Row(apple_Place, apple_Area, apple_RealArea)
			apple_List.append(Apple)
		
		elif target%6 == 2:
			tangerine_Place = targetJsonData[target]["C1_NM"]
			tangerine_Area	= targetJsonData[target]["DT"]
		elif target%6 == 3: #감귤
			tangerine_RealArea	= targetJsonData[target]["DT"]
			Tangerine = Row(tangerine_Place, tangerine_Area, tangerine_RealArea)
			tangerine_List.append(Tangerine)			
		
		elif target%6 == 4:
			plum_Place = targetJsonData[target]["C1_NM"]
			plum_Area	= targetJsonData[target]["DT"]
		elif target%6 == 5: # 자두
			plum_RealArea	= targetJsonData[target]["DT"]
			Plum = Row(plum_Place, plum_Area, plum_RealArea)
			plum_List.append(Plum)	




	# for month in months:

		

		

	# 	targetJsonData[0]["PRD_DE"]


		
	# 	final_Result.append( Row( ) )

		
		



print(apple_List)
print(plum_List)
print(tangerine_List)







#print(targetJsonData[0]["PRD_DE"])
#final_Result[]
