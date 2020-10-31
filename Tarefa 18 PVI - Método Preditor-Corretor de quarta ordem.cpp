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
    float yi = 200;
    float vi = 5;
    float k = 0.25;
    float m = 2;
    float vf=0;
    float yf=1;
    float dt = 0;
    int cont = 0;
    float v1,y1,v2,y2,v3,y3,v4,y4,vs,ys;
    float dtmax = 0;
    float altmax = 0;
    altmax = yi;
    while(yf > 0){
        dt = dt + 0.1;
        /* F1 */
        v1 = -10-((k/m)*vi);
        y1 = vi;
        /* S2 */
        vs = vi + (dt/2)*(v1);
        ys = yi + (dt/2)*(y1);
        /* F2 */
        v2 = -10-((k/m)*vs);
        y2 = vs;
        /* S3 */
        vs = vi + (dt/2)*(v2);
        ys = yi + (dt/2)*(y2);
        /* F3 */
        v3 = -10-((k/m)*vs);
        y3 = vs;
        /* S4 */
        vs = vi + (dt)*(v3);
        ys = yi + (dt)*(y3);
        /* F4 */
        v4 = -10-((k/m)*vs);
        y4 = vs;

        vf = vi + (dt/6)*(v1 + 2*v2 + 2*v3 + v4);
        yf = yi + (dt/6)*(y1 + 2*y2 + 2*y3 + y4);
        //cout << vf << ";" << yf << ";" << dt << endl;
        if(yf>yi){
            altmax = yf;
            dtmax = dt;
        }
        vi = vf;
        yi = yf;


        cont = cont+1;
    }
    cout << dt << " segundos em " << cont << " iteracoes." << endl;
    cout << "A altura maxima foi de " << altmax << " em " << dtmax << " segundos";
    //Solução
    //1.2 segundos em 12 iteracoes.
    //A altura maxima foi de 201.134 em 0.3 segundos
    return(0);
}
