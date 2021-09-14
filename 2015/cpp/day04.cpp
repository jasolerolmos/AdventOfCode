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

string MD5HexaC(string cad) {
    int filesize = cad.length();
    unsigned char * buf =  new unsigned char[12]();
    unsigned char *md5_result = new unsigned char[12]();
    char md5string [50] = "";
    char buffer [50] = "";
    printf("Size: %i", filesize);
    MD5(buf, filesize, md5_result);
    printf("MD5 (%s) = ", cad);
    for (int i=0; i < MD5_DIGEST_LENGTH; i++) {
        sprintf(buffer, "%02x",  md5_result[i]);
        strcat(md5string, buffer);
    }
    printf("\n");
    return "";
} 

string MD5Hexa(string cad) {
    char buffer [32];
    char md5string [32] = "";
    int size = cad.length();
    unsigned char * md5Binary = new unsigned char[size]();
    
    MD5((unsigned char *)cad.c_str(), size, md5Binary);

    for(int i=0; i < MD5_DIGEST_LENGTH; i++){
        sprintf(buffer, "%02x",  md5Binary[i]);
        strcat(md5string, buffer);
    }

    return md5string;
}

int part1(vector<string> lineas){
    int suma = 0;
    bool found = false;
    cout << "Part 1" << endl;
    int num = 0;

    unsigned char * solucion =  new unsigned char[32]();;
    

    for(int i = 0; i < lineas.size(); i++){
        printf(") %s", lineas[i]);
    }


    while(!found){
        ostringstream oss;
        oss << lineas[0] << "0";
        string hashMD5 = oss.str();
        string MD5String = MD5Hexa(lineas[0]);
        
        cout << lineas[0] << " => " << MD5String << endl;
        if (MD5String.substr(0,5) == "00000"){
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

    cout << "abcdef609043" << " in Hexadecimal: " << MD5Hexa("abcdef609043") << endl;
    cout << "abcdef0" << " in Hexadecimal: " << MD5Hexa("abcdef0") << endl;
    int solucion = part1(lineas);
    cout << "Part 1, Solución: " << solucion << endl;
    //solucion = part2(lineas);
    //cout << "Part 2, Solución: " << solucion << endl;
    return 0;
}