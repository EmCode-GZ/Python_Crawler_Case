import requests
import json

if __name__ == '__main__':
    # 指定url
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '1',
        'limit': '20',
    }
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    # get请求参数处理
    response = requests.get(url=url, params=param, headers=headers)

    list_data = response.json()
    print(list_data)
    # 持久化存储
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)

    print('over!!!')
