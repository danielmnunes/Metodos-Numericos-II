#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <limits.h>
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <windows.h>

using namespace std;

int main(){
    float vi = 5;
    float vf = 0;
    float yi = 200;
    float yf = 1;
    float cont = 0;
    float dt = 0;
    float m = 2;
    float k = 0.25;
    float dtmax = 0;
    float altmax = 0;
    altmax = yi;
    while(yf>0){
        dt = dt + 0.1;
        vf = (m/(m+k*dt))*(vi-10*dt);
        yf = yi + (((m*dt)/(m+k*dt))*(vi-10*dt));
        if(yf>yi){
            altmax = yf;
            dtmax = dt;
        }
        vi = vf;
        yi = yf;
        cont = cont + 1;
    }
    cout << dt << " segundos em " << cont << " iteracoes." << endl;
    cout << "A altura maxima foi de " << altmax << " em " << dtmax << " segundos";
    // Solução
    //1.2 segundos em 12 iteracoes.
    //A altura maxima foi de 200.776 em 0.2 segundos
    return(0);

}
