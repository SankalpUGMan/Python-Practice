#include<stdio.h>

int main()
{

float n[1000];
int m[1000];
float alpha;
int k;

m[0] = 0;
n[0] = 0.2;
alpha = 3.1428;				// I defined pi as 3.1428

	for(k=1;k<=999;k++)
	{
 	n[k]=((n[k-1]+alpha)*100);
 	m[k]=n[k];
  	n[k]=n[k]-m[k];
  	printf("%f\n",n[k]);
  	alpha=3.1428;
	}

  return 0;
}
