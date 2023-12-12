aboli = float(input('Cik daudz kg  ābolu? :')) 
cukura_cena = 0
udens_cena = 0
citrona_cena = 0
mandelu_cena = 0
kanela_cena = 0

if aboli < 3.0 :
    v_cukurs = 1-(((3-aboli)/3)*1)
    v_udens = 500-(((3-aboli)/3)*500)
    v_citrons = 1-(((3-aboli)/3)*1)
    v_mandelu = 5-(((3-aboli)/3)*5)
    v_kanelis = 10-(((3-aboli)/3)*10)
    print('nepiciešams',round(v_cukurs,2),'kg cukurs')
    print('nepiciešams',round(v_udens,2),'ml ūdens')
    print('nepiciešams',round(v_citrons,2),'gab citrona')
    print('nepiciešams',round(v_mandelu,2),'ml mandeļu ekstrakta')
    print('nepiciešams',round(v_kanelis,2),'g kanēļa')
elif aboli == 3:
    v_cukurs = 1
    v_udens = 500
    v_citrons = 1
    v_mandelu = 5
    v_kanelis = 10
elif aboli >3:
    v_cukurs = (((aboli-3)/3)*1)+1
    v_udens = (((aboli-3)/3)*500)+500
    v_citrons = (((aboli-3)/3)*1)+1
    v_mandelu = (((aboli-3)/3)*5)+5
    v_kanelis = (((aboli-3)/3)*10)+10
    print('nepiciešams',round(v_cukurs,2),'kg cukurs')
    print('nepiciešams',round(v_udens,2),'ml ūdens')
    print('nepiciešams',round(v_citrons,2),'gab citrona')
    print('nepiciešams',round(v_mandelu,2),'ml mandeļu ekstrakta')
    print('nepiciešams',round(v_kanelis,2),'g kanēļa')

cukurs = input('Vai jums ir nepieciešams vēl cukura?(j/n)')
if cukurs == 'j':
    papildus_cukurs= input('Cik vēl cukurs jums nepieciešams?')
    if papildus_cukurs <= 1:
        cukura_cena==1.35
        if papildus_cukurs > 1:
            cukura_cena == 2.70
            if papildus_cukurs >= 2:
                cukura_cena == 4.05

citrons = input('Vai jums ir nepieciešams vēl cukura?(j/n)')
if citrons == 'j':
    papildus_citrons= input('Cik vēl cukurs jums nepieciešams?')
    if papildus_citrons <= 1:
        citrona_cena==1.01
        if papildus_citrons > 1:
            citrona_cena == 2.02
            if papildus_citrons >= 2:
                citrona_cena == 3.03
