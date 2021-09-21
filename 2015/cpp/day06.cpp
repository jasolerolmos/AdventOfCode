#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <time.h>

using namespace std;

int SIZE_X = 1000;
int SIZE_Y = 1000;

vector<string> readFileString() {
    vector<string> lineas;
    fstream newfile;
    newfile.open("../input/input06.txt",ios::in);
    if (newfile.is_open()){
        string tp;
        while(getline(newfile, tp)){
            lineas.push_back(tp);
        }
        newfile.close();
    }

    return lineas;
}

vector<string> split(string cad, string delimiter) {
    size_t pos = 0;
    std::string token;
    vector<string> splited;
    while ((pos = cad.find(delimiter)) != std::string::npos) {
        token = cad.substr(0, pos);
        splited.push_back(token);
        cad.erase(0, pos + delimiter.length());
    }
    splited.push_back(cad);

    return splited;
}

int** CreateLights(int width, int height) {
    int** lights= 0;
    lights = new int*[width];
    for (int y = 0; y < height; y++ ){
        lights[y] = new int[height];
        for (int x = 0; x < width; x++) {
            lights[y][x] = 0;
        }
    }

    return lights;
}

int** ToggleLights(int** lights, int* points) {
    for (int y = points[1]; y <= points[3]; y++ ){
        for (int x = points[0]; x <= points[2]; x++) {
            lights[y][x] = (lights[y][x] + 1) % 2;
        }
    }
    return lights;
}

int** OnOffLights(int** lights, int* points, int value) {
    for (int y = points[1]; y <= points[3]; y++ ){
        for (int x = points[0]; x <= points[2]; x++) {
            lights[y][x] = value;
        }
    }
    return lights;
}

void VerLights(int** lights) {
    for (int y = 0; y < SIZE_Y; y++ ){
        for (int x = 0; x < SIZE_X; x++) {
            cout << " " << lights[y][x] << " ";
        }
        cout << endl;
    }
}

int * AnalizeLine(string p1, string p2){
    vector<string> pa = split(p1, ",");
    vector<string> pb = split(p2, ",");
    int *points = new int[4];
    points[0] = atoi(pa[0].c_str());
    points[1] = atoi(pa[1].c_str());
    points[2] = atoi(pb[0].c_str());
    points[3] = atoi(pb[1].c_str());

    return points;
}

int CountOn(int ** lights) {
    int sum = 0;
    for (int y = 0; y < SIZE_Y; y++ ){
        for (int x = 0; x < SIZE_X; x++) {
            if (lights[y][x] == 1) {
                sum++;
            }
        }
    }
    return sum;
}


int part1(vector<string> lineas) {
    int validos = 0;
    int** lights = CreateLights(SIZE_X, SIZE_Y);
    for(int i=0; i<lineas.size(); i++){
        vector<string> parts = split(lineas[i], " ");
        if ( parts.size() == 4) {
            int *points = AnalizeLine(parts[1], parts[3]);
            lights = ToggleLights(lights, points);
        } else if (parts.size() == 5) {
            int* points = AnalizeLine(parts[2], parts[4]);
            if (parts[1] == "on"){
                OnOffLights(lights, points, 1);
            } else {
                OnOffLights(lights, points, 0);
            }
       }
    }

    return CountOn(lights);
}

int main () 
{   
    vector<string> lineas = readFileString();
    cout << "\nPart 1, Solución: " << endl;

    clock_t tStart = clock();
    int solucion = part1(lineas);
    cout << "\t" << to_string(solucion) << endl;
    printf("Time: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);

    //cout << "\nPart 2, Solución: " << endl;

    //tStart = clock();
    //solucion = part2(lineas);
    //cout << "\t" << to_string(solucion) << endl;
    //printf("Time: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
}