from django.shortcuts import render
from Stock.models import stock_data

def Get_data_Example(request):

    #強烈建議了解資料庫內部結構後再進行操作，例如下載DB.Browser可查看資料庫內容
    try: 
        # 變數 = 資料庫名稱.方法(條件)   .first()是指符合條件的第一筆  #還有其他拿資料的方法
        first  = stock_data.objects.filter(stock_symbol = '2330').first()
        Second = stock_data.objects.filter(stock_symbol = '2317').first()
        Third  = stock_data.objects.filter(stock_symbol = '2454').first()
        #在CMD輸出，Debug用
        print(  first.stock_symbol,  first.high_price,  first.low_price,  first.change_price,
                Second.stock_symbol, Second.high_price, Second.low_price, Second.change_price,
                Third.stock_symbol,  Third.high_price,  Third.low_price,  Third.change_price )
        #打包到字典        
        data_dict = { '2330_1' : first.stock_symbol,
                      '2330_2' : first.high_price,  
                      '2330_3' : first.low_price,  
                      '2330_4' : first.change_price,
                      '2317_1' : Second.stock_symbol, 
                      '2317_2' : Second.high_price, 
                      '2317_3' : Second.low_price, 
                      '2317_4' : Second.change_price,
                      '2454_1' : Third.stock_symbol,  
                      '2454_2' : Third.high_price,  
                      '2454_3' : Third.low_price,  
                      '2454_4' : Third.change_price }
    except:
        print('Error')

                                #在HTML文件中使用的變數.KEY會映射出這邊的字典對應值
    return render( request, 'Get_data_Example.htm' , { 'Data' : data_dict })