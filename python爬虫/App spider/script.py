
import json
# 这个地方必须这么写 函数名：response
def response(flow):
    # 通过抓包软包软件获取请求的接口
    if 'aweme/v1/user/follower/list' in flow.request.url:
        # 数据的解析
        for user in json.loads(flow.response.text)['followers']:
            douyin_info = {}
            douyin_info['share_id'] = user['uid']
            douyin_info['douyin_id'] = user['short_id']
            douyin_info['nickname'] = user['nickname']
            print(douyin_info)