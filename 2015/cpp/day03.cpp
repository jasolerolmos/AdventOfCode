#include <iostream>
#include <sstream>
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
        
        ostringstream oss;
        oss << ejeX << " " << ejeY;
        string locCasa = oss.str();

        if (find(casa.begin(), casa.end(), locCasa) == casa.end()){
            casa.push_back(locCasa);
        }
    }
    return casa.size();
}

int part2(vector<string> lineas){
    int suma = 0;
    int ejes[] = {0,0};
    int santa[] = {0,0};
    int robot[] = {0,0};

    vector<string> casa;
    
    ostringstream oss;
    oss << ejes[0] << " " << ejes[1];
    string locCasa = oss.str();

    casa.push_back(locCasa);
    for(int n = 0; n < lineas[0].size(); n++){
        oss.str("");
        oss.clear();
        if (n % 2 == 0){
            ejes[0] = santa[0];
            ejes[1] = santa[1];
        } else {
            ejes[0] = robot[0];
            ejes[1] = robot[1];
        }

        switch (lineas[0][n]){
            case '^':
                ejes[0] += 1;
                break;
            case 'v':
                ejes[0] -= 1;
                break;
            case '<':
                ejes[1] -= 1;
                break;
            case '>':
                ejes[1] += 1;
                break;
            default:
                break;
        }
        
        oss << ejes[0] << " " << ejes[1];
        locCasa = oss.str();

        if (find(casa.begin(), casa.end(), locCasa) == casa.end()){
            casa.push_back(locCasa);
        }

        if (n % 2 == 0){
            santa[0] = ejes[0];
            santa[1] = ejes[1];
        } else {
            robot[0] = ejes[0];
            robot[1] = ejes[1];
        }
    }
    return casa.size();
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