# Zkus si trochu pohrát s formátováním stringů a s přesností.
# Jaký způsob formátování si vybereš je zcela na tobě.
# Program bude obsahovat tyto kroky:
#
# Na začátek souboru zapiš tyto proměnné presnost_cisla s hodnotou celého čísla 123.4567,
# proměnnou kombinace s hodnotou celého čísla 1.234,
# proměnnou presnost_str s hodnotou stringu "Hello",
# potom použij proměnnou formatovana_presnost, kam naformátuješ hodnotu v presnost_cisla tak,
# aby výstup vypadal: |1.23e+02|123.5|123.46|,
# dále zapiš proměnnou formatovana_kombinace, kam naformátuješ hodnotu v kombinace, aby výstup vypadal: |1.234$|,
# nakonec zapiš proměnnou formatovana_presnost_str, kam naformátuješ hodnotu v presnost_str, aby výstup vypadal: |Hell|,
# vše v závěru vypiš pomocí funkce print.

# Ukázka průběhu:
# Naformátovaná přesnost: |1.23e+02|123.5|123.46|,
# Naformátovaná kombinace: |1.234$|,
# Naformátovaný string: |Hell|.

p = 'p'
presnost_cisla = 123.4567
kombinace = 1.234
presnost_str = 'Hello'

def formatovana_presnost(cislo):
    """Formatoje cislo tak aby vystup vypadal nasledovne: |1.23e+02|123.5|123.46|"""
    presnost_2 = round(cislo, 2)
    presnost_1 = round(cislo, 1)
    scientific_notation = "{:.2e}".format(cislo)
    # presnost.append(scientific_notation)
    # presnost.append(presnost_1)
    # presnost.append(presnost_2)


    #print(f'presnost je {presnost}')

    return scientific_notation, presnost_1, presnost_2



def formatovana_kombinace(cislo):
    """Formatoje cislo tak aby vystup vypadal nasledovne: |1.234$|"""
    return '{0}{1}'.format(cislo, '$')



def formatovana_presnost_str(retezec: str):
    """Formatoje retezec tak aby vystup vypadal nasledovne: |Hell|"""
    return retezec[0:4]



print(f'Naformatovana presnost: |{formatovana_presnost(presnost_cisla)}|')
print(f'Naformatovana kombinace: |{formatovana_kombinace(kombinace)}|')
print(f'Naformatovany string: |{formatovana_presnost_str(presnost_str)}|.')
