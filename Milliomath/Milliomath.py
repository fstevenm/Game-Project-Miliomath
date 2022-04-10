import tkinter,tkinter.messagebox
import random

class Pertanyaan():
    def __init__(self,tanya,jawab,yang_benar):
        self.tanya=tanya
        self.jawab=jawab
        self.yang_benar=yang_benar
        
    def cek(self,tulisan,view):
        global benar
        
        if (tulisan==self.yang_benar):
            benar += 1
            if benar==1:
                jeda.config(text="BENAR")
                skor10.config(text="Rp. 2.000.000,00",bg='red')
            elif benar==2:
                jeda.config(text="BENAR")
                skor10.config(text="Rp. 2.000.000,00",bg='lightgrey')
                skor9.config(bg='red')
            elif benar==3:
                jeda.config(text="BENAR")
                skor10.config(bg='lightgrey')
                skor9.config(bg='lightgrey')
                skor8.config(bg='red')
            elif benar==4:
                jeda.config(text="BENAR")
                skor10.config(bg='lightgrey')
                skor9.config(bg='lightgrey')
                skor8.config(bg='lightgrey')
                skor7.config(bg='red')
            elif benar==5:
                jeda.config(text="BENAR")
                skor10.config(bg='lightgrey')
                skor9.config(bg='lightgrey')
                skor8.config(bg='lightgrey')
                skor7.config(bg='lightgrey')
                skor6.config(bg='red')
            elif benar==6:
                jeda.config(text="BENAR")
                skor10.config(bg='lightgrey')
                skor9.config(bg='lightgrey')
                skor8.config(bg='lightgrey')
                skor7.config(bg='lightgrey')
                skor6.config(bg='lightgrey')
                skor5.config(bg='red')
            elif benar==7:
                jeda.config(text="BENAR")
                skor10.config(bg='lightgrey')
                skor9.config(bg='lightgrey')
                skor8.config(bg='lightgrey')
                skor7.config(bg='lightgrey')
                skor6.config(bg='lightgrey')
                skor5.config(bg='lightgrey')
                skor4.config(bg='red')
            elif benar==8:
                jeda.config(text="BENAR")
                skor10.config(bg='lightgrey')
                skor9.config(bg='lightgrey')
                skor8.config(bg='lightgrey')
                skor7.config(bg='lightgrey')
                skor6.config(bg='lightgrey')
                skor5.config(bg='lightgrey')
                skor4.config(bg='lightgrey')
                skor3.config(bg='lightgrey')
                skor2.config(bg='red')
            elif benar==9:
                jeda.config(text="BENAR")
                skor10.config(bg='lightgrey')
                skor9.config(bg='lightgrey')
                skor8.config(bg='lightgrey')
                skor7.config(bg='lightgrey')
                skor6.config(bg='lightgrey')
                skor5.config(bg='lightgrey')
                skor3.config(bg='lightgrey')
                skor2.config(bg='lightgrey')
                skor1.config(bg='red')
                tkinter.messagebox.showinfo("WINNER","Selamat anda menang")
        else :
            jeda.config(text="SALAH")
            benar=0 
            answer=tkinter.messagebox.askquestion("KALAH","ULANG?")
            if answer=='yes':
                jeda.config(text="SEMANGAT")
                skor10.config(bg='grey')
                skor9.config(bg='grey')
                skor8.config(bg='grey')
                skor7.config(bg='grey')
                skor6.config(bg='grey')
                skor5.config(bg='grey')
                skor4.config(bg='grey')
                skor3.config(bg='grey')
                skor2.config(bg='grey')
                skor1.config(bg='grey') 
                question=[]
                tanya_pertanyaan()
            else :
                window.destroy()
           
        
        view.after(1, lambda: self.unpackView(view)) 
        
    def getView(self, window):

        view = tkinter.Frame(window)

        pilih=tkinter.Label(jendela1c,font=("Arial 18 bold"),text=self.tanya,
                                        bg='blue',fg='white',bd=5,
                                        width=44,justify=tkinter.CENTER)
        pilih.grid(row=0,column=0,columnspan=4,pady=4)
        
        label_pilihA=tkinter.Label(jendela1c,font=("Arial 14 bold"),
                                text="A: ",bg='black',fg='white',bd=5,
                                justify=tkinter.CENTER)
        label_pilihA.grid(row=1,column=0,pady=4,sticky=tkinter.W)
        pilih1=tkinter.Button(jendela1c,font=("Arial 14 bold"),text=self.jawab[0],
                                bg='blue',fg='white',bd=5,
                                width=17,justify=tkinter.CENTER,command=lambda: self.cek("A", view))
        pilih1.grid(row=1,column=1)

        label_pilihB=tkinter.Label(jendela1c,font=("Arial 14 bold"),
                                text="B: ",bg='black',fg='white',bd=5,
                                justify=tkinter.CENTER)
        label_pilihB.grid(row=1,column=2,pady=4,sticky=tkinter.W)
        pilih2=tkinter.Button(jendela1c,font=("Arial 14 bold"),text=self.jawab[1],
                                bg='blue',fg='white',bd=5,
                                width=17,justify=tkinter.CENTER,command=lambda: self.cek("B", view))
        pilih2.grid(row=1,column=3,pady=4)

        label_pilihC=tkinter.Label(jendela1c,font=("Arial 14 bold"),
                                text="C: ",bg='black',fg='white',bd=5,
                                justify=tkinter.CENTER)
        label_pilihC.grid(row=2,column=0,pady=4,sticky=tkinter.W)
        pilih3=tkinter.Button(jendela1c,font=("Arial 14 bold"),text=self.jawab[2],
                                bg='blue',fg='white',bd=5,
                                width=17,justify=tkinter.CENTER,command=lambda: self.cek("C", view))
        pilih3.grid(row=2,column=1,pady=4)

        label_pilihD=tkinter.Label(jendela1c,font=("Arial 14 bold"),
                                text="D: ",bg='black',fg='white',bd=5,
                                justify=tkinter.CENTER)
        label_pilihD.grid(row=2,column=2,pady=4,sticky=tkinter.W)
        pilih4=tkinter.Button(jendela1c,font=("Arial 14 bold"),text=self.jawab[3],
                                bg='blue',fg='white',bd=5,
                                width=17,justify=tkinter.CENTER,command=lambda: self.cek("D", view))
        pilih4.grid(row=2,column=3,pady=4)

        return view

    def unpackView(self, view):
        view.grid_forget()
        tanya_pertanyaan()

