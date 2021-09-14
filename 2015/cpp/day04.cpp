    #include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <openssl/md5.h>
using namespace std;

unsigned char *MD5(const unsigned char *d, 
                   unsigned long n,
                   unsigned char *md);

vector<string> readFileString() {
    ifstream file("../input/test04.txt");
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

void MD5Hexa(string cad) {
    char buffer [50];
    cout << "Cad: " << "1 " << endl;
    
    printf("Cadena %s %i\n", cad, cad.length());

    unsigned char * solucion = new unsigned char[32]();;
    unsigned char * aux1 =  new unsigned char[20]();
    strcpy((char *) aux1, (char *)cad.c_str());
    
    cout << "2 " << aux1 << endl;
    printf("Copiado %s %i\n", aux1, strlen((char*)aux1));
    
    MD5(aux1, strlen((char*)aux1), solucion);
    
    cout << "3 " << endl;
    
    for(int i=0; i <strlen((char*)solucion); i++){
        sprintf(buffer, "%02x",  solucion[i]);
    }
    printf("%s", buffer);

    cout << "4 " << endl;
}

int part1(vector<string> lineas){
    int suma = 0;
    bool found = false;
    cout << "Part 1" << endl;
    int num = 0;

    unsigned char * solucion =  new unsigned char[32]();;
    
    MD5Hexa("abcdef");

    while(!found){
        ostringstream oss;
        oss << lineas[0] << num;
        string hashMD5 = oss.str();
        unsigned char* m_Test =  new unsigned char[6]();

        strcpy( (char*) m_Test, hashMD5.c_str());
        
        cout << "MD5: " << m_Test << endl;
        MD5(m_Test, 6, solucion);
        for(int i=0; i <strlen((char*) solucion); i++){
            printf("%02x",  solucion[i]);
        }
        
        if (hashMD5.substr(0,5) == "00000"){
            cout << "Encontrado: " << num << endl;
            found = true;
        }
        num ++;
        found = true;
    }
    return num;
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
    char src[] = "abcdef";
    MD5Hexa("abcdef");

    int solucion = part1(lineas);
    cout << "Part 1, Solución: " << solucion << endl;
    //solucion = part2(lineas);
    //cout << "Part 2, Solución: " << solucion << endl;
    return 0;
}