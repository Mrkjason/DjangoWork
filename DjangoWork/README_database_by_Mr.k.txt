已將以下10種股票近1年來數據(2023/4/6 ~ 2024/5/10)載入資料庫 stock_data.db

  股票代碼 名稱
1 - 2330 - 台積電
2 - 2317 - 鴻海
3 - 2454 - 聯發科
4 - 1301 - 台塑
5 - 1303 - 南亞
6 - 2412 - 中華電信
7 - 2308 - 台達電
8 - 2881 - 富邦金
9 - 2891 - 中信金
10- 2892 - 第一金

這些資料使用 twstock 抓取
抓取用的程式在 catch.py ，有再次提取的需求時提供使用，
"""沒特殊狀況的話不用再執行一次"""

我有把拿資料的方法範例放在 view_2 、 Get_data_Example 裡提供參考


資料種類名稱與其意義對照表:

   stock_symbol : 股票編號
      date      : 日期
  total_capacity: 總成交股數
  total_turnover: 總成交金額
    open_price  : 開盤價
    high_price  : 盤中最高價
     low_price  : 盤中最低價
    close_price : 收盤價
   change_price : 漲跌價差
   trans_action : 成交筆數

安裝 twstock 方法:
#安裝 twstock、lxml
#CMD 指令:  pip install --user twstock
#           pip install lxml
#把 twstock 加入 PATH 路徑


建立資料檔:
python manage.py makemigrations

同步更新資料庫內容
python manage.py migrate
