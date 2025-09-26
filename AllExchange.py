import pandas as pd

date = "2025-09-25"
url = f"https://rate.bot.com.tw/xrt/all/{date}"

# 讀取網頁表格
tables = pd.read_html(url)
df = tables[0]

# 刪除最後三欄
df = df.iloc[:, :-3]

# 修改欄位名稱
df.columns = ["幣別", "現金買入", "現金賣出", "即期買入", "即期賣出"]

# 拆分幣別名稱與代號
df["幣別名稱"] = df["幣別"].str.extract(r"^([\u4e00-\u9fff]+)")
df["幣別代號"] = df["幣別"].str.extract(r"\((\w+)\)")

# 移除原本的「幣別」欄
df = df.drop(columns=["幣別"])

# 轉換數值格式
num_cols = ["現金買入", "現金賣出", "即期買入", "即期賣出"]
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors="coerce")

# 新增日期欄位
df["日期"] = date

# 調整欄位順序
df = df[["日期", "幣別名稱", "幣別代號", "現金買入", "現金賣出", "即期買入", "即期賣出"]]

print(df.head())
