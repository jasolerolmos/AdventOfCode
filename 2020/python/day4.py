from time import time
import re

start_time = time()
sol = 0
def AnalizarPassport(cadena):
    passportInvalido = False
    nombreCampos = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    hairColor = re.compile('#[0-9a-f]{6}')  # # -> six characters 0-9 or a-f.
    pid = re.compile('[0-9]{9}')  # # -> six characters 0-9 or a-f.
    datos = cadena.split(' ')
    temp = []
    sol = 1;sol2 = 0;
    
    #print('',cadena)
    for campo in datos:
        analisis = campo.split(':')
        temp.append(analisis[0])
        if analisis[0] == 'byr':
            if not (len(analisis[1])==4 and int(analisis[1]) >= 1920 and int(analisis[1]) <= 2002):
                return 0
        if analisis[0] == 'iyr':
            if not (len(analisis[1])==4 and int(analisis[1]) >= 2010 and int(analisis[1]) <= 2020):
                #print('\t\t\t\t\t\t\tiyr',analisis[1],' Issue Year KO.')
                return 0
        if analisis[0] == 'eyr':
            if not (len(analisis[1])==4 and int(analisis[1]) >= 2020 and int(analisis[1]) <= 2030):
                return 0
        
        if analisis[0] == 'hgt':
            if analisis[1].endswith('cm'):
                aux = analisis[1].replace('cm','')
                if not (int(aux)>=150 and int(aux)<=193):
                    return 0
            else:
                if analisis[1].endswith('in'):
                    aux = analisis[1].replace('in','')
                    if not (int(aux)>=59 and int(aux)<=76):
                        return 0
                else:
                    return 0
        
        if analisis[0] == 'hcl':    
            if not hairColor.match(analisis[1]):
                return 0
        
        if analisis[0] == 'ecl':
            eyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if not analisis[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return 0
        
        if analisis[0] == 'pid':
            if not pid.match(analisis[1]) or len(analisis[1]) != 9:
                return 0
                    
    for nc in nombreCampos:
        sol2 = sol2 + temp.count(nc)
        sol = sol * temp.count(nc)

    return sol

f = open("day4Input.txt", "r")
#f = open("ejemplo.txt", "r")

passport = ""
total=0
for linea in f:
    linea = linea.replace('\n', '')
    if(len(linea)>0):
        passport = passport + linea + ' '
    else:
        total = total + 1
        passport = passport.strip()
        resultado = AnalizarPassport(passport)
        sol = sol + resultado
        passport = ''

f.close();

print("Solución",sol,'de',total)
print("Elapsed time: %0.10f seconds." % (time() - start_time))