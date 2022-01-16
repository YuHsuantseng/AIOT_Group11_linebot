# Chatterbot-linebot #

## 專案介紹 ##

本專案以LINE Bot Server為主要執行架構，整體系統流程及架構如下：

使用者發送訊息至LINE官方帳號後，LINE Platform接收訊息，並將webhook事件傳送至LINE Bot Server的webhook URL，再由LINE Bot Server依據webhook event（聊天、聽音樂、看影片、聽笑話、查天氣、查詢資料等Request），決定利用chatterbot API還是網頁爬蟲去做相對應的Response。接著，透過LINE所提供的Messaging API，將Response回傳至Line platform，最後由LINE Platform傳遞給使用者，進而讓使用者和聊天機器人互動。

同時，我們使用Python物件導向的多型(Polymorphism)概念，來開發美食餐廳的LINE Bot，透過按鈕樣板訊息(Buttons template message)對談的方式瞭解使用者所要尋找的餐廳條件(地區、美食分類、平均消費價格)後，利用Python網頁爬蟲取得目前正在營業的五間最高人氣餐廳資料，回覆給使用者作為參考。

其中， Messaging API 為LINE官方定義的回應訊息標準介面，包含Text（文字）、Sticker（貼圖）、Video（影片）、Audio（聲音）及Template（樣板）訊息等，可使 data 於 LINE Bot Server 及 LINE Platform 之間傳遞（HTTPS上傳送的Request為JSON 格式）。

<img src="https://github.com/YuHsuantseng/AIOT_Group11_linebot/blob/main/images/Message%20API%E6%B5%81%E7%A8%8B.jpg" width="700" height="350" />

## 系統架構 ##

<img src="https://github.com/YuHsuantseng/AIOT_Group11_linebot/blob/main/images/%E7%B3%BB%E7%B5%B1%E6%9E%B6%E6%A7%8B.JPG" width="700" height="350" />
<img src="https://github.com/YuHsuantseng/AIOT_Group11_linebot/blob/main/images/%E7%B3%BB%E7%B5%B1%E6%B5%81%E7%A8%8B%E5%9C%96.jpg" width="350" height="700" />


## 使用情境 ##

假設小熊-小白，他剛好沒有人可以聊天，覺得很無聊想去找聊天機器人說說話，小白如果想買iphone，聊天機器人就會回傳iphone購物連結；小白想聽歌，輸入我要聽梁靜茹的勇氣，聊天機器人就回傳歌曲URL；小白想知道天氣狀態，聊天機器人會回傳天氣相關資訊；小白無聊想聽笑話時，聊天機器人就回傳一個笑話；小白想查哪個縣市推薦的美食時，聊天機器人就會用問答的方式，詢問小熊喜歡的美食類型、地區，最後回傳推薦他喜歡的餐廳給他；同時，小白也透過聊天機器人，來排除內心的寂寞感，甚至是得到歸屬感
<img src="https://github.com/YuHsuantseng/AIOT_Group11_linebot/blob/main/images/Line%20Bot%E4%BD%BF%E7%94%A8%E6%83%85%E5%A2%83.jpg" width="700" height="350" />

## DEMO ##

<img src="https://github.com/YuHsuantseng/AIOT_Group11_linebot/blob/main/images/demo.gif" width="350" height="700" />


## 前置作業 ##

### 環境要求 ###

`Python 3.8` 、 `Window10`

### 將專案複製(Clone)下來後，假設沒有以下套件，可以透過以下指令各別安裝： ###

chatterbot API 安裝

`$ pip install chatterbot==1.0.4` 、 `$ pip install chatterbot_corpus`

由於chatterbot API內部的資料集並未有中文繁體資料，因此需安裝opencc API來進行繁<->簡翻譯

`$ pip install opencc`

在Python網頁爬蟲應用上，BeautifulSoup是一個用來解析HTML結構的Python Package，將取回的網頁HTML結構，透過其提供的方法，能夠輕鬆的搜尋及擷取網頁上所需的資料：

`$ pip install beautifulsoup4`

而解析網頁的HTML程式碼前，還需安裝Python的requests Package，將要爬取的網頁HTML程式碼取回來：

`$ pip install requests`

pipenv套件管理工具安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，執行Django Migration(資料遷移)：

`$ pipenv shell`

`$ python manage.py migrate`





## 參考資料 ##

