#include <iostream>
#include <set>
#include <string>
#include <sstream>

using namespace std;

uint8_t * conv(uint32_t n, uint8_t *tab)
{
	tab[0] = (uint8_t)n;
	tab[1] = n >> 8;
	tab[2] = n >> 16;
	tab[3] = n >> 24;
	return tab;
}



uint32_t conv1(uint8_t *p)
{
	uint32_t n = p[3] << 24 | p[2] << 16 | p[1] << 8 | p[0];
	return n;
}

void incptr(int * start, int *stop)
{
	//int *p = start;

	while(start != stop)
	{
		*start+=2;
		cout << *start << '\n';
		start++;
	}
}
int main ()
{

uint32_t n = 0x45464748;
uint8_t *tab = new uint8_t[4];
uint8_t *ptr = conv(n, tab);
uint8_t tab2[4] = {'H', 'G', 'F', 'E'};
uint32_t nu = conv1(tab2);
cout << "NU: " << nu;
for(int i = 0; i<4; ++i)
{
	cout << ptr[i] << '\n';
}
//uint32_t a = conv1(ptr);

int * ptr2 = nullptr;
unsigned int i = 1;
char * pChar = (char *)&i;
if (*pChar)
	printf("little");
else
	printf("Big");

int t [] = {10,20,30,40,50};
incptr(&t[0], t + 5);


delete [] ptr;
  return 0;
}
