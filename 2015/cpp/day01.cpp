#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;


vector<string> readFileString() {
    
    ifstream file("../input/input01.txt");
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

int part2(vector<string> lineas){
    int piso = 0;
    for(int n = 0; n < lineas[0].length(); n++){
        if (lineas[0][n] == '(') 
            piso++;
        else
            piso--;
        if (piso == -1)
            return n+1;
    }

    return 0;
}


int part1(vector<string> lineas){
    int up = count(lineas[0].begin(), lineas[0].end(), '(');
    int down = count(lineas[0].begin(), lineas[0].end(), ')');
    
    return up-down;
}

int main () 
{   
    vector<string> lineas = readFileString();
    cout << "Part 1, Solución: " << part1(lineas) << endl;
    cout << "Part 2, Solución: " << part2(lineas) << endl;
    return 0;
}