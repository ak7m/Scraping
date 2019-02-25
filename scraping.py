import pandas as pd
from bs4 import BeautifulSoup
import requests
from google.colab import files

url = "http://www.g36cmsky.com/"

response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

tags = soup.find_all("div", {"class":"sidebody"})

# データフレームを作成してください。列名は、name, urlです。
columns = ["name", "url"]
df2 = pd.DataFrame(columns=columns)

# 記事名と記事URLをデータフレームに追加してください
for tag in tags:
 name = tag.a.string
 url = tag.a.get("href")
 se = pd.Series([name, url], columns)
 print(se)
 df2 = df2.append(se, columns)

# result.csvという名前でCSVに出力してください。
filename = "result.csv"
df2.to_csv(filename, encoding = 'utf-8-sig') #encoding指定しないと、エラーが起こります。おまじないだとおもって入力します。
files.download(filename)
