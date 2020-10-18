'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SUN_GRAVITY = 274
MARS_GRAVITY = 3.711
MERKUR_GRAVITY = 3.7
URAN_GRAVITY = 8.87
VENUS_GRAVITY = 8.87
SATURN_GRAVITY = 10.44
NEPTUN_GRAVITY = 11.15
JUPITER_GRAVITY = 24.79
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu v m/s
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu v m/s

GRAVITIES = [
    ("Jupiter", JUPITER_GRAVITY),
    ("Země", EARTH_GRAVITY),
    ("Saturn", SATURN_GRAVITY),
    ("Merkur", MERKUR_GRAVITY),
    ("Venuše", VENUS_GRAVITY),
    ("Slunce", SUN_GRAVITY),
    ("Měsíc", MOON_GRAVITY),
    ("Mars", MARS_GRAVITY),
    ("Neptun", NEPTUN_GRAVITY),
    ("Uran", URAN_GRAVITY),
]

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def height(g1, g2, v):
    '''
    Tato funkce spočítá a vypíše, jak moc vás bude bolet pád na planetě v porovnání s pádem na jiné planetě
    '''
    if g1[0] == "Slunce":
        print(f"Když na Slunci spadnete z výšky {v} metrů, bude vás to bolet, jako kdybyste na planetě {g2[0]} spadli z {g1[1] * v / g2[1]} metrů... A budete u toho hořet")
    elif g1[0] == "Měsíc":
        print(f"Když na Měsíci spadnete z výšky {v} metrů, bude vás to bolet, jako kdybyste na planetě {g2[0]} spadli z {g1[1] * v / g2[1]} metrů... A budete u toho hořet")
    else:
        print(f"Když na planetě {g1[0]} spadnete z výšky {v} metrů, bude vás to bolet, jako kdybyste na planetě {g2[0]} spadli z {g1[1] * v / g2[1]} metrů.")


