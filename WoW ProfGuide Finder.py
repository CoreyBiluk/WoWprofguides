## This program askes the user which World of Warcraft profession guide they
## would like to find and then opens the link for them in the browser.

import webbrowser as wb

# URLs
herb = 'https://www.wow-professions.com/guides/wow-herbalism-leveling-guide'
mining = 'https://www.wow-professions.com/guides/wow-mining-leveling-guide'
skin = 'https://www.wow-professions.com/guides/wow-skinning-leveling-guide'
alch = 'https://www.wow-professions.com/guides/wow-alchemy-leveling-guide'
smith = 'https://www.wow-professions.com/guides/wow-blacksmithing-leveling-guide'
chant = 'https://www.wow-professions.com/guides/wow-enchanting-leveling-guide'
eng = 'https://www.wow-professions.com/guides/wow-engineering-leveling-guide'
leather = 'https://www.wow-professions.com/guides/wow-leatherworking-leveling-guide'
tailor = 'https://www.wow-professions.com/guides/wow-tailoring-leveling-guide'

def find ():
    
    run = True
    
    while run:
        print("Welcome to the WoW Profession Guide Finder v1.0\n")
        print("Choose which guide to find:\n")
        print("[1]Herbalism [2]Mining [3]Skinning\n")
        print("[4]Alchemy [5]Blacksmithing [6]Enchanting\n")
        prof_choice = input("[7]Engineering [8]Leatherworking [9]Tailoring\n")
        
        if prof_choice == '1':
            wb.open_new(herb)
        if prof_choice == '2':
            wb.open_new(mining)
        if prof_choice == '3':
            wb.open_new(skin)
        if prof_choice == '4':
            wb.open_new(alch)
        if prof_choice == '5':
            wb.open_new(smith)
        if prof_choice == '6':
            wb.open_new(chant)
        if prof_choice == '7':
            wb.open_new(eng)
        if prof_choice == '8':
            wb.open_new(leather)
        if prof_choice == '9':
            wb.open_new(tailor)
        
        quit_val = input("Find another guide? Y/N?\n")
        
        if quit_val.upper() == 'N':
            run = False
            
        
if __name__ == '__main__':
    find()