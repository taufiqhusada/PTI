# program <kalkulator polynom sederhana>
# author : Taufiq Husada, M. Dafa Syarif, Tiffany Angelia, Rhesa Janitra
# deskripsi: program yang menerima masukan 2 polinom, kemudian melakukan operasi operasi pada polinom tersebut. Operasinya berupa: mencetak polinom, 
# menjumlahkan polinom, mengurangkan polinom, dan membuat turunan dari polinom

# kamus global:
# masukan,n1,n2,menu : int
# p1,p2: array of int
# isInt, isValid, stop, endprogram: boolean


def cetak(a, n):    # Fungsi untuk mecetak polinum yg berisikan koefisien dan derajat yg sudah diinput
    adaBukan0 = False   # inisialisasi boolean untuk ada atau tidaknya angka nol (0)
    if (n==0):  #jika derajat 0
      print(a[0])
    elif(n==1): # jika derajat 1
      if (a[0]==1): # jika koefisien nya 1, maka cukup print x, bukan 1x
        print("x",end="")
      elif (a[0]==-1):  # jika koefisiennya -1, maka cukup print -x, bukan -1x
        print("-x",end="")
      elif(a[0]!=0):  # selain -1,1,0
        print(str(a[0])+"x",end="")
      #else, 0 tidak dicetak

      if (a[0]==0): # jika koefisien pertama 0
        print(a[1])
      else: # jika koefisien pertama bukan 0
        if (a[1]>0):
          print(" + "+str(a[1]))
        elif(a[i]<0):
          print(" - "+str(-a[1]))
    else: # jika derajat lebih dari 1
        # Pemisalan untuk koefisien x pangkat n
      if (a[0]==1):   # fungsi tidak akan mencetak angka 1 (hanya berlaku untuk koefisien x pangkat tertinggi
                      # hingga x pangkat 1)
          print("x^" + str(n), end="")
          adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true
      elif (a[0]==-1):    # fungsi tidak akan mencetak angka -1 melainkan hanya - saja (hanya berlaku untuk koefisien x
                          # pangkat n hingga x pangkat 1
          print("-x^" + str(n), end="")
          adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true
      elif (a[0] > 0):
          print(str(a[0]) + "x^" + str(n),end="")
          adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true
      elif (a[0] < 0):
          print(str(a[0]) + "x^" + str(n),end="")
          adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true

      for i in range(1, n - 1):   # Inisialisasi Array pemisalan yang berlaku untuk
                                  # pangkat kedua terbesar hingga pangkat 2

          if (a[i] == 1): # fungsi tidak akan mencetak angka 1 (hanya berlaku untuk koefisien x pangkat tertinggi
                          # hingga x pangkat 1)
              if (adaBukan0): # Flow algoritma akan msk kesini jika adaBukan0 sdh menjadi True di flow sblmnya
                              # maka, simbol "+" dicetak
                  print(" + " + "x^" + str(n - i), end="") # Peletakan tanda " + " sebelum koefisien x
              else: # Flow algoritma akan msk kesini jika adaBukan0 masih False, maka simbol "+" tdk dicetak
                  print("x^" + str(n - i), end="")
              adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true
          elif (a[i] == -11):  # fungsi tidak akan mencetak angka -1 melainkan hanya - saja (hanya berlaku untuk koefisien x
                               # pangkat n hingga x pangkat 1
              if (adaBukan0):
                  print(" - " + "x^" + str(n - i), end="") # Peletakan tanda " - " & penghilangan angka -1 sebelum x
              else:
                  print("-x^" + str(n - i), end="")
              adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true
          elif (a[i] > 0):
              if (adaBukan0): # Flow algoritma akan msk kesini jika adaBukan0 sdh menjadi True di flow sblmnya
                              # maka, simbol "+" dicetak
                  print(" + " + str(a[i]) + "x^" + str(n - i), end="") # Peletakan tanda " + " sebelum koefisien x
              else: # Flow algoritma akan msk kesini jika adaBukan0 masih False, maka simbol "+" tdk dicetak
                  print(str(a[i]) + "x^" + str(n - i), end="")
              adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true
          elif (a[i] < 0):
              if (adaBukan0):
                  print(" - " + str(-a[i]) + "x^" + str(n - i), end="") # Mempositifkan bilangan kemudian menaruh
                                                                        # simbol "-" satu spasi sblm koefisien
              else:
                  print(str(a[i]) + "x^" + str(n - i), end="")
              adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true

      # Pemisalan untuk koefisien x pangkat 1
      if (a[n-1] == 1): # fungsi tidak akan mencetak angka 1 (hanya berlaku untuk koefisien x pangkat tertinggi
                        # hingga x pangkat 1)

          if (adaBukan0): # Flow algoritma akan msk kesini jika adaBukan0 sdh menjadi True di flow sblmnya
                          # maka, simbol "+" dicetak
              print(" + " + "x", end="") # Peletakan tanda " + " sebelum koefisien x
          else: # Flow algoritma akan msk kesini jika adaBukan0 masih False, maka simbol "+" tdk dicetak
              print("x", end="")
          adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true
      elif (a[n-1] == -1):  # fungsi tidak akan mencetak angka -1 melainkan hanya - saja (hanya berlaku untuk koefisien x
                            # pangkat n hingga x pangkat 1
          if (adaBukan0):
              print(" - " + "x", end="")
          else:
              print("-x", end="")
          adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true
      elif a[n - 1] > 0:
          if (adaBukan0): # Flow algoritma akan msk kesini jika adaBukan0 sdh menjadi True di flow sblmnya
                          # maka, simbol "+" dicetak
              print(" + " + str(a[n-1]) + "x" , end="") # Peletakan tanda " + " sebelum koefisien x
          else: # Flow algoritma akan msk kesini jika adaBukan0 masih False, maka simbol "+" tdk dicetak
              print(str(a[n-1]) + "x" , end="")
          adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true
      elif a[n - 1] < 0:
          if (adaBukan0): #
              print(" - " + str(-a[n-1]) + "x" , end="") # Mempositifkan bilangan kemudian menaruh
                                                         # simbol "-" satu spasi sblm koefisien
          else:
              print(str(a[n-1]) + "x" , end="")
          adaBukan0 = True #Setiap terdapat koefisien pd X pangkat n sampai 1, maka boolean adaBukan0 akan menjadi true

      # Pemisalan untuk koefisien x pangkat nol atau konstanta
      if a[n] > 0:

          if(adaBukan0): # Flow algoritma akan msk kesini jika adaBukan0 sdh menjadi True di flow sblmnya
                         # maka, simbol "+" dicetak
              print(" + " + str(a[n])) # Peletakan tanda " + " sebelum koefisien x
          else: # Flow algoritma akan msk kesini jika adaBukan0 masih False, maka simbol "+" tdk dicetak
              print(str(a[n]))
      elif a[n] < 0:
          if(adaBukan0):
              print(" - " + str(-a[n])) # Mempositifkan bilangan kemudian menaruh
                                        # simbol "-" satu spasi sblm koefisien
          else:
              print(str(a[n]))