def tanya_pertanyaan():
    global questions, window, index, button, benar, number_of_questions 
    if (len(questions) == index + 1):
        tkinter.Label(window, text="Terima kasih sudah menjawab "
              + str(benar) + " dari " + str(number_of_questions)
              + " questions answered right").grid()
    welcome.grid_forget()
    index += 1
    questions[index].getView(window).grid()
    

questions = []
file = open("questions.txt","r")
line = file.readline()
while(line != ""):
    tanyaString = line
    jawab = []
    for i in range (4):
        jawab.append(file.readline())

    yang_benar = file.readline()
    yang_benar = yang_benar[:1]
    questions.append(Pertanyaan(tanyaString, jawab, yang_benar))
    line = file.readline()
random.shuffle(questions)
    
index = -1
benar = 0
number_of_questions = len(questions) 
 
 
 
window=tkinter.Tk()
window.title("MILLOMATHEMATICS")
window.geometry("1200x680")
window.configure(bg='black')
#=====================FRAME=====================
#jendela = tkinter.Frame(window,bg='black')
#jendela.grid()

jendela1 = tkinter.Frame(window,bg='black',bd=20,width=900,height=600)
jendela1.grid(row=0,column=0)
jendela2 = tkinter.Frame(window,bg='grey',bd=20,width=450,height=600)
jendela2.grid(row=0,column=1)

jendela1a = tkinter.Frame(jendela1,bg='black',bd=20,width=900,height=200)
jendela1a.grid(row=0,column=0)
jendela1b = tkinter.Frame(jendela1,bg='black',bd=20,width=900,height=220)
jendela1b.grid(row=1,column=0)
jendela1c = tkinter.Frame(jendela1,bg='black',bd=20,width=900,height=200)
jendela1c.grid(row=2,column=0)

#=====================FUNGSIGAMBAR=====================

def ganti_50():
    canvas = tkinter.Canvas(jendela1a,bg='black',
                            width=180,height=80)
    canvas.grid(row=0,column=0)
    canvas.delete("all")
    gambarbaru = tkinter.PhotoImage(file='50x.png')
    canvas.create_image(90,40, image=gambarbaru)
    canvas.image=gambarbaru

