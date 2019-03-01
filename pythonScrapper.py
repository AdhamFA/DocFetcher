import bs4 as bs
import urllib.request


def read_python_lib():
    sauce = urllib.request.urlopen('https://docs.python.org/3/library/')
    soup = bs.BeautifulSoup(sauce, 'lxml')
    pylist_parent = soup.find('div', class_="toctree-wrapper compound")
    pylist = pylist_parent.find('ul')
    for li in pylist.find_all('li', class_="toctree-11"):
        print(li.text)


read_python_lib()