# prosedur turunan
def turunan(p,n):
  c = [0 for i in range(n)]    # insilasisasi array turunan
  for i in range(n):
    c[i] = (n-i)*p[i]     # mengalikan koefisien dengan pangkat-1
  cetak(c,n-1)   # mencetak polinom hasil turunan

# prosedur penjumlahan
def penjumlahan(p1, p2, n1, n2):
    pHasil = [0 for i in range(max(n1,n2)+1)]    #inisialisasi array untuk emnyimpan koefisien hasil penjumlahan
    if (n1>n2):   # jika derajat polinom 1 lebih besar dari derajat polinom 2
      for i in range(n1-n2): 
        pHasil[i] = p1[i];  # karena p1 derajatnya lebih tinggi, maka suku awal pHasil mengikuti p1
      for i in range(n1-n2,n1+1): 
        pHasil[i] = p1[i]+p2[i-(n1-n2)] #menjumlahkan sisanya
    else:       # jika derajat polinom 2 lebih besar dari derajat polinom 1
      for i in range(n2-n1):  
        pHasil[i] = p2[i]   # karena p1 derajatnya lebih tinggi, maka suku awal pHasil mengikuti p2
      for i in range(n2-n1,n2+1):
        pHasil[i] = p1[i-(n2-n1)]+p2[i] # menjumlahkan sisanya
    cetak(pHasil,max(n1,n2))   # cetak polinom hasil penjumlahan


