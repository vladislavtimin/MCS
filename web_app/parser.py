import urllib.request
from bs4 import BeautifulSoup


BASE_URL = 'http://www2.hm.com'
url_vars = {'Футболки и майки':'?product-type=men_extended_sizes_tshirt&sort=stock&offset=0&page-size=120',
            'Рубашки':'?product-type=men_extended_sizes_shirts&sort=stock&offset=0&page-size=90',
            'Кардиганы и джемперы':'?product-type=men_extended_sizes_hoodies&sort=stock&offset=0&page-size=150',
            'Брюки':'?product-type=men_extended_sizes_bottoms&sort=stock&offset=0&page-size=150',
            'Куртки и пальто':'?product-type=men_extended_sizes_jackets&sort=stock&offset=0&page-size=60',
            'Пиджаки и костюмы':'?product-type=men_extended_sizes_blazerssuits&sort=stock&offset=0&page-size=60',
            'Спортивная одежда':'?product-type=men_extended_sizes_sport&sort=stock&offset=0&page-size=60',
            'Белье':'?product-type=men_extended_sizes_underwear&sort=stock&offset=0&page-size=60'}


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def get_categories(html):
    soup = BeautifulSoup(html, "html.parser")
    categories = soup.find_all('li', class_='section-menu-subcategory')
    list_of_categories = []
    for category in categories:
        list_of_categories.append((category.find('a').attrs['href'], category.find('a').text.strip(),))
    return list_of_categories


def get_items(html):
    list_of_categories = get_categories(html)
    item_list = []
    for num in range(0,list_of_categories.__len__()):
        soup = BeautifulSoup(get_html(BASE_URL + list_of_categories[num][0] + url_vars[list_of_categories[num][1]]), "html.parser")
        rows = soup.find('div', class_='product-items-wrapper')
        for item in rows.find_all('a'):
            if item.text.strip() != '':
                item_list.append((list_of_categories[num][1], item.attrs['href']))
    return item_list


def parse(html):
    item_list = get_items(html)
    sorted_clothes = []
    category = item_list[0][0]
    clothes = []
    for num in range(0, item_list.__len__()):
        soup = BeautifulSoup(get_html(BASE_URL + item_list[num][1]), "html.parser")
        rows = soup.find('div', class_='row product-detail')
        print(num)
        if category != item_list[num][0]:
            sorted_clothes.append({
                category: clothes.copy(),
            })
            clothes.clear()
            category = item_list[num][0]
        clothes.append({
            'title': rows.find('h1', class_='product-item-headline').text.strip(),
            'price': int(rows.find('span', class_='price-value').text.strip().replace("\xa0","").split()[0]),
            'image': rows.find('div', class_='product-detail-main-image-container').img.attrs['src'][2:],
            'description': rows.find('p', class_='product-detail-description-text').text.strip(),
        })
        #print(clothes[num]['price'])
    sorted_clothes.append({
        category: clothes.copy(),
    })
    return sorted_clothes


def main():
    list_of_categories = []
    for category in (get_categories(get_html(BASE_URL + '/ru_ru/muzhchiny/vybrat-kategoriyu/extended-sizes.html'))):
        list_of_categories.append(category[1])
    list_of_clothes = (parse(get_html(BASE_URL + '/ru_ru/muzhchiny/vybrat-kategoriyu/extended-sizes.html')))
    #print(list_of_categories)
    #for item in list_of_clothes[7][list_of_categories[7]][1]:
    #    print(item)
    return list_of_categories, list_of_clothes

if __name__ == '__main__':
    main()