import tkinter.messagebox
import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image

# step1: select the files to be processed(default order)
def select():
    global pic_s
    pic_s=fd.askopenfilenames(filetypes=[('图片文件','.jpg')])
    if pic_s!='':
        pic_in.set(pic_s)
        button_out['state']='normal'
    return None

# step2: select the folder to output the pdf file
def select_out():
    path_save=fd.askdirectory()
    if path_save!='':
        pdf_out.set(path_save)
        button_on['state']='normal'

# step3: write the pictures into a pdf
def combine():
    i=0
    source=[]
    output=Image.open(pic_s[0])
    for path in pic_s:
        if i>=1:
            pic=Image.open(path)
            if pic.mode == "RGB":
                pic = pic.convert("RGB")
            source.append(pic)
        else:
            i+=1
    output.save(pdf_out.get()+'/combine_result.pdf',"pdf",save_all=True,append_images=source)
    tkinter.messagebox.showinfo('Successfully operated!')
    return None

# GUI initialize
def main(root3):
    global pic_in, pdf_out, on, entry_out, button_out, button_on
    pic_in = tk.StringVar()
    pdf_out = tk.StringVar()
    on = tk.StringVar()
    label_input = tk.Label(root3, text='①选择要合并的图片：')
    entry_input = tk.Entry(root3, textvariable=pic_in, width=45)
    button_input = tk.Button(root3, text='①选择要合并的图片', command=select)
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
    button_on.place(x=220, y=150)
    
global pic_in, pdf_out, on, entry_out, button_out, button_on
    
root2 = tk.Tk()
sw = root2.winfo_screenwidth()
sh = root2.winfo_screenheight()
c = (sw - 400) / 2
d = (sh - 300) / 2
root2.geometry('605x500+%d+%d'%(c, d))
root2.title('图片合并为PDF')
root2.resizable(width=False, height=False)
root = tk.Frame(root2, width=605, height=500)
root.place(x=0, y=0)

main(root)
root2.mainloop()