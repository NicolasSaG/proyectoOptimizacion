#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>

//gcc examen.c -o examen
//ejecutar: ./examen iteraciones numPoblaciones numIndividuos


double getZLineal(int n, double x[n], double y[n], double m, double b);
double generarIndividuo(double lim_inf, double lim_sup);
int generarSemillaAleatoria();

int main(int argc, char const *argv[]){
	double x[4] = {1, 3 ,3.5, 4};
	double y[4] = {0.42, 0.75, 1.00, 0.92};
	//usando geneticos
	//calcular +-(Sumx)^2
	int lim_m = 100;
	long i, j;
	double lim_b = 0;
	for (i = 0; i < 4; ++i){
		lim_b += x[i];
	}
	lim_b = pow(lim_b, 2);
	//calcular limites
	//listo xd

	//generar individuos
	int num_poblaciones = 100;
	int num_individuos = 1000;

	//mejor general
	double mejorZ = 10000.0;
	double mejorM = 0.0;
	double mejorB = 0.0;
	long idVector = 0.0;
	long pob = 0.0;

	//mejor poblacion
	double mejorZPob, mejorMPob, mejorBPob;
	long idVectorPob = 0;

	double m_aux, b_aux = 0, z_aux;

	srand(generarSemillaAleatoria());
	for(i = 0; i < num_poblaciones; i++){
		mejorZPob = 100000.0;
		mejorMPob = 0.0;
		mejorBPob = 0.0;
		idVectorPob = 0.0;
		for(j = 0; j < num_individuos; j++){
			m_aux = generarIndividuo(-100.0, 100.0);
			b_aux = generarIndividuo(-132.25, 132.25);
			z_aux = getZLineal(4, x, y, m_aux, b_aux);
			if(z_aux < mejorZPob){
				mejorZPob = z_aux;
				mejorMPob = m_aux;
				mejorBPob = b_aux;
				idVectorPob = j;
			}
		}
		if(mejorZPob < mejorZ){
			mejorZ = mejorZPob;
			mejorM = mejorMPob;
			mejorB = mejorBPob;
			idVector = idVectorPob;
			pob = i;
		}
	}
	 


	printf("Poblacion:%ld, vector:%ld. Z= %lf; m= %lf; b=%lf\n",pob, idVector, mejorZ, mejorM, mejorB);
	return 0;
}


double getZLineal(int n, double x[n], double y[n], double m, double b){
	double z = 0;
	int i;
	for(i = 0; i < n; i++){
		z += fabs(m*x[i] + b - y[i]);
	}
	return z;
}

double generarIndividuo(double lim_inf, double lim_sup){
	// double individuo = lim_inf + (double) (rand() / (double) (RAND_MAX + 1.0)) * (lim_sup - lim_inf + 1.0);
	// printf("%llf\n", individuo);
	double range = (lim_sup - lim_inf); 
  double div = RAND_MAX / range;
  return lim_inf + (rand() / div);
	//return individuo;
}

int generarSemillaAleatoria(){
	int semilla;
	//horas x min + seg * numprocs
	system("tasklist | find /c \"exe\" > nprocs.txt");
	FILE * f_np = fopen("nprocs.txt", "r");
	if(f_np == NULL)
		exit(-1);
	char * line = NULL;
  size_t len = 0;
	int read;
	read = getline(&line, &len, f_np);
	fclose(f_np);
	system("del nprocs.txt");

	semilla = atoi(line);

	time_t t_actual = time(NULL);
  struct tm *conv;
  conv = localtime(&t_actual);
  semilla = (semilla * conv->tm_hour + conv->tm_min)* conv->tm_sec;
	return semilla;
}