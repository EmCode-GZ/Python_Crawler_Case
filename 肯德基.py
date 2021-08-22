import requests
import json

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'
    }
    # 指定请求url
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?'
    # post请求参数处理
    kw = input('enter a word:')
    # page=input('enter a number:')
    data = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '10',
        'op': 'keyword'
    }
    # 请求发送
    response = requests.post(url=post_url, headers=headers, params=data)

    page_text = response.text
    print(page_text)

    filename = './' + kw + '.text'

    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("over!!")
    #
    # list_data = response.json()
    # # page_text = response.text
    # print(list_data)
    #
    # # 进行持久化存储
    # filename = './' + kw + '.json'
    # with open(filename, 'w', encoding='utf-8') as fp:
    #     json.dump(list_data, fp=fp, ensure_ascii=False)
    #     print('success!!!')
