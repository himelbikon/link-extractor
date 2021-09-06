from bs4 import BeautifulSoup
import requests, pandas


host = 'https://bdebooks.com/'
urls = set()


def extractor(url):
	global urls
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'lxml')

	a_tags = soup.find_all('a')
	for a in a_tags:
		link = a.get('href')
		if link is not None and host[:-2] in link[0: len(host)] and not link in urls:
			urls.add(link)
			print(f'[{len(urls)}] {link}')
			extractor(link)



def main():
	print('\n---------- Starting ---------')

	urls.add(host)
	print(f'[{len(urls)}] {host}')

	try:
		extractor(host)
	except Exception as e:
		print(e)

	df = pandas.DataFrame({'Links': list(urls)})
	df.to_excel('bdebooks pdf links.xlsx', index=False, header=False)

	print('\n---------- Operation Ended ---------')



main()