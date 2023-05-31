from googletrans import Translator
tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)



while 1:
    matn_uz = input("tarjima qilmoqchi bolgan gapni kirgazing: \n >>>")
    til=input("Qaysi tildagi tarjimasi krk (ru/eng/uz)")
    while 1:    
        if til=="ru":
            tarjima_ru = tarjimon.translate(matn_uz,dest="ru")
            print(tarjima_ru.text,"\n")
            break
        elif til=="eng":
            tarjima_eng = tarjimon.translate(matn_uz)
            print(tarjima_eng.text,"\n")
            break
        elif til=="uz":
            tarjima_uz = tarjimon.translate(matn_uz,dest="uz")
            print(tarjima_uz.text,"\n")
            break
        else:
            print(f"Siz til tanlashda Xato qildingiz!\n Qaysi tilga otkazmoqchisiz qaytadan kirgazing (ru/eng/uz)\n>>>")