import os

satuan=('nol','satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan')

def terbilang(n):
    if n>=1_000_000_000_000:
        return terbilang(n//1_000_000_000_000) + ' triliun ' + (terbilang(n%1_000_000_000_000) if n%1_000_000_000_000!=0 else '')
    elif n>=1_000_000_000:
        return terbilang(n//1_000_000_000) + ' miliyar ' + (terbilang(n%1_000_000_000) if n%1_000_000_000!=0 else '')
    elif n>=1_000_000:
        return terbilang(n//1_000_000) + ' juta ' + (terbilang(n%1_000_000) if n%1_000_000!=0 else '')
    elif n>=1000:
        if n//1000==1:
            return 'seribu ' + (terbilang(n%1000) if n%1000!=0 else '')
        else:
            return terbilang(n//1000) + ' ribu ' + (terbilang(n%1000) if n%1000!=0 else '')
    elif n>=100:
        if n//100==1:
            return 'seratus ' + (terbilang(n%100) if n%100!=0 else '')
        else:
            return terbilang(n//100) + ' ratus ' + (terbilang(n%100) if n%100!=0 else '')
    elif n>=20:
        return terbilang(n//10) + ' puluh ' + (terbilang(n%10) if n%10!=0 else '')
    elif n>=12:
        return terbilang(n%10) + ' belas'
    elif n==11:
        return 'sebelas'
    elif n==10:
        return 'sepuluh'
    else:
        return satuan[n]

num=('Zero','one','two','three','four','five','six','seven','eight','nine',
    'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')

def tersaid(n):
    if n<20:
        return num[n]
    elif n>=1_000_000_000:
        return tersaid(n//1_000_000_000) + ' billion ' + (tersaid(n%1_000_000_000) if n%1_000_000_000!=0 else '')
    elif n>=1_000_000:
        return tersaid(n//1_000_000) + ' million ' + (tersaid(n%1_000_000) if n%1_000_000!=0 else '')
    elif n>=1000:
        return tersaid(n//1000) + ' thousand ' + (tersaid(n%1000) if n%1000!=0 else '')
    elif n>=100:
        return tersaid(n//100) + ' hundred ' + (tersaid(n%100) if n%100!=0 else '')
    elif n>=90:
        return 'ninety ' + (tersaid(n%10) if n%10!=0 else '')
    elif n>=80:
        return 'eighty ' + (tersaid(n%10) if n%10!=0 else '')
    elif n>=70:
        return 'seventy ' + (tersaid(n%10) if n%10!=0 else '')
    elif n>=60:
        return 'sixty ' + (tersaid(n%10) if n%10!=0 else '')
    elif n>=50:
        return 'fifty ' + (tersaid(n%10) if n%10!=0 else '')
    elif n>=40:
        return 'forty ' + (tersaid(n%10) if n%10!=0 else '')
    elif n>=30:
        return 'thirty ' + (tersaid(n%10) if n%10!=0 else '')
    elif n>=20:
        return 'twenty ' + (tersaid(n%10) if n%10!=0 else '') 

while True:
    os.system('cls')
    try:
        print('[0] = Exit')
        pil = int(input('Bahasa Indonesia [1] / English [2] ? '))
    except Exception as e:
        print('Input invalid...')
    else:
        if pil == 1:
            os.system('cls')
            try:
                n = input('Input Angka ? ')
                koma=False
                for char in n:
                    if char=='.':
                        koma=True   
                bilangan=int(n[0:n.find('.')])
                des=n[n.find('.')+1: ]
                listdes=[i for i in des]
            except Exception as e:
                print('Error', e)
            else:
                if koma==False:
                    n=int(n)          
                    print(f'{n:,} = {terbilang(n)}')
                else:
                    print(f'{bilangan:,}.{des} = {terbilang(bilangan)} koma',end=' ')
                    for i in listdes:
                        print(terbilang(int(i)), end=' ')
                    print()

        elif pil == 2:
            os.system('cls')
            try:
                n=input('Enter a Number : ')
                coma=False
                for char in n:
                    if char=='.':
                        coma=True   
                bilangan=int(n[0:n.find('.')])
                des=n[n.find('.')+1: ]
                listdes=[i for i in des]
            except Exception as e:
                print('Error :',e)
            else:
                if coma == False:
                    n = int(n)
                    print(f'{(n):,} = {tersaid(n)}')
                else:
                    print(f'{bilangan:,}.{des} = {tersaid(bilangan)} point', end= ' ')
                    for i in listdes:
                        print(tersaid(int(i)), end=' ')
                    print()

        elif pil == 0:
            break
    finally:
        print()
        os.system('pause')