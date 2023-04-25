import os.path
from PyPDF2 import PdfReader, PdfWriter
import tkinter as tk
from tkinter import filedialog as fd
import tkinter.messagebox

# the operation of splitting
def split_pdf(pdf_i, start, end):
    pdf = PdfReader(pdf_i)
    pdf_wt = PdfWriter()
    for i in range(start-1, end):
        pdf_wt.add_page(pdf.pages[i])
    pdf_path, pdf_name = os.path.split(pdf_in.get())
    pdf_name, pdf_ext = os.path.splitext(pdf_name)
    split_name = pdf_out.get() + '\\' + pdf_name + '(P%d—P%d).pdf'%(start,end)
    split_name2 = pdf_out.get() + '\\' + pdf_name + '(P%d).pdf'%start
    pdf_name = split_name2 if start == end else split_name
    with open(pdf_name, 'wb') as outfile:
        pdf_wt.write(outfile)

# select the pdf file to be splitted
def select_pdf():
    pdf_selected = fd.askopenfilename(filetypes=file_types)
    if pdf_selected != '':
        pdf_in.set(pdf_selected)
        pdf = PdfReader(pdf_selected)
        pages = len(pdf.pages)
        pdf_pages.set('③输入要分割的页码：(页码范围1-%d)'%pages)
        button_out['state'] = 'normal'

# select where the result file will be located
def select_out():
    path_save = fd.askdirectory()
    if path_save != '':
        button_split['state'] = 'normal'
        pdf_out.set(path_save)

# operation before splitting
def pdf_split():
    if pdf_out2.get() != '':
        # the replace from Chinese to English
        page_out_in = pdf_out2.get().replace('，', ',')
        page_split = page_out_in.split(',')
        pdf_to_be_split = pdf_in.get()
        pdf = PdfReader(pdf_to_be_split)
        pages = len(pdf.pages)
        flag_successed =0
        flag_failed =[]
        for i in page_split:
            page_range = i.split('-')
            page_range_l = len(page_range)
            # handling the exception of page index range
            if page_range_l > 1:
                start = int(page_range[0])
                end = int(page_range[1])
                if start <= end <= pages:
                    split_pdf(pdf_to_be_split, start, end)
                    flag_successed+=1
                else:
                    flag_failed.append(f'{start}-{end}')
            # some exceptions
            elif page_range_l == 1:
                if int(page_range[0]) <= pages:
                    split_pdf(pdf_to_be_split, int(page_range[0]), int(page_range[0]))
                    flag_successed += 1
                else:
                    flag_failed.append(f'{page_range[0]}')
        if len(flag_failed)==0:
            tkinter.messagebox.showinfo('HANDLING TIPS: %d个文件分割成功'%flag_successed)
        else:
            tkinter.messagebox.showinfo('HANDLING TIPS: %d个文件分割成功,%d个文件分割失败'%(flag_successed,len(flag_failed)))
            tkinter.messagebox.showinfo('HANDLING TIPS:', f'以下页码输入错误，页码范围为1--{pages}\n{flag_failed}')

def main(root3):
    global pdf_in, pdf_out, pdf_out2, entry_out, entry_out2, pdf_pages, button_out, button_split
    pdf_in = tk.StringVar()
    pdf_out = tk.StringVar()
    pdf_out2 = tk.StringVar()
    pdf_pages = tk.StringVar()
    pdf_pages.set('③输入要分割的页码：')
    label_input = tk.Label(root3, text='①选择要分割的PDF文件：')
    entry_input = tk.Entry(root3, textvariable=pdf_in, width=45)
    button_input = tk.Button(root3, text='①选择要分割的PDF文件', command=select_pdf)
    label_out = tk.Label(root3, text='②选择输出文件夹：')
    entry_out = tk.Entry(root3, textvariable=pdf_out, width=45)
    button_out = tk.Button(root3, text='②选择保存位置', command=select_out)
    button_out['state'] = 'disabled'
    page_out = tk.Label(root3, textvariable=pdf_pages, text='③输入要分割的页码：')
    page_out_ = tk.Label(root3, text='（可分割为多个PDF，用cn/en逗号分隔。例如: 2-10,15)')
    entry_out2 = tk.Entry(root3, textvariable=pdf_out2, width=45)
    button_split = tk.Button(root3, text='④执行分割', command=pdf_split, width=20, height=3)
    button_split['state'] = 'disabled'
    label_input.place(x=10, y=10)
    entry_input.place(x=10, y=35)
    button_input.place(x=350, y=32)
    label_out.place(x=10, y=80)
    entry_out.place(x=10, y=105)
    button_out.place(x=350, y=97)
    page_out.place(x=10, y=150)
    page_out_.place(x=10, y=175)
    entry_out2.place(x=10, y=200)
    button_split.place(x=220, y=240)

global pdf_in, pdf_out, pdf_out2, entry_out, entry_out2, pdf_pages, button_out, button_split
file_types = [('PDF文件', '.pdf')]
root2 = tk.Tk()
sw = root2.winfo_screenwidth()
sh = root2.winfo_screenheight()
c = (sw - 400) / 2
d = (sh - 300) / 2
root2.geometry('605x500+%d+%d'%(c, d))
root2.title('PDF分割')
root2.resizable(width=True, height=True)
root = tk.Frame(root2, width=605, height=500)
root.place(x=0, y=0)
main(root)
root2.mainloop()
