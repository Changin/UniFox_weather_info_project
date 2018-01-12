# -*- coding:utf-8 -*-

#result = soup.find("code", class_="bash") #id와 class를 조합하여 찾을 수도 있다
#result = soup.find("A") #태그로 찾기 (첫번째)
#result = soup.find_all("A") #태그로 찾기 (모두)
#result = soup.find(id="AA") #id로 찾기

from bs4 import BeautifulSoup
import requests
import os

###---------------------------------------------------------------------------------------------###

#Entry point
def starter():
	select = selector()
	caller(select)

#unicode 문자 처리를 위한 새로운 print함수
def printRAW(*Text):
    RAWOut = open(1, 'w', encoding='utf8', closefd=False)
    print(*Text, file=RAWOut)
    RAWOut.flush()
    RAWOut.close()

#사용자에게 지역을 입력받아 리턴하는 함수
def selector():
	os.system('clear')
	printRAW("Input location (서울,일산) : ")
	select = input()
	os.system('clear')
	return select

#지역별 함수 인자값을 다르게 한 후, 함수를 호출해줌
def caller(select):
	url = "http://www.weather.go.kr/weather/forecast/timeseries.jsp?searchType=INTEREST"

	if (select == "서울"):
		url += "&wideCode=1100000000&cityCode=1117000000&dongCode=1117055500"
		location = "서울"

	elif (select == "일산"):
		url += "&wideCode=4100000000&cityCode=4128700000&dongCode=4128754000"
		location = "일산"

	else:
		printRAW("Input error")
		exit()

	printRAW("현재 "+location+" 기상현황을 불러오는 중입니다...")
	printWeather(url,location)

#날씨정보 출력 함수
def printWeather(url, location):
	req = requests.get(url)
	soup = BeautifulSoup(req.text,"html.parser")

	os.system('clear')

	weather = soup.find_all('img')[24].get('alt')								#기상
	temp = soup.find_all(class_="now_weather1_right")[0].get_text()				#기온
	wind = soup.find_all(class_="now_weather1_right")[1].get_text()				#풍향 및 풍속
	humidity = soup.find_all(class_="now_weather1_right")[2].get_text()			#습도
	precipitation = soup.find_all(class_="now_weather1_right")[3].get_text()	#강수량

	ment1 = "현재 "+location+"의 날씨는 "+weather+" 입니다.\n기온 : "+temp+"\n풍향 : "+wind+"\n습도 : "+humidity+"\n"
	ment2 = ""

	if (weather == "비" or weather == "눈"):
		ment1 += "강수량 : "+precipitation+"\n"
		ment2 = "외출할 때 우산이 필요할 것으로 보입니다."

	length = len(temp)-1
	if (int(temp[0:length]) <= 0):
		ment2 += "\n추우니 외출할 때 꼭 두꺼운 옷 챙기세요!\n"
	elif (int(temp[0:length]) <= 10):
		ment2 += "\n쌀쌀한 기온이니 외출할 때 따뜻한 옷 챙기세요!\n"
	elif (int(temp[0:length]) <= 20):
		ment2 += "\n가벼운 복장을 추천합니다.\n"
	else:
		ment2 += "\n상당히 더우니 시원한 복장을 추천합니다.\n"

	printRAW(ment1+ment2)

###---------------------------------------------------------------------------------------------###

starter()