import tkinter.messagebox
import tkinter as tk
from tkinter import filedialog as fd
from PyPDF2 import PdfMerger, PdfReader #引入

# step1: select the files to be processed(default order)
def select():
    global file_s
    file_s=fd.askopenfilenames(filetypes=[("pdf文件",".pdf")])
    if file_s!='':
        pic_in.set(file_s)
        button_out['state']='normal'
    return None

# step2: select the folder to output the pdf file
def select_out():
    global path_save
    path_save=fd.askdirectory()
    if path_save!='':
        pdf_out.set(path_save)
        button_on['state']='normal'

# step3: write the pictures into a pdf
def combine():
    file_merger = PdfMerger(strict=False)
    path=path_save+"combine.pdf"
    for pdf in file_s:
        file_merger.append(PdfReader(pdf), 'tag')
    file_merger.add_metadata(
        {u'/Title': u'my title', u'/Creator': u'creator', '/Subject': 'subjects'})
    with open(path, 'wb+') as fa:
        file_merger.write(fa)
    tkinter.messagebox.showinfo('Successfully operated!')
    fa.close()
    file_merger.close()
    return None

# GUI initialize
def main(root3):
    global pic_in, pdf_out, on, entry_out, button_out, button_on
    pic_in = tk.StringVar()
    pdf_out = tk.StringVar()
    on = tk.StringVar()
    label_input = tk.Label(root3, text='①选择要合并的pdf：')
    entry_input = tk.Entry(root3, textvariable=pic_in, width=45)
    button_input = tk.Button(root3, text='①选择要合并的pdf', command=select)
    label_out = tk.Label(root3, text='②选择输出文件夹：（输出结果为该文件夹下的combine_result.pdf）')
    entry_out = tk.Entry(root3, textvariable=pdf_out, width=45)
    button_out = tk.Button(root3, text='②选择保存位置', command=select_out)
    button_out['state'] = 'disabled'
    button_on = tk.Button(root3, text='③执行', command=combine, width=20, height=3)
    button_on['state'] = 'disabled'
    label_input.place(x=10,y=10)
    entry_input.place(x=10, y=35)
    button_input.place(x=350, y=32)
    label_out.place(x=10, y=80)
    entry_out.place(x=10, y=105)
    button_out.place(x=350, y=97)
    button_on.place(x=150, y=150)
    
global pic_in, pdf_out, on, entry_out, button_out, button_on
    
root2 = tk.Tk()
sw = root2.winfo_screenwidth()
sh = root2.winfo_screenheight()
c = (sw - 400) / 2
d = (sh - 300) / 2
root2.geometry('500x300+%d+%d'%(c, d))
root2.title('PDF合并')
root2.resizable(width=False, height=False)
root = tk.Frame(root2, width=605, height=500)
root.place(x=0, y=0)

main(root)
root2.mainloop()