以下複製於老師PPT，並記錄目前進度

<<< 期末專案作業內容 >>>

網站美工(UI/UX) (10%)
▪ 設計出使用者友善的介面，讓使用者容易使用並理解查詢系統的功能
▪ 使用Bootstrap、CSS等前端技術編寫美化網頁，使網站看起來更美觀
>>>教學範例:
>>>https://note.robinks.net/2013/10/using-bootstrap-to-build-prototype-web.html
>>>最簡單也最難


▪ Django架設網站 (20%)
▪ 將網站部署到heroku上或使用ngrok，使其他人得以使用行動裝置或電腦透過IP連線到網站
▪ 首頁放上組別、小組成員、小組分工……等資訊
>>>從頭開始算的話， ngrok 比較方便，缺點是免費版只能連續運作8小時，但也夠展示成果用了，要用哪種都可以


~~~~~~~~~~ 已完成 ~~~~~~~~~~
▪ 選定至少10支股票，使用twstock API、django內建方法、或其他開放API，將至少一年之資訊存入sqlite3資
料庫中 (20%)
▪ 總成交股數
▪ 總成交金額
▪ 開盤價
▪ 盤中最高價
▪ 盤中最低價
▪ 收盤價
▪ 漲跌價差
▪ 成交筆數
~~~~~~~~~~ 已完成 ~~~~~~~~~~


▪ 簡易查詢即時股市程式 (25%)
▪ 需使用twstock API，能夠透過輸入股票代號或名稱搜尋
▪ 顯示該股票之下列資訊
▪ 查詢時間、股票代號、股票名稱、股票全名
▪ 最佳買入價(best bid price)、最佳買入數量(best bid volume)
▪ 最佳賣出價(best ask price)、最佳賣出數量(best ask volume)
▪ 開盤價、最高價、最低價
▪ 需注意排版(乾淨整齊漂亮)
>>>twstock 官方文件：https://twstock.readthedocs.io/zh-tw/latest/


▪ 顯示股票歷史資訊走勢圖 (25%)
▪ 需連結資料庫
▪ 輸入年份或月份後，顯示該股票的年或月 (1)開盤/收盤價曲線圖以及 (2)KD線圖
>>>從資料庫拿資料，KD線圖需要用算的
>>>查看資料庫內部教學：https://raymond-investment.com/blog/sqlite-db-browser-install