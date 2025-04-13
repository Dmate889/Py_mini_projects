import random

fantasy_names = [
    "Aelandan", "Aelanthas", "Aeldorthus", "Aelethrak", "Aelilriel", "Aeliris", "Aelirnos", "Aelmirgorn", "Aelorvek", "Aelorith",
    "Aelthas", "Aelvak", "Aelynor", "Brynian", "Bryniriel", "Brynnos", "Brynthas", "Druaelzor", "Drudan", "Drudorvek",
    "Drugarion", "Drukarnax", "Drunax", "Drurak", "Druthal", "Druvek", "Druwyn", "Elanmir", "Elandrak", "Elanthus",
    "Elarion", "Elilkar", "Elmirvek", "Eloril", "Elornax", "Elroskar", "Elsylrak", "Elthus", "Elvak", "Elwyn",
    "Fendrak", "Fenmir", "Fenwyn", "Kaelgorn", "Kaelkarnax", "Kaelmir", "Kaelriel", "Kaelvak", "Kaelwyn", "Kaethas",
    "Keldan", "Kelgorn", "Kelkar", "Kelnax", "Kelwyn", "Lyrdan", "Lyrelrak", "Lyricion", "Lyrkar", "Lyrmir",
    "Maldrak", "Maleth", "Malion", "Malnos", "Malros", "Malvak", "Malthas", "Malyndor", "Morakar", "Moriel",
    "Morilkar", "Morion", "Mornax", "Morthal", "Morvak", "Moryn", "Ravak", "Ravdan", "Ravkar", "Ravmir",
    "Ravnax", "Ravnos", "Ravriel", "Ravwyn", "Shaelkar", "Shaelnos", "Shaelrak", "Shaelwyn", "Shaethas", "Shaion",
    "Shakar", "Shariel", "Shavos", "Shaxor", "Sylador", "Sylarion", "Sylkar", "Sylmir", "Sylrak", "Sylwyn",
    "Thalakar", "Thaldan", "Thalgorn", "Thalmir", "Thalor", "Thalos", "Thalrak", "Thalwyn", "Torak", "Tordras",
    "Torgorn", "Torilkar", "Torion", "Torkar", "Tornax", "Torwyn", "Tyrdan", "Tyriel", "Tyrion", "Tyrkar",
    "Tyrnax", "Tyrros", "Tyrvak", "Tyrwyn", "Vordan", "Vorgorn", "Vorkar", "Vornax", "Vorthal", "Vorvak",
    "Xanakar", "Xandrak", "Xaniel", "Xankarnax", "Xannos", "Xanrak", "Xanthas", "Xanvek", "Xanwyn", "Zarakar",
    "Zardrak", "Zariel", "Zarion", "Zarkar", "Zarnax", "Zarros", "Zarthal", "Zarthus", "Zarvak", "Zarwyn"
]

def randomize():
    name = random.choice(fantasy_names)
    return name
