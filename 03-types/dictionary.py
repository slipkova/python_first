'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Kolekcce, která je neuspořádaná, měnitelná a indexovaná.
# V pythonu se dictionaries píšou ve složených závorkách a mají klíče a hodnoty

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1': {
    'name': 'Emil',
    'year': 2004
  },
  'child2': {
    'name': 'Tobias',
    'year': 2007
  },
  'child3': {
    'name': 'Linus',
    'year': 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''
s = {
    "bb": "Bluebull",
    "gc": "Good Car",
    "bv": "Bee vomit",
    "sb": "Sleeping beauty"
}



sportsman = {
  "s1": {
    "last name": "Dalon",
    "name": "Arnold",
    "birth": "1856",
    "sport": "Spinach breeding",
    "dress": {"blue and white", "blue"},
    "last two competitions": ["World championship", "Lax le por"],
    "sponsors": (s["bb"], s["gc"])
  },


  "s2": {
      "last name": "Xae",
      "name": "Max",
      "birth": "1996",
      "sport": "3D chess",
      "dress": {"red", "red and black"},
      "last two competitions": ["The best one", "Tour de check"],
      "sponsors": (s["bb"], s["bv"])
  },

  "s3": {
      "last name": "Larson",
      "name": "Bree",
      "birth": "1967",
      "sport": "Speeed eating",
      "dress": {"Hamburger costume"},
      "last two competitions": ["The biggest spinach", "Ripping belly"],
      "sponsors": (s["bb"], s["gc"])
  }
}

del sportsman["s2"]

sportsman["s4"] = {
      "last name": "De Louvre",
      "name": "Agnes",
      "birth": "1694",
      "sport": "Couching",
      "dress": {"blue pyjamas", "red uderwear"},
      "last two competitions": ["Are you dead?", "Extreme loafers"],
      "sponsors": (s["sb"], s["gc"])
  }

sportsman["s5"] = {
      "last name": "Xae",
      "name": "Max",
      "birth": "1996",
      "sport": "3D chess",
      "dress": {"red", "red and black"},
      "last two competitions": ["The best one", "Tour de check"],
      "sponsors": (s["bb"], s["bv"])
  }

print("-----------------------------")
print("Sportsmen of Zuanne")
print("-----------------------------")
print("Name      Last name      Year of birth     Sport               Dress                         Last two competitions                   Sponsors")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
for i in sportsman:
    x = ""
    x += sportsman[i]["name"].ljust(10)
    x += sportsman[i]["last name"].ljust(15)
    x += sportsman[i]["birth"].ljust(18)
    x += sportsman[i]["sport"].ljust(20)
    x += "".join([i + ', ' for i in sportsman[i]["dress"]])[:-2].ljust(30)
    x += "".join([i + ', ' for i in sportsman[i]["last two competitions"]])[:-2].ljust(40)
    x += "".join([i + ', ' for i in sportsman[i]["sponsors"]])[:-2].ljust(40)
    print(x)

