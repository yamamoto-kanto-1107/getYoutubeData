from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import app

# ウィンドウを作成
root = Tk()
root.geometry("620x550")
root.title('入力フォーム')

# ウィンドウ全体のpadding
root.config(padx=10, pady=10)

# CSV出力先
label1 = ttk.Label(root, text='CSV出力先:',anchor='w', font=("MSゴシック", "15"))
label1.grid(row=0, column=0, sticky=W, pady=2)

# CSV出力先エントリ
OutputCSV = StringVar()
OutputCSV_txt = ttk.Entry(root, textvariable=OutputCSV, width=20)
OutputCSV_txt.grid(row=0, column=1,pady=5)

# CSV参照ボタン
def dirdialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir=iDir)
    OutputCSV.set(iDirPath)

IDirButton = ttk.Button(root, text="参照", command=dirdialog_clicked)
IDirButton.grid(row=0, column=2, padx=5, pady=5)

# 取得チャンネル数
label2 = ttk.Label(root, text='出力チャンネル数:',anchor='w', font=("MSゴシック", "15"))
label2.grid(row=1, column=0, sticky=W, pady=2)
output_count = IntVar()
Output_count_txt = ttk.Entry(root, textvariable=output_count, width=20)
output_count.set(0)
Output_count_txt.grid(row=1, column=1,pady=5)

# ジャンル選択ラベル
categoryLabel = ttk.Label(root, text='ジャンル:', anchor="w", width=15, font=("MSゴシック", "15"))
categoryLabel.grid(row=2, column=0, sticky=W, pady=5)

categorySelect = IntVar()

categories = [
    {'name': '映画とアニメ', 'value': 1},
    {'name': '自動車と乗り物', 'value': 2},
    {'name': '音楽', 'value': 10},
    {'name': 'ペットと動物', 'value': 15},
    {'name': 'スポーツ', 'value': 17},
    {'name': 'ショート　ムービー', 'value': 18},
    {'name': '旅行とイベント', 'value': 19},
    {'name': 'ゲーム', 'value': 20},
    {'name': '動画ブログ', 'value': 22},
    {'name': 'ブログ', 'value': 23},
    {'name': 'コメディー', 'value': 24},
    {'name': 'エンターテイメント', 'value': 25},
    {'name': 'ニュースと政治', 'value': 26},
    {'name': 'ハウツーとスタイル', 'value': 27},
    {'name': '教育', 'value': 28},
    {'name': '科学と技術', 'value': 29}
]

# ラジオボタンでジャンルを選択
for i, category in enumerate(categories):
    categoryBtn = ttk.Radiobutton(root, text=category['name'], variable=categorySelect, value=category['value'])
    categoryBtn.grid(row=3 + i, column=0, sticky=W, padx=20, pady=2)


# 開始ボタン
def btn_click():
    csv_value = str(OutputCSV.get())
    count_value = int(output_count.get())
    category_value = categorySelect.get()
    ret = messagebox.askquestion('質問', 'CSV出力しますか？')
    if ret:
        print('call')
        app.output_youtube_detail(csv_value,category_value,count_value)
    else:
        print('no')

button1 = ttk.Button(root, text='開始', command=btn_click)
button1.grid(row=20, column=1, padx=10, pady=10)

# ウィンドウ表示継続
root.mainloop()
