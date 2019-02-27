import bs4 as bs
import urllib.request


def get_j8_class(j_class):
    sauce = urllib.request.urlopen('https://docs.oracle.com/javase/8/docs/api/allclasses-noframe.html').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    link = "classNotFound"
    for url in soup.find_all('a'):
        if j_class == url.string:
            link = "https://docs.oracle.com/javase/8/docs/api/" + url.get('href')
            break
    return link


def get_j7_class(j_class):
    sauce = urllib.request.urlopen('https://docs.oracle.com/javase/7/docs/api/allclasses-noframe.html').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    link = "classNotFound"
    for url in soup.find_all('a'):
        if j_class == url.string:
            link = "https://docs.oracle.com/javase/7/docs/api/" + url.get('href')
            break
    return link


def get_j11_class(j_class):
    sauce = urllib.request.urlopen('https://docs.oracle.com/en/java/javase/11/docs/api/allclasses.html').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    link = "classNotFound"
    for url in soup.find_all('a'):
        if j_class == url.string:
            link = "https://docs.oracle.com/en/java/javase/11/docs/api/" + url.get('href')
            break
    return link


# This function searches a link for methods and returns information about them
def get_method_information(method_requested, link):
    if link == "classNotFound":
        return "I was not able to find the class you referenced.\n\n^(I am a bot still in development." \
               " For questions or suggestions, you can message /u/ADhoom)"
    inner_sauce = urllib.request.urlopen(link)
    broth = bs.BeautifulSoup(inner_sauce, 'lxml')
    method_detail = broth.find("h3", text="Method Detail").find_parent('li')
    method_information = ""
    is_found = False
    for method in method_detail.find_all("ul", class_="blockList"):
        method_name = method.find("h4").text
        if method_name == method_requested:
            method_pre = method.find("pre").text
            method_desc = method.find("div", class_="block").text
            ref = method.previous_sibling.previous_sibling.name
            method_information += ("#Here's what I found about the **" + method_name + "** method:\n\n")
            method_information += "##" + broth.title.text + "\n\n"
            method_information += ("~~~\n" + method_pre + "\n~~~" "\n\n")
            method_information += ("\n\n" + method_desc + "\n\n")
            method_information += ("[Method Documentation Page](" + (link+ref) + ")\n\n")
            is_found = True
            break
    if is_found is False:
        method_information += "I was not able to find any information about **" + method_requested +\
                              "** in the oracle documentation.\n\n"
        method_information += "[Oracle Java 8 Documentation]("+link+")\n\n"
    method_information += "^(I am a bot still in development. For questions or suggestions, you can message /u/ADhoom)"
    return method_information


# This function searches the oracle java 11 api for a word a user wants and returns its information
def _java11_scrapper(j_class):
    sauce = urllib.request.urlopen('https://docs.oracle.com/en/java/javase/11/docs/api/allclasses.html').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    string = ""
    is_found = False
    for url in soup.find_all('a'):
        if j_class == url.string:
            link = "https://docs.oracle.com/en/java/javase/11/docs/api/" + url.get('href')
            inner_sauce = urllib.request.urlopen(link)
            broth = bs.BeautifulSoup(inner_sauce, 'lxml')
            string += ("#here's what I found about the **" + j_class + "** class:\n\n")
            string += "##Java 11\n\n"
            string += ("~~~\n" + broth.pre.text + "\n~~~" "\n\n")
            string += ("\n\n" + broth.find('div', class_='block').text + "\n\n")
            string += ("[Class Documentation Page](" + link + ")\n\n")
            is_found = True
            break
    if is_found is False:
        string += "I was not able to find any information about **" + j_class + "** in the oracle documentation.\n\n"
        string += "[Oracle Java 11 Documentation](https://docs.oracle.com/en/java/javase/11/docs/api/index.html)\n\n"

    string += "^(I am a bot still in development. For questions or suggestions, you can message /u/ADhoom)"
    return string


# This function searches the oracle java 8 api for a word a user wants and returns its information
def _java8_scrapper(j_class):
    sauce = urllib.request.urlopen('https://docs.oracle.com/javase/8/docs/api/allclasses-noframe.html').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    string = ""
    is_found = False
    for url in soup.find_all('a'):
        if j_class == url.string:
            link = "https://docs.oracle.com/javase/8/docs/api/" + url.get('href')
            inner_sauce = urllib.request.urlopen(link)
            broth = bs.BeautifulSoup(inner_sauce, 'lxml')
            string += ("#here's what I found about the **" + j_class + "** class:\n\n")
            string += "##Java 8\n\n"
            string += ("~~~\n" + broth.pre.text + "\n~~~" "\n\n")
            string += ("\n\n" + broth.find('div', class_='block').text + "\n\n")
            string += ("[Class Documentation Page](" + link + ")\n\n")
            is_found = True
            break
    if is_found is False:
        string += "I was not able to find any information about **" + j_class + "** in the oracle documentation.\n\n"
        string += "[Oracle Java 8 Documentation](https://docs.oracle.com/javase/8/docs/api/overview-summary.html)\n\n"

    string += "^(I am a bot still in development. For questions or suggestions, you can message /u/ADhoom)"
    return string


# This function searches the oracle java 7 api for a word a user wants and returns its information
def _java7_scrapper(j_class):
    sauce = urllib.request.urlopen('https://docs.oracle.com/javase/7/docs/api/allclasses-noframe.html').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    string = ""
    is_found = False
    for url in soup.find_all('a'):
        if j_class == url.string:
            link = "https://docs.oracle.com/javase/7/docs/api/" + url.get('href')
            inner_sauce = urllib.request.urlopen(link)
            broth = bs.BeautifulSoup(inner_sauce, 'lxml')
            string += ("#here's what I found about the **" + j_class + "** class:\n\n")
            string += "##Java 7\n\n"
            string += ("~~~\n" + broth.pre.text + "\n~~~" "\n\n")
            string += ("\n\n" + broth.find('div', class_='block').text + "\n\n")
            string += ("[Class Documentation Page](" + link + ")\n\n")
            is_found = True
            break
    if is_found is False:
        string += "I was not able to find any information about **" + j_class + "** in the oracle documentation.\n\n"
        string += "[Oracle Java 7 Documentation](https://docs.oracle.com/javase/7/docs/api/overview-summary.html)\n\n"

    string += "^(I am a bot still in development. For questions or suggestions, you can message /u/ADhoom)"
    return string


def search_jdk(version, java_class):
    if version == "java11" or version == "j11":
        return _java11_scrapper(java_class)
    elif version == "java8" or version == "j8" or version == "java":
        return _java8_scrapper(java_class)
    elif version == "java7" or version == "j7":
        return _java7_scrapper(java_class)
