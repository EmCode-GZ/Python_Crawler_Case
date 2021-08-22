import requests

# UA检测
# UA伪装
# UA：User-Agent(请求载体的身份标识)
if __name__ == "__main__":
    # UA伪装：将对应的user-agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }
    url = 'https://www.sogou.com/web?'
    # 处理url携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 对指定的url发起的请求是携带参数的，并且在请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text

    print(page_text)

    filename = kw + '.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename, 'succuss!!')
