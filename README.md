# chatterbot-linebot #

## 專案介紹 ##

本專案以LINE Bot Server為主要執行架構，整體系統流程及架構如下：

使用者發送訊息至LINE官方帳號後，LINE Platform接收訊息，並將webhook事件傳送至LINE Bot Server的webhook URL，再由LINE Bot Server依據webhook event（聊天、聽音樂、看影片、聽笑話、查天氣、查詢資料等Request），決定利用chatterbot API還是網頁爬蟲去做相對應的Response。接著，透過LINE所提供的Messaging API，將Response回傳至Line platform，最後由LINE Platform傳遞給使用者，進而讓使用者和聊天機器人互動。

同時，我們使用Python物件導向的多型(Polymorphism)概念，來開發美食餐廳的LINE Bot，透過按鈕樣板訊息(Buttons template message)對談的方式瞭解使用者所要尋找的餐廳條件(地區、美食分類、平均消費價格)後，利用Python網頁爬蟲取得目前正在營業的五間最高人氣餐廳資料，回覆給使用者作為參考。

其中， Messaging API 為LINE官方定義的回應訊息標準介面，包含Text（文字）、Sticker（貼圖）、Video（影片）、Audio（聲音）及Template（樣板）訊息等，可使 data 於 LINE Bot Server 及 LINE Platform 之間傳遞（HTTPS上傳送的Request為JSON 格式）。






## 前置作業 ##

# 環境要求 #

Python 3.8

需先安裝chatterbot API
`$ pip install chatterbot==1.0.4
`$ pip install chatterbot_corpus

由於chatterbot API內部的資料集並未有中文繁體資料，因此需安裝opencc API來進行繁<->簡翻譯
`$ pip install opencc


將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，執行Django Migration(資料遷移)：

`$ pipenv shell`

`$ python manage.py migrate`

## 執行畫面 ##

<img src="https://1.bp.blogspot.com/-xtdV8qWOQgI/XwsK2R_FLRI/AAAAAAAADho/mwYWqibN1wIv1Xy-RZF9LBN2rPwmMsbNQCPcBGAsYHg/s2048/line_bot_buttons_template_message_1.jpg" width="350" height="700" />

<img src="https://1.bp.blogspot.com/-WRi2qROqKis/XwsK2fDaTZI/AAAAAAAADho/VZ-Ac8ewhjccJwDMtyQAsJftU2t78OH3gCPcBGAsYHg/s2048/line_bot_buttons_template_message_2.jpg" width="350" height="700" />