# proses pengurangan
def pengurangan(p1, p2, n1, n2):
    pHasil = [0 for i in range(max(n1,n2)+1)]    #inisialisasi array untuk menyimpan koefisien hasiil pengurangan
    if (n1>n2):   # jika derajat polinom 1 lebih besar dari derajat polinom 2
      for i in range(n1-n2):
        pHasil[i] = p1[i];  # karena p1 derajatnya lebih tinggi, maka suku awal pHasil mengikuti p1
      for i in range(n1-n2,n1+1):
        pHasil[i] = p1[i]-p2[i-(n1-n2)] # mengurangkan sisanya
    else:     #jika derajat polinom 2 lebih besar daripada derajat polinom 1
      for i in range(n2-n1):
        pHasil[i] = -p2[i]  # karena p1 derajatnya lebih tinggi, maka suku awal pHasil mengikuti p2
      for i in range(n2-n1,n2+1):
        pHasil[i] = p1[i-(n2-n1)]-p2[i] # mengurangkan sisanya
    cetak(pHasil,max(n1,n2))   # mencetak polinom hasil pengurangan

# main program

# proses menginput polinom pertama

# proses menginputkan derajat polinom pertama
isInt = False   
while(isInt==False):    # jika masukan bukan bilangan bulat maka, pembacaan akan dilakukan terus menerus hingga masukan merupakan sebuah int
  try:
    n1 = int(input("masukkan derajat polynom pertama: "))   # derajat polynom pertama
    isInt = True      # jika masukan bilangan bulat maka pembcaan diakhiri
  except ValueError:      # jika masukan bukan bilangan bulat
    print("")
    print("masukan bukan sebuah bilangan bulat,ulangi masukan") # print pesan yang menunjukkan bahwa pengguna salah memasukkan input
    print("") 

# proses menginputkan koefisien dari suku suku polinom 1
p1 = [0 for i in range(n1+1)];  #inisialisasi array koefisien dari polynom pertama
stop = False  # inisialisasi boolean stop
i = 0   # inisialisasi i
while(i<=n1 and stop == False):   # jika pembacaan masih dilakukan
  isInt = False
  while(isInt==False):
    try:
      masukan = int(input("masukkan koefisien x^ "+str(n1-i)+" : "))    #input
      isInt = True    #masukan benar(int)
    except:
      print("")
      print("masukan bukan sebuah bilangan bulat,ulangi masukan") # print pesan yang menunjukkan bahwa pengguna salah memasukkan input
      print("")

  if (masukan == -999):   # jika masukan -999, maka pembacaan dihentikan
    stop = True
  else:     # jika masukan bukan -999, maka simpan di array
    p1[i] = masukan
    i+=1;

# proses menginput polinom kedua

# proses menginputkan derajat polinom 2
isInt = False   # inisialisasi boolean
while(isInt==False):    # jika masukan bukan bilangan bulat maka, pembacaan akan dilakukan terus menerus hingga masukan merupakan sebuah int
  try:
    n2 = int(input("masukkan derajat polynom kedua: "))   # derajat polynom pertama
    isInt = True      # jika masukan bilangan bulat maka pembcaan diakhiri
  except ValueError:      # jika masukan bukan bilangan bulat
    print("")
    print("masukan bukan sebuah bilangan bulat,ulangi masukan") # print pesan yang menunjukkan bahwa pengguna salah memasukkan input
    print("") 

