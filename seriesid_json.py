import requests
from bs4 import BeautifulSoup
import json

def get_source_code():
	"""获取车系页面的源代码"""
	r = requests.get("http://newcar.xcar.com.cn/price/")
	return BeautifulSoup(r.text, "lxml")

def get_series_by_brand(source, brand_id):
	"""根据品牌的id属性,获取此品牌下的所有车系的id"""
	brand = source.find(id=brand_id)
	series_info = brand.next_sibling.next_sibling
	factorys = series_info.find_all("div", class_="column_content")
	factorys_dict = {}
	for f in factorys:
		factory_name = f.find(class_="tit").get_text()
		items = f.find_all("div", class_="item_list")
		series_dict = {}
		for item in items:
			a = item.find("a")
			series_id = a["href"].replace("/","")
			series_name = a["title"]
			series_dict[series_id] = series_name
		factorys_dict[factory_name] = series_dict
	return factorys_dict

def write_json(factorys_dict):
	f = open("series_info.json", "w", encoding="utf-8")
	json.dump(factorys_dict, f, ensure_ascii=False)


def main():
	source = get_source_code()
	factorys_dict1 = get_series_by_brand(source, "brand_1")
	factorys_dict2 = get_series_by_brand(source, "brand_2")
	factorys_dict3 = get_series_by_brand(source, "brand_3")
	factorys_dict4 = get_series_by_brand(source, "brand_4")
	factorys_dict1.update(factorys_dict2)
	factorys_dict1.update(factorys_dict3)
	factorys_dict1.update(factorys_dict4)

	write_json(factorys_dict1)


if __name__ == '__main__':
	main()
