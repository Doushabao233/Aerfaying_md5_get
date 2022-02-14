import hashlib
from tkinter import *
from tkinter import font
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import tkinter.messagebox as msgbox
from webbrowser import open_new_tab

# 窗口
window = Tk()
window.title('文件md5获取器')
window.resizable(False, False)

md5_result = StringVar()
md5_result.set('文件MD5将在这里生成，可以双击复制')

# 函数
def choose_file():
    f = askopenfile(title='选择要获取md5的文件', mode='rb')
    try:
        file_md5 = hashlib.md5(f.read()).hexdigest() + '.' + f.name.split('.')[-1]
    except:
        msgbox.showerror('错误', '选择的文件有误或没有选择文件')
    else:
        md5_result.set(file_md5)
        f.close()

def about():
    msgbox.showinfo('关于', 'A营md5生成器\nby 豆沙包\n2021.11.7\n功能可能还不是很完善，请谅解')

def how_to_use():
    msgbox.showinfo('如何使用', '1. 点击选择文件按钮\n2. 然后选择你要获取md5的文件\n3. 最后复制输入框内的内容')
    msgbox.showinfo('如何使用', '另外，可以点击菜单栏使用一些其他的功能')
    msgbox.showinfo('此时作者内心的想法', '不会吧，不会吧！难道都2021年了，难道还有人连这种软件都不会用？')

# 菜单栏
menubar = Menu()

file = Menu(menubar, tearoff=False)
menubar.add_cascade(label='文件', menu=file)

file.add_command(label='选择文件', command=lambda: choose_file())

help = Menu(menubar, tearoff=False)
menubar.add_cascade(label='帮助', menu=help)

help.add_command(label='如何使用', command=how_to_use)
help.add_command(label='关于', command=about)

other = Menu(menubar, tearoff=False)
menubar.add_cascade(label='其他', menu=other)
other.add_command(label='打开阿儿法营', command=lambda: open_new_tab('https://www.aerfaying.com/'))
other.add_command(label='打开备用站（稽木世界）', command=lambda: open_new_tab('https://www.gitblock.cn/'))

# 窗口元素
choose = Button(text='选择文件', width=60, command=lambda: choose_file()).grid(column=0, row=0, padx=10, pady=10)
result = Entry(textvariable=md5_result, width=38, font=('Consolas')).grid(column=0, row=1, padx=10, pady=10)

# 结尾
window.config(menu=menubar)
window.mainloop()