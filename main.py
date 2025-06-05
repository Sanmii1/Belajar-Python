# Import Libary Yang Digunakan
from tkinter import *
import re

#------------Note------------#
# Syntax Format
# varName : Type Data = ....
#------------Inisiasi variabel------------#
VALUE : str = "0"  # variabel pertama untuk menyimpan nilai perhitungan
TEMPORARY_VALUE : str = "" # variabel kedua untuk menyimpan nilai perhitungan


#------------Kode------------#
window : object = Tk() # inisiasi object Tk
window.geometry("350x400") # Mengatur Panjang Dan Lebar argumen pertama lebar, argumen kedua panjang/tinggi
window.title("Calculator") # Mengatur Judul Aplikasi
window.resizable(False,False)
icon : object = PhotoImage(file='icon.png') # Tempat untuk menyimpan foto yang mau digunakan 
window.iconphoto(True, icon) # set ke aplikasi kita agar bisa menggunakan fotonya argumen pertama nilai  True -> menerapkan ke window yang lain, False -> hanya window ini saja
window.config(background="#21252b") # Mengubah warna background

labelResult : object = Label(window, text=VALUE,background="#21252b", fg="white",font=("Arial",50,"normal"),width=8,anchor="e") # Untuk membuat teks di window dengan properti yang sesuai
labelResult.grid(row=0, column=0, columnspan=4, sticky="e") # Atur Lokasi dan lebar label nya


# Fungsi untuk menampilkan angka sesuai dengan tombol angka yang di pencet
def inputNumber(number: int) -> str :
    global VALUE

    # Logic untuk menghilangkan angka 0 di saat ada angka masuk
    if len(VALUE) == 1 and VALUE == "0" : 
        VALUE = str(number)
        labelResult.config(text = VALUE )
    else :
        VALUE += str(number)
        labelResult.config(text = VALUE )

# Fungsi untuk operator yang dipilih 
def inputOperator(arg : str) -> str :
    global VALUE
    global TEMPORARY_VALUE

    # Kondisi untuk Operator Pangkat dan akar 
    if arg == "exp" :
        OPVALUE  :str = str(int(VALUE)**2)
        TEMPORARY_VALUE += OPVALUE
        labelResult.config(text = OPVALUE)
        VALUE =""
    elif arg == "root" :
        OPVALUE :str = str(int(VALUE)**0.5)
        TEMPORARY_VALUE += "{:.2f}".format(float(OPVALUE))
        labelResult.config(text = "{:.2f}".format(float(OPVALUE)))
        VALUE =""

    # Kondisi untuk operator bukan dari keduanya
    else :    
        TEMPORARY_VALUE += VALUE
        VALUE = "0"

        labelResult.config(text= VALUE)

        match arg :
            case "sum" :
                TEMPORARY_VALUE +=",+"
            case "sub" :
                TEMPORARY_VALUE += ",-"
            case "div" :
                TEMPORARY_VALUE += ",/"
            case "mul" :
                TEMPORARY_VALUE += ",*"

# Fungsi untuk perhitungan matematika
def handleMath() -> str :
    global VALUE
    global TEMPORARY_VALUE
    TEMPORARY_VALUE = TEMPORARY_VALUE + VALUE
    VALUE_ARRAY : list[str] = re.split(r"[,]",TEMPORARY_VALUE)
    OPERATOR_RESULT :str = VALUE_ARRAY[0]
    skip :int = 0
    for e in VALUE_ARRAY :
        if skip > 0 :
            OPERATOR_RESULT :str = str(eval(OPERATOR_RESULT+e))
        skip += 1

    VALUE = OPERATOR_RESULT   
    TEMPORARY_VALUE = ""
    labelResult.config(text = VALUE)

# Fungsi untuk menambahkan koma
def comaButton() -> str :
    global TEMPORARY_VALUE
    global VALUE
    VALUE += "."
    labelResult.config(text = VALUE)

# Fungsi untuk menghapus per nomor
def deleteButton() -> None :
    global VALUE

    VALUE = VALUE[:-1]
    labelResult.config(text = VALUE) 

