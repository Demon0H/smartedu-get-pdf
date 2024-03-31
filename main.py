import tkinter as tk
from tkinter import filedialog
import requests
import chardet
import time
def get_url_content():
    url = entry.get()
    if "ContentId=" in url:
        start_index = url.index("ContentId=") + len("ContentId=")
        if "&" in url[start_index:]:
            end_index = url.index("&", start_index) + start_index
            content=url[start_index:end_index]
            content=content.replace("&saveAsCopy=false",'')
            url=f"https://r3-ndr.ykt.cbern.com.cn/edu_product/esp/assets/{content}.pkg/pdf.pdf"
            response = requests.get(url)
            content = response.content
            file_name = time.strftime("%Y-%m-%d-%H-%M-%S")
            with open(f"{file_name}.pdf", "wb") as file:
                file.write(response.content)
            tk.messagebox.showinfo("国家中小学智慧教育平台教材获取","请查看该目录下是否有文档，有则成功")
            return content
app = tk.Tk()
app.title("国家中小学智慧教育平台教材获取")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

entry_label = tk.Label(frame, text="请复制教程的网站到该文本框:")
entry_label.pack()

entry = tk.Entry(frame, width=50)
entry.pack()

button = tk.Button(frame, text="确定", command=get_url_content)
button.pack()

app.mainloop()