import requests

while True:
    city = input('请输入城市,回车退出:\n')
    if not city:
        break
    try:
        req = requests.get(
            'http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    except:
        print('查询失败')
        break
    # print(req.text)
    dic_city = req.json()  # 将json格式的文件转换为字典
    # print(dic_city)
    city_data = dic_city.get('data')  # 字典分为3部分：data、status、desc，这里我们需要data
    if city_data:
        city_forecast = city_data['forecast'][0]  # 只需要forecast的第一位，当天的天气
        # 下面的都可以换成'get'方法
        print(city_forecast.get('date'))  # 日期
        print(city_forecast.get('high'))  # 最高气温
        print(city_forecast.get('low'))  # 最低气温
        print(city_forecast.get('type'))  # 天气情况
    else:
        print('未获得')
