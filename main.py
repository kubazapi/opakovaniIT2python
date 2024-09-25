jmeno = "Jakub"                 # Vytvořte proměnnou, do které vložíte své jméno.
prijmeni = "Zapletal"           # Vytvořte proměnnou, do které vložíte své příjmení.
print(jmeno + " " + prijmeni)                    # Vypište tyto dvě proměnné do konzole.

vek = int(input("Váš věk (pouze číslo):"))   # Vytvořte vstup pro uživatele, který bude moct zadat pouze věk (nikoli své jméno nebo jinou stringovou hodnotu).
if vek < 0:
    print("Nesprávná hodnota.")

print("Počet písmen ve vašem jméně:", len(jmeno))               # Vypište v konzoli délku první proměnné a druhé proměnné.
print("Počet písmen ve vašem příjmení:", len(prijmeni))

cislo = 6                      # Vytvořte proměnnou, do které uložíte hodnotu 6.
                   
for _ in range(5):             # Vytvořte cyklus, který bude mít 5 opakování a při každém opakování se přičte hodnota 3.
    cislo += 3  
print("Výsledná hodnota po pěti cyklech:", cislo)                   # Vypište v konzoli výslednou hodnotu po 5 cyklech.



vek = int(input("Zadejte svůj věk: "))        # Vytvořte podmínku pro uživatele, který zadá věk - 1. Pokud zadá jen celočíselnou hodnotu program odpoví "Děkuji". 2. Pokud zadá jakoukoli jinou hodnotu program odpoví "Zadej jen celočíselnou hodnotu." 
if vek >= 0:
    print("Děkuji")
else:
    print("Zadej jen celočíselnou hodnotu.")
     
    
import random                                # Vytvořte proměnnou, do které uloží program náhodnou hodnotu od 1-10 a vypište ji do konzole.

nahodne_cislo = random.randint(1, 10)

print("Náhodné číslo:", nahodne_cislo)

