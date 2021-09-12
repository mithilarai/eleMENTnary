import csv
from collections import Counter

start_up = print('This program will easily  give out the details about any element present in currect periodic table')
print('')

with open('chem_elements.csv' , newline = '') as f : 
    reader = csv.reader(f)
    list_data = list(reader)
position =''
new_data = []
result = True
while(result) : 
    element_name = input('Enter the element (Name/Symbol/Atomic No.) [any 1]: ')
    for i in range(len(list_data)) : 
        Element_No = list_data[i][0]
        Element_Symbol = list_data[i][2]
        Element = list_data[i][1]
        if (Element == element_name or Element_No == element_name or Element_Symbol == element_name) : 
            position = list_data[i]
        else:
            result=False
        
    if(position != ""):
        not_found = []
        print('')
        if(position[0] != '') :
            print(f'    Atomic Number : {position[0]}')
        else  : 
            not_found.append('Atomic No.') 

        if(position[1] != '') :
            print(f'    Element : {position[1]}')
        else : 
            not_found.append('Element') 

        if(position[2] != '') :
            print(f'    Symbol : {position[2]}')
        else : 
            not_found.append('Symbol') 

        if(position[3] != '') :
            print(f'    Atomic Mass : {position[3]} u ')
        else : 
            not_found.append('Atomic Mass') 

        if(position[3] != '') :
            print(f'    Molar Mass : {position[3]} g/mL ')
        else : 
            not_found.append('Molar Mass') 

        if(position[23] != '') : 
            print(f'    Discoverer : {position[23]}')
        else : 
            not_found.append('Discover') 

        if(position[24] != '') :
            print(f'    Year : {position[24]}')
        else : 
            not_found.append('Year') 

        if(position[15] != '') :
            print(f'    Type : {position[15]}')
        else : 
            not_found.append('Type') 

        print('')
        if(position[4] != '') :
            print(f'    No. Of Neutrons : {position[4]}')
        else : 
            not_found.append('No. Of Neutrons') 

        if(position[5] != '') :
            print(f'    No. Of Protons : {position[5]}')
        else : 
            not_found.append('No. Of Protons') 

        if(position[6] != '') :
            print(f'    No. Of Electrons : {position[6]}')
        else : 
            not_found.append('No. Of Electrons') 

        if(position[26] != '') :
            print(f'    No. Of Shells : {position[26]}')
        else : 
            not_found.append('No. Of Shells') 

        if(position[27] != '') : 
            print(f'    No. of Valence Electrons: {position[27]}')
        else : 
            not_found.append('No of Valence Electrons') 

        print('')
        if(position[7] != '') :
            print(f'    Period : {position[7]}')
        else : 
            not_found.append('Period') 

        if(position[8] != '') :
            print(f'    Group : {position[8]}')
        else : 
            not_found.append('Group') 

        if(position[9] != '') :
            print(f'    Phase : {position[9]}')
        else : 
            not_found.append('Phase') 

        if(position[19] != '') : 
            print(f'    Density : {position[19]}')
        else : 
            not_found.append('Density') 

        if(position[20] != '') : 
            print(f'    Melting Point : {position[20]}')
        else : 
            not_found.append('Melting Point') 

        if(position[21] != '') : 
            print(f'    Boiling Point : {position[21]}')
        else : 
            not_found.append('Boiling Point') 

        print('')
        if(position[16] != '') : 
            print(f'    Atomic Radius : {position[16]}')
        else : 
            not_found.append('Atomic Radius') 

        if(position[17] != '') : 
            print(f'    Electronegativity : {position[17]}')
        else : 
            not_found.append('Electronegativity') 

        if(position[22] != '') : 
            print(f'    No. Of Isotopes : {position[22]}')
        else : 
            not_found.append('No. Of Isotopes') 

        print('')

        if(len(not_found) != 0) : 
            print(f'Some details like {not_found} are not available :(   Sorry for the inconvenience')
            print('')

    else:
        print("Element does not exist")

    mood = input('Wanna Continue (y/n) : ')
    print('')

    if(mood == 'n' or mood == 'N') : 
        result = False
        print('Thanks for using this application :)')
        print('')
        print('')

    else : 
        result = True
        

        
    # Electron Affinity
    # Ionization anthalpy
