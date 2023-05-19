class Magaza:

    def __init__(self, magaza_adi, satici_adi, satilan_urun, urun_fiyati, tutar=0):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satilan_urun = satilan_urun
        self.__urun_fiyati = urun_fiyati
        self.__tutar = tutar

    def ara_deger(self, magaza_adi, satici_adi, satilan_urun, urun_fiyati):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satilan_urun = satilan_urun
        self.__urun_fiyati = urun_fiyati

    def magaza_satis_tutar(self, kutuphane):
        self.__tutar = kutuphane["Ürünün tutarı"]
        for key, value in kutuphane.items():
            print(key,value)

    def __str__(self):
        return "{} mağazasında çalışan {} isimli çalışanın satış " \
               "tutarı={}".format(self.__magaza_adi, self.__satici_adi, self.__tutar)


def main():
    secim = int(input("Kaç kere veri gireceksiniz."))
    magaza_list = []
    for count in range(secim):
        magazanin_adi = str(input("Mağaza adı gir"))
        saticinin_adi = str(input("Satıcının adını gir"))
        satilmis_urun = str(input("Satılmış ürünü gir"))
        urun_tutar = float(input("Satılmış ürünün tutarı"))
        veri_kutuphane = {"Mağaza adı": magazanin_adi, "Satıcının adı": saticinin_adi, "Satılmış ürün": satilmis_urun,
                          "Ürünün tutarı": urun_tutar}
        magaza_obje = Magaza(magazanin_adi, saticinin_adi, satilmis_urun, urun_tutar)
        magaza_obje.ara_deger(magazanin_adi, saticinin_adi, satilmis_urun, urun_tutar)
        magaza_obje.magaza_satis_tutar(veri_kutuphane)
        print(magaza_obje)


main()
