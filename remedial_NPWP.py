#Wayne Untu (Kelas Data Science 08, remedial modul 01)

def cekNPWP(x):
    a1=0
    a2=0
    b=0
    c=0
    d=0
    e=0
    f=0
    y=len(x)
    t_pertama = x.find('.') #2
    t_kedua = x.find('.', t_pertama+1, len(x)) #6
    t_ketiga = x.find('.', t_kedua+1, len(x)) #10
    s_pertama = x.find('-') #12
    t_keempat = x.find('.', t_ketiga+1, len(x)) #16
    part1 = x[0:t_pertama]
    part2 = x[(t_pertama+1):t_kedua]
    part3 = x[(t_kedua+1):t_ketiga]
    part4 = x[(t_ketiga+1):s_pertama]
    part5 = x[(s_pertama+1):t_keempat]
    part6 = x[(t_keempat+1):]
    
    a1a1= 1
    a2a2= 1
    bb=len(part2)
    cc=len(part3)
    dd=len(part4)
    ee=len(part5)
    ff=len(part6)

    #identitas 1: identitas wajib pajak DONE
    for i in range(0, t_pertama-1):
        if(x[i]=='0'): 
            a1=a1+1
    for i in range(t_pertama-1, t_pertama):
        if(((x[i]=='1') or (x[1]=='2') or (x[1]=='3') or (x[1]=='4')or (x[1]=='5')or (x[1]=='6') or (x[1]=='7') or (x[1]=='8') or (x[1]=='9'))):
            a2=a2+1
    for i in range (t_pertama+1, t_kedua): #identitas 2: nomor urut partA DONE
        if(x[i]=='1') or (x[i]=='2') or (x[i]=='3') or (x[i]=='4')or (x[i]=='5')or (x[i]=='6') or (x[i]=='7') or (x[i]=='8') or (x[i]=='9') or (x[i]=='0'):
            b=b+1
    for i in range (t_kedua+1, t_ketiga): #identitas 3: nomor urut partB DONE
        if(x[i]=='1') or (x[i]=='2') or (x[i]=='3') or (x[i]=='4')or (x[i]=='5')or (x[i]=='6') or (x[i]=='7') or (x[i]=='8') or (x[i]=='9') or (x[i]=='0'):
            c=c+1
    for i in range (t_ketiga+1, s_pertama): #identitas 4: pengaman
        if(x[i]=='1') or (x[i]=='2') or (x[i]=='3') or (x[i]=='4')or (x[i]=='5')or (x[i]=='6') or (x[i]=='7') or (x[i]=='8') or (x[i]=='9') or (x[i]=='0'):
            d=d+1   
    for i in range (s_pertama+1, t_keempat): #identitas 5: kode KPP
        if(x[i]=='1') or (x[i]=='2') or (x[i]=='3') or (x[i]=='4')or (x[i]=='5')or (x[i]=='6') or (x[i]=='7') or (x[i]=='8') or (x[i]=='9') or (x[i]=='0'):
            e=e+1
    for i in range (t_keempat+1, len(x)): #identitas 6: status wajib pajak
        if(x[i]=='1') or (x[i]=='2') or (x[i]=='3') or (x[i]=='4')or (x[i]=='5')or (x[i]=='6') or (x[i]=='7') or (x[i]=='8') or (x[i]=='9') or (x[i]=='0'):
            f=f+1    

    if(len(x) == 20 and t_pertama == 2 and t_kedua==6 and t_ketiga==10 and s_pertama==12 and t_keempat==16 and a1==a1a1 and a2==a2a2 and b==bb and c==cc and d==dd and e==ee and f==ff):
        print("Kode seri NPWP valid!", '\n' 'Identitas Wajib Pajak:', part1, '\n' 'Nomor Registrasi:', part2+'.'+part3, '\n' 'Alat Pengaman:', part4, '\n' 'Kode KPP:', part5, '\n' 'Status Wajib Pajak:', part6)
    else:
       print("Kode seri NPWP tidak valid!")
    # Jika ingin cek, silahkan un-command perintah-perintah 'print' di bawah ini:
    # print('a1', a1, a1a1)
    # print('a2', a2, a2a2)
    # print('b', b, bb)
    # print('c', c, cc)
    # print('d', d, dd)
    # print('e', e, ee)
    # print('f', f, ff)


cekNPWP('02.123.456.0-212.191')