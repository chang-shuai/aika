from bs4 import BeautifulSoup
import requests
import json

def start_requests():
	data = read_series_json()
	for factory_name, series_info in data.items():
		for series_id, series_name in series_info.items():
			serirs_url = "http://newcar.xcar.com.cn/%s/review.htm" %(series_id)
			parse(serirs_url)
			print(series_id, series_name)
def parse(serirs_url):

	pass
def check_url(serirs_url):
	r = requests.get(serirs_url, allow_redirects=False)
	code = r.status_code
	print(code)
	if 200 != code:
		return False
	else:
		soup = BeautifulSoup(r.text, "lxml")
		element = soup.find("div", class_="alibi_wrap")
		print(element)

def read_series_json():
	f = open("series_info.json", "r", encoding="utf-8")
	return json.load(f)

def main():
	check_url("http://newcar.xcar.com.cn/2590/review.htm")

if __name__ == '__main__':
	main()