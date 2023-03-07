import tkinter as tk
from tkinter import *
import tkinter.messagebox as box
import mysql.connector as connect
from datetime import datetime
root=Tk()

root.geometry ('400x350')
root.title('Search Engine')
label=Label(root, text='Search',font=('Helvetica 17 bold'))
label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

root.columnconfigure (0, weight=2)
root.columnconfigure (1, weight=3)
search=Entry (root)
search.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
frame=Frame(root)

def connection():
    global con
    con=connect.connect(host='localhost',port='3306',user='root',password='root_123')
    print('Connected to MYSqL')
connection()

#Creating Database
def create_database(D_name):
    cur=con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS "+str(D_name))
    print('Database is Ready')
create_database('MY_DICTIONARY')

#use database
def use_database(name):
    query='use '+str(name)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print('Using',name,'Database')
use_database('MY_DICTIONARY')

#creating table
def create_table(t_name):
    query='CREATE TABLE IF NOT EXISTS '+str(t_name)+'(Words VARCHAR(50),TimeStrap varchar(50))'
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print('Table Ready')
create_table('Dict')

def solve():
    #query='select*from dictionary'
    #cur=con.cursor()
    #cur.execute(query)
    #for i in cur:
    #   print(i)
    file=open('data.txt','r')
    reference=file.readlines()
    file.close()
    word=search.get()
    length=len(word)
    s=set()
    sets=set(word)
    for ele in word:
        for item in reference:
            if sets.issubset(item):
                s.add(item)
        else:
            pass
    li=list(s)
    l=tk.StringVar(value=li)
    lis=Listbox(root,listvariable=l)
    lis.grid(column=0,row=3,sticky=tk.E,padx=1,pady=1)
    
def X():
    now=datetime.now()
    form=now.strftime('%m-%d-%y %H:%M:%S')
    word=search.get()
    if word=='':
        box.showinfo('box','what u want to search empty ah\nplease enter a word')
    else:
        l=[]
        l.append(word)
        l.append(form)
#inserting into database
        cur=con.cursor()
        query='INSERT INTO Dict(words,TimeStrap)values(%s,%s)'
        val=l
        try:
            cur.execute(query,val)
            con.commit()
            print('Data Saved')
        except:
            con.rollback()
        
        
def key_press(e):
    command=solve()
def key_release(e):
    command=solve()
root.bind('<KeyPress>',key_press)
root.bind('<KeyRelease>',key_release)
but=Button(root,text='search',command=X)
but.grid(column=1,row=1,sticky=tk.W,padx=5,pady=5)

root.mainloop()
con.close()


