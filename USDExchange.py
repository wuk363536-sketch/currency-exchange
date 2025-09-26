# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 設定全域字型為 微軟正黑體
rcParams["font.family"] = "Microsoft JhengHei"

# 連線資料庫
db_path = "台灣銀行.db"
conn = sqlite3.connect(db_path)

# 讀取匯率資料表並排序
df = pd.read_sql_query("SELECT * FROM 匯率 ORDER BY 日期 ASC", conn)
conn.close()

# 將日期欄位轉成 datetime
df["日期"] = pd.to_datetime(df["日期"])

# 過濾「幣別名稱」為「美金」
df_usd = df[df["幣別名稱"] == "美金"]

# 繪製折線圖
plt.figure(figsize=(12, 6))
plt.plot(df_usd["日期"], df_usd["現金買入"], marker='o', linestyle='-', color='b')
plt.title("美金現金買入匯率走勢")
plt.xlabel("日期")
plt.ylabel("現金買入")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 儲存圖檔
plt.savefig("美金一年匯率走勢圖.png", dpi=300)

plt.show()
