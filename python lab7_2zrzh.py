import requests

# 配置参数（替换为你的News API Key）
NEWS_KEY = ''
NEWS_URL = 'https://newsapi.org/v2/everything'
NEWS_PARAMS = {
    'apiKey': NEWS_KEY,
    'q': '中国 新闻',
    'language': 'zh',
    'pageSize': 5,
    'sortBy': 'publishedat'
}

def get_china_news():
    """获取中文新闻"""
    try:
        # 发送请求并解析响应
        res = requests.get(NEWS_URL, params=NEWS_PARAMS)
        res.raise_for_status()
        data = res.json()

        # 无结果提示
        if data['totalResults'] == 0:
            print("未找到中文新闻")
            return

        for i, art in enumerate(data['articles'], 1):

            title = art.get('title')
            source = art['source'].get('name')
            time = art.get('publishedat', '').split('T')[0]
            description = art.get('description')[:50]

            print(f"\n{i}. 标题：{title}")
            print(f"   来源：{source}")
            print(f"   发布时间：{time}")
            print(f"   简介：{description}...")
    except Exception as e:
        print(f"获取失败：{e}")


if __name__ == "__main__":
    get_china_news()