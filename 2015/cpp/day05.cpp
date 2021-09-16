#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <time.h>

using namespace std;


vector<string> readFileString() {
    vector<string> lineas;
    fstream newfile;
    newfile.open("../input/input05.txt",ios::in);
    if (newfile.is_open()){
        string tp;
        while(getline(newfile, tp)){
            lineas.push_back(tp);
        }
        newfile.close();
    }

    return lineas;
}

bool prohibidas(string cad){
    bool valida = true;
    vector<string> prohibidas{"ab", "cd", "pq", "xy"};
    int i=0;
    while(valida && i<prohibidas.size()){
        if (cad.find(prohibidas[i]) != string::npos)
            valida = false;
        i++;
    }
    
    return valida;
}

bool repeatChar(string cad){
    bool valido = false;
    int i=0;
    while(!valido && i<cad.size()-2){
        string pareja = cad.substr(i, 2);
        string resto = cad .substr(i+2);
        
        if (resto.find(pareja) != string::npos){
            valido = true;
        }
        i++;
    }

    return valido;
}

bool doubleCharWithSeparator(string cad){
    bool valido = false;
    int i=0;
    while(!valido && i<cad.size()-2){
        if (cad[i] == cad[i+2]) {
            valido = true;
        }
        i++;
    }

    return valido;
}


bool doubleChar(string cad){
    bool valido = false;
    int i=0;
    while(!valido && i<cad.size()-1){
        if (cad[i] == cad[i+1]) {
            valido = true;
        }
        i++;
    }

    return valido;
}

bool findVocales(string cad){
    int numVocales = 0;
    char vocales[] = {'a', 'e', 'i', 'o' , 'u'};
    for(int i=0; i<strlen(vocales); i++)
        numVocales += count(cad.begin(), cad.end(), vocales[i]);
        if (numVocales >= 3)
            return true;

    return false;
}

int part1(vector<string> lineas) {
    int validos = 0;
    for(int i=0; i<lineas.size(); i++){
        if (prohibidas(lineas[i]) && findVocales(lineas[i]) && doubleChar(lineas[i])){
            validos++;
        }
    }
    return validos;
}


int part2(vector<string> lineas) {
    int validos = 0;
    for(int i=0; i<lineas.size(); i++){
        if (doubleCharWithSeparator(lineas[i]) && repeatChar(lineas[i])){
            validos++;
        }
        
    }
    return validos;
}

int main () 
{   
    vector<string> lineas = readFileString();
    cout << "\nPart 1, Solución: " << endl;

    clock_t tStart = clock();
    int solucion = part1(lineas);
    cout << "\t" << to_string(solucion) << endl;
    printf("Time: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);

    cout << "\nPart 2, Solución: " << endl;

    tStart = clock();
    solucion = part2(lineas);
    cout << "\t" << to_string(solucion) << endl;
    printf("Time: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
}