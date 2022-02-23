def ortalama_hesaplama() :
    ort=input('Universiteliysen : 1  , Liseliysen:  2  ')
    if ort==1:
        vize=input('Vize Notunuzu Girin  :  ')
        final=input('Final Notunuzu Girin  :  ')
        ortalama=(float(vize)*0.4) + (float(final)*0.6)
        print("Ortalmaniz :{0} ").format(ortalama)
    elif ort==2:
        y1=input('Ilk Yazili Notunuzu Girin  :  ')
        y2=input('Ikinci Yazili Notunuzu Girin  :  ')
        ortalam=(int(y1) + int(y2)) /2
        print("Ortalamaniz : {0}").format(ortalam)
print(ortalama_hesaplama())