# proses menginputkan koefisien dari suku suku polinom 2
p2 = [0 for i in range(n2+1)];  # inisialisasi array koefisien dari polynom kedua
stop = False  # insialisasi boolean stop
i = 0;    # inisialisasi i
while(i<=n2 and stop == False):   # jika pembacaan masih dilakukan
  isInt = False
  while(isInt==False):
    try:
      masukan = int(input("masukkan koefisien x^ "+str(n2-i)+" : "))    #input
      isInt = True    #masukan benar (int)
    except:
      print("")
      print("masukan bukan sebuah bilangan bulat,ulangi masukan") # print pesan yang menunjukkan bahwa pengguna salah memasukkan input
      print("")

  if (masukan == -999):   # jika masukan -999, pembacaan dihentikan
    stop = True
  else:   # jika masukan bukan -999, maka simpan di array
    p2[i] = masukan   
    i+=1;

print("")   # sebagai line kosonng

# Proses pemilihan menu

# Mencetak daftar menu
print("MENU")
print("1. Mencetak polynom 1 dan polynom 2")
print("2. Menjumlahkan polynom 1 dan polynom 2")
print("3. Mengurangkan polynom 1 dan polynom 2")
print("4. Membuat turunan dari polynom 1 dan polynom 2")
print("0. Mengakhiri program")
print("") # line kosong

endprogram = False    # insialisasi boolean endprogram yang menunjukkan pembacaan menu masih dilakukan
while(endprogram==False): #jika program masih berjalan 
  isValid = False   # inisalisasi boolean
  while(isValid==False):  # jika masukan belum valid, maka pembacaan akan terus dilakukan hingga masukan valid
    try:
      menu = int(input("masukkan menu (1/2/3/4/0): "))    # memasukan input dari user
      if (menu == 1 or menu == 2 or menu == 3 or menu == 4 or menu == 0): #jika masukan valid
        isValid = True
      else:   # jika masukan tidak valid, namun masih berupa int
        print("masukan salah, ulangi masukan, menu haruslah (0/1/2/3/4)") # print pesan yang menunjukkan bahwa pengguna salah memasukkan input
    except ValueError:    # jika masukan bukanlah int
      print("masukan salah, ulangi masukan, menu haruslah (0/1/2/3/4)") # print pesan yang menunjukkan bahwa pengguna salah memasukkan input

  if (menu==1):   # jika menu 1, maka mencetak nilai polynom
    print("polinom 1:")
    cetak(p1,n1)  # call fungsi cetak
    print("") #line kosong sebagi penjarak
    print("polinom 2:")
    cetak(p2,n2)  # call fungsi cetak
    print("") #line kosong sebagi penjarak
  elif (menu==2):   # jika menu 2 maka penjumlahan polynom
    print("hasil penjumlahan polinom 1 dan 2:")
    penjumlahan(p1,p2,n1,n2)  # call fungsi penjumlahan
    print("") #line kosong sebagi penjarak
  elif (menu==3):   # jika menu 3 pengurangan polynom
    print("hasil pengurangan polinom 1 dan 2")
    pengurangan(p1,p2,n1,n2)  # call fungsi pengulangan
    print("") #line kosong sebagi penjarak
  elif (menu==4):   # jika menu 4 maka turunan polynom
    print("turunan polinom 1")
    turunan(p1,n1)  # call fungsi turunan
    print("") #line kosong sebagi penjarak
    print("turunan polinom 2")  
    turunan(p2,n2)  # call fungsi turunan
    print("") #line kosong sebagi penjarak
  elif (menu==0):   # jika menu = 0, program selesai
    endprogram = True # jadikan bool endprogram jadi true, agar loop berakhir




