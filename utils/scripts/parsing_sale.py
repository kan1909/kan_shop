import requests
from django.core.files import File
from parsel import Selector

from apps.categories.models import Category
from apps.products.models import ProductItem, Product, ProductImage
from utils.scripts.constants import (
    CATEGORY_MAIN_LINK_XPATH,
    MAIN_URl,
    GET_PRODUCTS_LINK_XPATH,
    PRODUCT_SIZE_XPATH,
    PRODUCT_PRICE_XPATH,
    PRODUCT_TEXT_XPATH,
    BASE_DIR,
)

COLOR_DICT = {
    'Черный': '#000000',
    'Бежевый': '#FFEDDA',
    'Красный': "#FF2626",
    'Фиолетовый': '#C400FF',
    'Серый': '#B2B1B9',
    'Белый': '#EEEEEE',
    'Цветные': '#FF7600',
    'Голубой': '#3DB2FF',
    'Синий': '#2D46B9',
    'Коричневый': '#C68B59',
    'Розовый': '#F037A5',
    'Желтый': '#FFE459',
}


def get_first_category(tree: Selector):
    all_category = tree.xpath('//a[@class="number"]/span[@itemprop="name"]/text()').extract()
    return all_category[0]


def get_middle_category(tree: Selector):
    all_category = tree.xpath('//a[@class="number"]/span[@itemprop="name"]/text()').extract()
    return all_category[1]


def pagination_function(tree):
    pagination = tree.xpath('//div[@class="module-pagination"]//a/@href').extract()[-1]
    total_page = pagination.split('=')[1]
    print(total_page)
    return int(total_page)


def product_articul(tree):
    title = tree.xpath('//div[@id="content"]//h1/text()').extract_first()
    try:
        split_title = title.split('-')[0]
        return split_title
    except Exception as e:
        split_title = title.split(' ')[0]
        return split_title


def get_color_item(tree):
    color_text = tree.xpath(PRODUCT_TEXT_XPATH).extract_first()
    split_text = color_text.split('/')[-1]
    try:
        return COLOR_DICT[split_text]
    except KeyError as e:
        return '#F9F9F9'


def get_image_data(tree: Selector):
    images = tree.xpath('//img[@class="xzoom-gallery"]/@src').extract()
    main_url = 'http://start-opt.ru/upload/resize_cache/iblock/{}'
    correct_image = []
    for image in images:
        refactor_image = image.split('/')
        change_size = refactor_image[5].split("_")
        change_size[0], change_size[1] = 400, 400
        img_index = refactor_image[4] + '/' + str(change_size[0]) + '_' + str(change_size[1]) + '_' + change_size[
            2] + '/' + refactor_image[6]
        formatting_url = main_url.format(img_index)
        img_data = requests.get(formatting_url).content
        filename = refactor_image[6]
        with open(f'{BASE_DIR}/Downloads/{filename}', 'wb') as handler:
            handler.write(img_data)
            correct_image.append(handler.name)
    return correct_image


def get_correct_price(tree):
    price: str = tree.xpath(PRODUCT_PRICE_XPATH).extract_first()
    remove_space = price.replace(' ', '')
    return int(remove_space)


def get_product_detail(product_detail, url):
    tree = Selector(text=product_detail)
    article_product = product_articul(tree)
    get_title = tree.xpath('//div[@id="content"]//h1/text()').extract_first()
    product_image = get_image_data(tree)
    product_size = tree.xpath(PRODUCT_SIZE_XPATH).extract()
    product_category_first = get_first_category(tree)
    product_category_middle = get_middle_category(tree)
    color = get_color_item(tree)
    size_chart = product_size[2]
    simple_size = product_size[6]
    product_text = tree.xpath(PRODUCT_TEXT_XPATH).extract_first()
    product_price = get_correct_price(tree)
    data = {
        'url': url,
        'article': article_product,
        'price': product_price,
        'description': product_text,
        'product_title': get_title,
        'color': color,
        'size_chart': size_chart.strip(),
        'size': simple_size.strip(),
        'product_category_first': product_category_first,
        'product_category_middle': product_category_middle,
        'product_image': [image for image in product_image]
    }
    print(data)
    main_category, create = Category.objects.get_or_create(title=data['product_category_first'])
    obj, create = Category.objects.get_or_create(title=data['product_category_middle'], parent=main_category)
    product_obj, create = Product.objects.get_or_create(article=data['article'], category=obj)
    product_items_obj = ProductItem.objects.create(
        title=data['product_title'],
        price=data['price'],
        product=product_obj,
        description=data['description'],
        size_chart=data['size_chart'],
        size=data['size'],
        quantity=100,
        color=data['color'],
    )
    counter = 1
    for image in data['product_image']:
        product_item_images = ProductImage(product_item=product_items_obj)
        product_item_images.image.save(f'product_image{counter}.jpg', File(open(image, 'rb')))
        counter += 1
    return get_title


def response_product_data(params_product):
    tree = Selector(text=params_product)
    get_products_link = tree.xpath(GET_PRODUCTS_LINK_XPATH).extract()
    for product_data in get_products_link:
        response_product = requests.get(MAIN_URl.format(product_data))
        send_request_product = get_product_detail(response_product.text, response_product.url)
    return get_products_link


def subcategory_woman(params_category, main_url):
    tree = Selector(text=params_category)
    total_page = pagination_function(tree)
    page_part = '?PAGEN_1={}'
    try:
        for page in range(1, total_page + 1):
            url_gener = main_url + page_part.format(page)
            response_pagination_data = requests.get(url_gener)
            send_request_all_data = response_product_data(response_pagination_data.text)
        return total_page
    except Exception as e:
        print("Parsing Sale is Done")


def main():
    response = requests.get('http://start-opt.ru/catalog/')
    tree = Selector(text=response.text)
    get_categories_main = tree.xpath(CATEGORY_MAIN_LINK_XPATH).extract()
    response_to_subcategory = requests.get(MAIN_URl.format(get_categories_main[4]))
    get_subname_category = subcategory_woman(response_to_subcategory.text, response_to_subcategory.url)
    return get_subname_category


main()
