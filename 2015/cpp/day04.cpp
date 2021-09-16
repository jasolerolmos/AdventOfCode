#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <time.h>
#include <openssl/md5.h>

using namespace std;

unsigned char *MD5(const unsigned char *d, unsigned long n, unsigned char *md);

vector<string> readFileString() {
    vector<string> lineas;
    fstream newfile;
    newfile.open("../input/input04.txt",ios::in);
    if (newfile.is_open()){
        string tp;
        while(getline(newfile, tp)){
            lineas.push_back(tp);
        }
        newfile.close();
    }

    return lineas;
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

int calcRange(string cad, int value, int incremento, string search){
    bool found = false;
    int num = 0;

    unsigned char * solucion =  new unsigned char[32]();

    while(!found){
        ostringstream oss;
        oss << cad << to_string(num);
        string hashMD5 = oss.str();
        string MD5String = MD5Hexa(hashMD5);
        
        if (MD5String.substr(value,search.length()) == search){
            cout << "Encontrado: " << num << endl;
            cout << hashMD5 << " => " << MD5String << endl;
            found = true;
        } else {
            num = num + incremento;
        }
    }
    return num;
}

int main () 
{   
    vector<string> lineas = readFileString();
    cout << "\nPart 1, Solución: " << endl;

    clock_t tStart = clock();
    int solucion = calcRange(lineas[0], 0, 1, "00000");
    cout << "\t" << to_string(solucion) << endl;
    printf("Time: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    
    cout << "\nPart 2, Solución: " << endl;
    tStart = clock();
    solucion = calcRange(lineas[0], 0, 1, "000000");
    cout << "\t" <<  to_string(solucion) << endl;
    printf("Time: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    
    return 0;
}