import os

import requests
from bs4 import BeautifulSoup


def get_content(pg=1171355):
    url = f"http://www.shuyyw.cc/read/1102/{pg}.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    header = soup.find("h1").text
    header = header[header.index('正文') + 3:]
    print(pg, header)
    # print(soup.find(attrs={"id": "content"}).text)
    year_context = soup.find(attrs={"id": "content"}).contents

    join = '\n\t'.join(filter(lambda i: i != "", map(lambda x: x.text.strip(), year_context)))
    end_index = join.find("〖")
    if end_index == -1:
        end_index = join.find("本章结束")
    join = join[:end_index]
    # print(join)
    file_path = '一等家丁_第2032章.txt'
    content = header + '\n\t' + join.strip() + '\n\n'
    # print('content[2638]', content[2638])
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content)


if __name__ == "__main__":
    for i in range(1171355, 1171474):
        get_content(i)
    for i in range(3396900, 3396997):
        get_content(i)
    # get_content(1171401)
