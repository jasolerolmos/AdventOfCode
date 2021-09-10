#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

vector<string> readFileString() {
    ifstream file("../input/input02.txt");
    string str;
    vector<string> lineas;

    while (getline(file, str)) {
        if(str.size() > 0){
            lineas.push_back(str+'\0');
        }
    }
    file.close();

    return lineas;
}

vector<int> splitStr(string s, string del = " ")
{
    vector<int> split;
    int start = 0;
    int end = s.find(del);
    while (end != -1) {
        split.push_back(atoi(s.substr(start, end - start).c_str()));
        start = end + del.size();
        end = s.find(del, start);
    }
    split.push_back(atoi(s.substr(start, end - start).c_str()));
    return split;
}

int minArea(vector<int> lados) {
    int minimo = lados[0] * lados[1];
    if ( (lados[0] * lados[2]) < minimo){
        minimo = lados[0] * lados[2];
    } else {
        if ((lados[1] * lados[2]) < minimo){
            minimo = lados[1] * lados[2];
        }
    }
    return minimo;
}

int papelNecesario(vector<int> lados) {
    return ((lados[0] * lados[1]) * 2
        + (lados[0] * lados[2]) * 2
        + (lados[1] * lados[2]) * 2
        + minArea(lados));
}


int part1(vector<string> lineas){
    int suma = 0;

    for(int n = 0; n < lineas.size(); n++){
        vector<string> medidas;
        string regalo = lineas[n];
        vector<int> lados = splitStr(regalo, "x");
        sort(lados.begin(), lados.end());
        
        suma += papelNecesario(lados);
    }
    return suma;
}

int part2(vector<string> lineas){
    int suma = 0;

    for(int n = 0; n < lineas.size(); n++){
        vector<string> medidas;
        string regalo = lineas[n];
        vector<int> lados = splitStr(regalo, "x");
        sort(lados.begin(), lados.end());
        suma += (lados[0]*2 + lados[1]*2) + (lados[0] * lados[1] * lados[2]);
    }
    return suma;
}

int main () 
{   
    vector<string> lineas = readFileString();
    int solucion = part1(lineas);
    cout << "Part 1, Solución: " << solucion << endl;
    solucion = part2(lineas);
    cout << "Part 2, Solución: " << solucion << endl;
    return 0;
}