# Fungsi untuk mereset 
def resetButton () -> str :
    global VALUE
    global TEMPORARY_VALUE

    VALUE = "0"
    TEMPORARY_VALUE= ""
    labelResult.config(text = VALUE)

# Menambahkan beberapa widget button 
buttonZero = Button(window,text="0",width=10, height=3,background="white",command=lambda: inputNumber(0))
buttonOne = Button(window,text="1",width=10, height=3,background="white",command=lambda: inputNumber(1))
buttonTwo = Button(window,text="2",width=10, height=3,background="white",command=lambda: inputNumber(2))
buttonThree = Button(window,text="3",width=10, height=3,background="white",command=lambda: inputNumber(3))
buttonFour = Button(window,text="4",width=10, height=3,background="white",command=lambda: inputNumber(4))
buttonFive = Button(window,text="5",width=10, height=3,background="white",command=lambda: inputNumber(5))
buttonSix = Button(window,text="6",width=10, height=3,background="white",command=lambda: inputNumber(6))
buttonSeven = Button(window,text="7",width=10, height=3,background="white",command=lambda: inputNumber(7))
buttonEight = Button(window,text="8",width=10, height=3,background="white",command=lambda: inputNumber(8))
buttonNine = Button(window,text="9",width=10, height=3,background="white",command=lambda: inputNumber(9))
buttonEqual = Button(window,text="=",width=10, height=3,background="#F08C2F",command=lambda: handleMath())
buttonSum = Button(window,text="+",width=10, height=3,background="white",command=lambda: inputOperator("sum"))
buttonSubtract = Button(window,text="-",width=10, height=3,background="white",command=lambda: inputOperator("sub"))
buttonDivide = Button(window,text=":",width=10, height=3,background="white",command=lambda: inputOperator("div"))
buttonMultiply = Button(window,text="*",width=10, height=3,background="white",command=lambda: inputOperator("mul"))
buttonReset = Button(window,text="c",width=10, height=3,background="white",command=lambda: resetButton())
buttonFraction = Button(window,text="DEL",width=10, height=3,background="white",command=lambda: deleteButton())
buttonComa = Button(window,text=",",width=10, height=3,background="white",command=lambda: comaButton())
buttonExp = Button(window,text="x²",width=10, height=3,background="white",command=lambda: inputOperator("exp"))
buttonRoot = Button(window,text="√x",width=10, height=3,background="white",command=lambda: inputOperator("root"))


# Mengatur Layout dengan sistem grid untuk setiap widget
buttonFraction.grid(row=1, column=0,padx=3,pady=2)
buttonExp.grid(row=1, column=1,padx=3,pady=2)
buttonRoot.grid(row=1, column=2,padx=3,pady=2)
buttonReset.grid(row=1,column=3,padx=3,pady=2)
buttonSeven.grid(row=2, column=0,padx=3,pady=2)
buttonEight.grid(row=2, column=1,padx=3,pady=2)
buttonNine.grid(row=2, column=2,padx=3,pady=2)
buttonSum.grid(row=2,column=3,padx=3,pady=2)
buttonFour.grid(row=3, column=0,padx=3,pady=2)
buttonFive.grid(row=3, column=1,padx=3,pady=2)
buttonSix.grid(row=3, column=2,padx=3,pady=2)
buttonSubtract.grid(row=3,column=3,padx=3,pady=2)
buttonOne.grid(row=4, column=0,padx=3,pady=2)
buttonTwo.grid(row=4, column=1,padx=3,pady=2)
buttonThree.grid(row=4, column=2,padx=3,pady=2)
buttonMultiply.grid(row=4,column=3,padx=3,pady=2)
buttonEqual.grid(row=5, column=0,padx=3,pady=2)
buttonComa.grid(row=5, column=1,padx=3,pady=2)
buttonZero.grid(row=5, column=2,padx=3,pady=2)
buttonDivide.grid(row=5,column=3,padx=3,pady=2)

window.mainloop() # Agar bisa tampil/muncul di layar sampai tombol close di pencet

