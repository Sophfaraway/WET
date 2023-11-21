
def main():
    bludistaci = {
    "Jakub":3,
    "Vašek":2,
    "Ema":2
    }
    jmeno = input("Napiš jméno ").capitalize() #převede 1. písmenko na velké
    #lower - všechna na malá
    #upper - všechna na velká písmenka
    kolik_bludistaku(bludistaci, jmeno)
#hl. funkce - začátek programu
#pass - pro prázdné funkce 
#print(bludistaci["Vašek"])

def kolik_bludistaku(seznam, jmeno):
    
    if jmeno in seznam:
        print(seznam[jmeno])
    #abstrakce = usnadnění
    #print(bludistaci[jmeno])

def pridej_studenta(seznam, jmeno):
    seznam[jmeno] = 1

#pridej_studenta(bludistaci)
#print(bludistaci)

if __name__=="__main__": #always needs to be here - spouští pouze pokud to je hl. program
    main()