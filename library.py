from ast import Delete
from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter
class LibraryManangementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title=("Library management system")
        self.root.geometry('1550x800+0+0')
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.adress_var=StringVar()
        # self.postid_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.finalprice_var=StringVar()
        # self.b_name=StringVar()
 
        
        lbltitle=Label(self.root,text="Library management system",bg="lemon chiffon", fg="black",bd=20,relief=RIDGE,font=("times new roman", 50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
         #=================================Data frame left =============#
        DataFrameLeft=LabelFrame(frame,text="Library membership information",bg="pink", fg="dark orchid",bd=5,relief=RIDGE,font=("times new roman", 19,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        lblMemebr=Label(DataFrameLeft,text="Member Type:",font=("times new roman", 15,"bold"),padx=2,pady=6,bg="pink")
        lblMemebr.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman", 15,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin staff","Student","lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblprn_no=Label(DataFrameLeft,text="Prn No:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lblprn_no.grid(row=1,column=0,sticky=W)
        txtprn_no=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.prn_var,width=29)
        txtprn_no.grid(row=1,column=1)


        lblTitle=Label(DataFrameLeft,text="ID No:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lblTitle.grid(row=2,column=0,sticky=W)
        txttitle=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.id_var,width=29)
        txttitle.grid(row=2,column=1)

        lblFirstname=Label(DataFrameLeft,text="Name:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lblFirstname.grid(row=3,column=0,sticky=W)
        txtfname=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.name_var,width=29)
        txtfname.grid(row=3,column=1)

        

        lbladress=Label(DataFrameLeft,text="Adress:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lbladress.grid(row=4,column=0,sticky=W)
        txtladress=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.adress_var,width=29)
        txtladress.grid(row=4,column=1)

        lblMobile=Label(DataFrameLeft,text="Mobile:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=5,column=1)

        lblbId=Label(DataFrameLeft,text="Book ID:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lblbId.grid(row=6,column=0,sticky=W)
        txtbId=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.bookid_var,width=29)
        txtbId.grid(row=6,column=1)

        lblbt=Label(DataFrameLeft,text="Book Title:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lblbt.grid(row=7,column=0,sticky=W)
        txtbt=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.booktitle_var,width=29)
        txtbt.grid(row=7,column=1)

        lblat=Label(DataFrameLeft,text="Author:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lblat.grid(row=1,column=2,sticky=W)
        txtat=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.author_var,width=29)
        txtat.grid(row=1,column=3)

        lbldb=Label(DataFrameLeft,text="Date Borrowed:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lbldb.grid(row=2,column=2,sticky=W)
        txtdb=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtdb.grid(row=2,column=3)

        lbldd=Label(DataFrameLeft,text="Date Due:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lbldd.grid(row=3,column=2,sticky=W)
        txtdd=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.datedue_var,width=29)
        txtdd.grid(row=3,column=3)

        lbldob=Label(DataFrameLeft,text="Dates on Book:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lbldob.grid(row=4,column=2,sticky=W)
        txtdob=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.daysonbook_var,width=29)
        txtdob.grid(row=4,column=3)

        lbllrf=Label(DataFrameLeft,text="Late return fine:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lbllrf.grid(row=5,column=2,sticky=W)
        txtlrf=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.lateratefine_var,width=29)
        txtlrf.grid(row=5,column=3)

        lbldod=Label(DataFrameLeft,text="Date Over Due:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lbldod.grid(row=6,column=2,sticky=W)
        txtldod=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtldod.grid(row=6,column=3)

        lblap=Label(DataFrameLeft,text="Actual price:",font=("times new roman", 12,"bold"),padx=2,pady=6,bg="pink")
        lblap.grid(row=7,column=2,sticky=W)
        txtlap=Entry(DataFrameLeft,font=("times new roman", 13,"bold"),textvariable=self.finalprice_var,width=29)
        txtlap.grid(row=7,column=3)








     #============================data frame right==============#



        DataFrameRight=LabelFrame(frame,text="Book Details",bg="pink", fg="dark orchid",bd=5,relief=RIDGE,font=("times new roman", 19,"bold"),padx=2,pady=6)
        DataFrameRight.place(x=910,y=5,width=540,height=350)


        self.txtBox=Text(DataFrameRight,font=("times new roman", 12,"bold"),padx=2,pady=6,width=32,height=14)
        self.txtBox.grid(row=0,column=2)

        listscrollbar=Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0,column=1,sticky='ns')

        listBooks=["Python Programming",'Java',"Gandhi biography","Indias struggle","fountain head","Amazon","Indian history","Indian polity","Gandhi biography","Indias struggle","fountain head","Amazon","Indian history","Indian polity","Gandhi biography","Indias struggle","fountain head","Amazon","Indian history","Indian polity"]
        
        def SelectBook(event):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Gandhi biography"):
                self.bookid_var.set("Bkid5454")
                self.booktitle_var.set("Python manual")
                self.author_var.set('Paul')
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("RS 50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs 788")


        
        
        listBox=Listbox(DataFrameRight,font=("times new roman", 12,"bold"),width=20,height=14)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)


        #=================================buttons frame=============#
        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=100,pady=5,bg="pink1")
        framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(framebutton,command=self.add_data,text="Add Data",font=("times new roman", 12,"bold"),bg="light sky blue",width=23,fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(framebutton,command=self.showData,text="Show Data",font=("times new roman", 12,"bold"),bg="light sky blue",width=23,fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(framebutton,command=self.update,text="Update",font=("times new roman", 12,"bold"),bg="blue",width=23,fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(framebutton,command=self.delete,text="Delete",font=("times new roman", 12,"bold"),bg="blue",width=23,fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(framebutton,command=self.get_book_detail,text="Reset",font=("times new roman", 12,"bold"),bg="blue",width=23,fg="white")
        btnAddData.grid(row=0,column=5)

        btnAddData=Button(framebutton,command=self.exit,text="Exit",font=("times new roman", 12,"bold"),bg="blue",width=23,fg="white")
        btnAddData.grid(row=0,column=6)

         #=================================info frame=============#
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.libray_table=ttk.Treeview(Table_frame,column=('membertype','prn no','id',"name",'adress','mobile','book id','book title','author','date borrowed','date due','days','late return fine','date over due','final price'),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.libray_table.xview)
        yscroll.config(command=self.libray_table.yview)

        self.libray_table.heading("membertype",text="member type")
        self.libray_table.heading("prn no",text="prn no")
        self.libray_table.heading("id",text="id")
        # self.libray_table.heading("title",text="title")
        self.libray_table.heading("name",text="name")
        self.libray_table.heading("adress",text="adress")
        # self.libray_table.heading("postid",text="postid")
        self.libray_table.heading("mobile",text="mobile")
        self.libray_table.heading("book id",text="book id")
        self.libray_table.heading("book title",text="book title")
        self.libray_table.heading("author",text="author")
        self.libray_table.heading("date borrowed",text="date borrowed")
        self.libray_table.heading("date due",text="date due")
        self.libray_table.heading("days",text="days on book")
        self.libray_table.heading("late return fine",text="late return fine")
        self.libray_table.heading("date over due",text="date over due")
        self.libray_table.heading("final price",text="final price")
        
        self.libray_table["show"]="headings"
        self.libray_table.pack(fill=BOTH,expand=1)

        self.libray_table.column("membertype",width=100)
        
        
        

       
        self.libray_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="akhildatabase")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,Id=%s,name=%s,adress=%s,Mobile=%s,Bookid=%s,booktitle=%s,Author=%s,dateborrowed=%s,datedue=%s,daysonbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where Prn_no=%s",(self.member_var.get(),self.id_var.get(),self.name_var.get(),self.adress_var.get(),self.mobile_var.get(),self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.daysonbook_var.get(),self.lateratefine_var.get(),self.dateoverdue_var.get(),self.finalprice_var.get(),self.prn_var.get()))

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Updated")






    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="akhildatabase")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.member_var.get(),self.prn_var.get(),self.id_var.get(),self.name_var.get(),self.adress_var.get(),self.mobile_var.get(),self.bookid_var.get(),self.booktitle_var.get(),self.author_var.get(),self.dateborrowed_var.get(),self.datedue_var.get(),self.daysonbook_var.get(),self.lateratefine_var.get(),self.dateoverdue_var.get(),self.finalprice_var.get()))
       
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")
                                                                                                      
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="akhildatabase")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.libray_table.delete(*self.libray_table.get_children())
            for i in rows:
                self.libray_table.insert("",END,values=i)
            
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.libray_table.focus()
        content=self.libray_table.item(cursor_row)
        row=content["values"]

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.name_var.set(row[3])
        self.adress_var.set(row[4])
        
        self.mobile_var.set(row[5])
        self.bookid_var.set(row[6])
        self.booktitle_var.set(row[7])
        self.author_var.set(row[8])
        self.dateborrowed_var.set(row[9])
        self.datedue_var.set(row[10])
        self.dateoverdue_var.set(row[11])
        self.daysonbook_var.set(row[12])
        self.lateratefine_var.set(row[13])
        self.finalprice_var.set(row[14])


    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"Prn No\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID NO\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"NAME\t\t"+ self.name_var.get() + "\n")
        self.txtBox.insert(END,"ADRESS\t\t"+ self.adress_var.get() + "\n")
        self.txtBox.insert(END,"MOBILE\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"BOOK ID\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"BOOK TITLE\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"AUTHOR\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"DATE BORROWED\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DATE DUE\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DATE OVER DUE\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"DAYS ON BOOK\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"LATE RETURN FINE\t\t"+ self.lateratefine_var.get() + "\n")
        self.txtBox.insert(END,"FINAL PRICE\t\t"+ self.finalprice_var.get() + "\n")
    
    

    def get_book_detail(self):
        
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="akhildatabase")
        my_cursor=conn.cursor()
        sql_select_query = """select * from library where Id = %s"""
        # set variable in query
        value=(self.id_var.get(),)
        my_cursor.execute(sql_select_query, value)
        # fetch result
        record = my_cursor.fetchall()

        for row in record:
            
            print("Name= ", row[3], )
            print("Id= ", row[0])
            print("Bookid = ", row[6])
            print("date borrow  = ", row[8], "\n")
        
        self.txtBox.insert(END,"Name\t\t"+ row[3] + "\n")
        self.txtBox.insert(END,"Id\t\t"+ row[0] + "\n")
        self.txtBox.insert(END,"Bookid\t\t"+ row[6] + "\n")
        self.txtBox.insert(END,"date_b\t\t"+ row[9] + "\n")
        # self.txtBox.insert(END,"ADRESS\t\t"+ self.adress_var.get() + "\n")
        # self.txtBox.insert(END,"MOBILE\t\t"+ self.mobile_var.get() + "\n")
        # self.txtBox.insert(END,"BOOK ID\t\t"+ self.bookid_var.get() + "\n")
        # self.txtBox.insert(END,"BOOK TITLE\t\t"+ self.booktitle_var.get() + "\n")
        # self.txtBox.insert(END,"AUTHOR\t\t"+ self.author_var.get() + "\n")
        # self.txtBox.insert(END,"DATE BORROWED\t\t"+ self.dateborrowed_var.get() + "\n")
        # self.txtBox.insert(END,"DATE DUE\t\t"+ self.datedue_var.get() + "\n")
        # self.txtBox.insert(END,"DATE OVER DUE\t\t"+ self.dateoverdue_var.get() + "\n")
        # self.txtBox.insert(END,"DAYS ON BOOK\t\t"+ self.daysonbook_var.get() + "\n")
        # self.txtBox.insert(END,"LATE RETURN FINE\t\t"+ self.lateratefine_var.get() + "\n")
        # self.txtBox.insert(END,"FINAL PRICE\t\t"+ self.finalprice_var.get() + "\n")





    def reset(self):

        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.name_var.set("")
        self.adress_var.set("")
        # self.postid_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.dateoverdue_var.set("")
        self.daysonbook_var.set("")
        self.lateratefine_var.set("")
        self.finalprice_var.set("")

    def exit(self):
        iExit=tkinter.messagebox.askyesno("Library management System","Do u want to exit")
        if iExit>0:
            self.root.destroy()
            return


    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="akhildatabase")
            my_cursor=conn.cursor()
            query="delete from library where Prn_no=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Memeber has been deleted")



    
    


if __name__=="__main__":
    root=Tk()
    obj=LibraryManangementSystem(root)
    root.mainloop()
