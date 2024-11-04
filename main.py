import os.path
import datetime
import poimage
import requests
from parsel import Selector
from config import url, headers, ROOT_PATH


# 支持jpg、png等所有图片格式
def process_image(input_image, output_image):
    poimage.del_watermark(
        input_image=input_image,
        output_image=output_image)


def get_article_image_url(url):
    try:
        resp = requests.get(
            url=url,
            headers=headers
        )
    except Exception as e:

        return []

    response = Selector(text=resp.text)

    img_list = response.xpath('//img/@data-src').extract()
    return img_list


def download(url, path, filename):
    full_path = os.path.join(path, filename)
    binary = requests.get(url, headers=headers).content
    with open(full_path, 'wb') as f:
        f.write(binary)
    target_path = os.path.join(path, f'processed-{filename}')
    process_image(full_path, target_path)


def main():
    img_list = get_article_image_url(url)
    current_date = datetime.datetime.now().strftime('%Y%m%d%H%M')
    folder = os.path.join(ROOT_PATH, current_date)
    if not os.path.exists(folder):
        os.makedirs(folder)

    for index, img_url in enumerate(img_list):
        print('downing image ',img_url)
        try:
            download(img_url, folder, f'{index}.png')
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
