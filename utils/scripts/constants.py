from pathlib import Path

MAIN_URl = 'http://start-opt.ru{}'

# xpath

CATEGORY_MAIN_LINK_XPATH = '//ul[@class="menu dropdown"]/li/a/@href'
GET_CATEGORY_NAME_XPATH = '//ul[@class="menu dropdown"]/li/a/span/text()'
GET_PRODUCTS_LINK_XPATH = '//div[@class="catalog_block items block_list"]/div//div[@class="item-title"]/a/@href'
PAGINATION_XPATH = '//div[@class="nums"]/a/@href'

# Product info

PRODUCT_TEXT_XPATH = '//div[@class="preview_text dotdot"]/text()'
PRODUCT_PRICE_XPATH = '//div[@class="price"]//span[@class="price_value" and position()=1]/text()'
PRODUCT_SIZE_XPATH = '//div[@class="char_line flex"]//text()'

BASE_DIR = Path(__file__).resolve().parent
