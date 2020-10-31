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
    float dt = 0;
    float k = 0.25;
    float m = 2;
    float v1,v2,y1,y2;
    float cont = 0;
    float altmax;
    float dtmax;
    while(yf>0){
        dt = dt + 0.1;
        /* S0+1/2 */
        v1 = vi + (dt/2)*(-10 - (k*vi)/m);
        y1 = yi + (dt/2)*vi;
        //cout << v1 << ";" << y1 << endl;
        /* S barra */
        v2 = vi + dt*(-10 - (k*vi)/m);
        y2 = yi + dt*vi;
        //cout << v2 << ";" << y2 << endl;
        /* Sk+1 */
        vf = vi + (dt*(((1.0/6)*(-10-(k*vi)/m)) + ((4.0/6)*(-10-v1)) + ((1.0/6)*(-10-v2))));
        yf = yi + (dt*(((1.0/6)*vi) + ((4.0/6)*v1) + ((1.0/6)*v2)));
        //cout << vf << ";" << yf << endl;
        if(yf>yi){
            altmax = yf;
            dtmax = dt;
        }
        vi = vf;
        yi = yf;
        cont = cont +1;
    }
    cout << "A altura maxima e de  " << altmax << " em " << dtmax << " segundos." << endl;
    cout << "O tempo de queda e " << dt << " com velocidade final de " << vf;
    // Solução
    //A altura maxima e de  200.963 em 0.2 segundos.
    //O tempo de queda e 2 com velocidade final de 0.221188

    return(0);
}
