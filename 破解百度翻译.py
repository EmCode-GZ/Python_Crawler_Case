import requests
import json

if __name__ == '__main__':
    # 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    # post请求参数处理(同get一致)
    word = input('enter a word:')
    data = {
        'kw': word
    }
    # 请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取相应数据:json方法返回的是obj(如果确认响应数据是json类型的，才可以使用json)
    dic_obj = response.json()
    # 进行持久化存储
    filename = word + '.json'
    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print('over!')
