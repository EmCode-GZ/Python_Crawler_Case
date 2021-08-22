import requests
import json

# http://scxk.nmpa.gov.cn:81/xk/
# 测试
#
# if __name__ == '__main__':
#     url = 'http://scxk.nmpa.gov.cn:81/xk/'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'
#     }
#
#     page_text = requests.get(url=url, headers=headers).text
#
#     with open('./huazhuang.html', 'w', encoding='utf-8') as fp:
#         fp.write(page_text)
#
# # http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=6321fa3a8cad4edba7b5597c3fdea52e
# # http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=c3854166c00f46b5b29fe2a55d3df929

if __name__ == '__main__':
    # 批量获取不同企业的ID值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
    }
    ID_list = []  # 存储企业ID
    all_data_list = []

    for page in range(1, 6):
        page = str(page)
        # 参数的封装
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
            }
        json_ID = requests.post(url=url, headers=headers, data=data).json()
        for dic in json_ID['list']:
            ID_list.append(dic['ID'])


    # 获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in ID_list:
        data = {
            'id': id
        }

        detail_json = requests.post(url=post_url, data=data, headers=headers).json()
        print(detail_json, '-----------------------ending-------------------')
        all_data_list.append(detail_json)

    # 持久化存储
    fp = open('./AllData.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('over!!')