def ganti_orang():
    canvas = tkinter.Canvas(jendela1a,bg='black',
                            width=180,height=80)
    canvas.grid(row=0,column=1)
    canvas.delete("all")
    gambarbaru = tkinter.PhotoImage(file='orangx.png')
    canvas.create_image(90,40, image=gambarbaru)
    canvas.image=gambarbaru
    
def ganti_phone():
    canvas = tkinter.Canvas(jendela1a,bg='black',
                            width=180,height=80)
    canvas.grid(row=0,column=2)
    canvas.delete("all")
    gambarbaru = tkinter.PhotoImage(file='phonex.png')
    canvas.create_image(90,40, image=gambarbaru)
    canvas.image=gambarbaru
    
    
#=====================GAMBAR=====================

gambar_tengah=tkinter.PhotoImage(file='centre.png')
gambar1=tkinter.Label(jendela1b,image=gambar_tengah,
                      bg='black',width=300,height=200)
gambar1.grid()

g_50=tkinter.PhotoImage(file='50.png')
gambar50=tkinter.Button(jendela1a,image=g_50,
                      bg='black',width=180,height=80,
                        command=ganti_50)
gambar50.grid(row=0,column=0)

g_phone=tkinter.PhotoImage(file='phone.png')
gambarphone=tkinter.Button(jendela1a,image=g_phone,
                      bg='black',width=180,height=80,
                           command=ganti_phone)
gambarphone.grid(row=0,column=2)

g_orang=tkinter.PhotoImage(file='orang.png')
gambarorang=tkinter.Button(jendela1a,image=g_orang,
                      bg='black',width=180,height=80,
                           command=ganti_orang)
gambarorang.grid(row=0,column=1)

#=====================Button,Label=====================
welcome=tkinter.Button(jendela1c,text="SELAMAT DATANG",font="Arial 50",width=20,justify="right"
                      ,relief="ridge",bd=5,command=tanya_pertanyaan)
welcome.grid(column=0,row=0,columnspan=5)

jeda=tkinter.Label(jendela1b,text="SOAL",font="Times 10",width=10,height=2,justify="center"
                   ,bg='black',fg='white')
jeda.grid(column=0,row=2,columnspan=5,rowspan=2)


#==========================================SKOR
highlight=tkinter.Label(jendela2,text="Apakah anda dapat menjadi juara?\n\n\n\n",
                        font="Arial 12 bold",bg='grey',fg='white')
highlight.grid(row=0,column=0)

skor1=tkinter.Label(jendela2,text="Rp. 300.000.000,00",font="Arial 20",bg='grey',fg='white')
skor2=tkinter.Label(jendela2,text="Rp. 150.000.000,00",font="Arial 20",bg='grey',fg='white')
skor3=tkinter.Label(jendela2,text="Rp. 75.000.000,00",font="Arial 20",bg='grey',fg='white')
skor4=tkinter.Label(jendela2,text="Rp. 50.000.000,00",font="Arial 20",bg='grey',fg='white')
skor5=tkinter.Label(jendela2,text="Rp. 40.000.000,00",font="Arial 20",bg='grey',fg='white')
skor6=tkinter.Label(jendela2,text="Rp. 30.000.000,00",font="Arial 20",bg='grey',fg='white')
skor7=tkinter.Label(jendela2,text="Rp. 15.000.000,00",font="Arial 20",bg='grey',fg='white')
skor8=tkinter.Label(jendela2,text="Rp. 8.000.000,00",font="Arial 20",bg='grey',fg='white')
skor9=tkinter.Label(jendela2,text="Rp. 5.000.000,00",font="Arial 20",bg='grey',fg='white')
skor10=tkinter.Label(jendela2,text="Rp. 2.000.000,00",font="Arial 20",bg='grey',fg='white')
skor1.grid(row=1,column=0)
skor2.grid(row=2,column=0)
skor3.grid(row=3,column=0)
skor4.grid(row=4,column=0)
skor5.grid(row=5,column=0)
skor6.grid(row=6,column=0)
skor7.grid(row=7,column=0)
skor8.grid(row=8,column=0)
skor9.grid(row=9,column=0)
skor10.grid(row=10,column=0)


window.mainloop()