#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

vector<string> readFileString() {
    ifstream file("../input/input03.txt");
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


int part1(vector<string> lineas){
    int suma = 0;
    int ejeY = 0;
    int ejeX = 0;

    vector<string> casa;
    casa.push_back((ejeX + " " + ejeY));
    for(int n = 0; n < lineas[0].size(); n++){
        switch (lineas[0][n]){
            case '^':
                ejeY += 1;
                break;
            case 'v':
                ejeY -= 1;
                break;
            case '<':
                ejeX -= 1;
                break;
            case '>':
                ejeX += 1;
                break;
            default:
                break;
        }
        
        string locCasa = printf(ejeX+ " " + ejeY;

        if (find(casa.begin(), casa.end(), locCasa) != casa.end()){
            cout << "Repetido: " << locCasa << endl;
        }
        else {
            casa.push_back(locCasa);
            cout << locCasa << endl;
        }
    }
    return casa.size();
}

int part2(vector<string> lineas){
    int suma = 0;

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