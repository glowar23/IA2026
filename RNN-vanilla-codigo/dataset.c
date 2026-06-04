int sumar(int a, int b) { return a + b; }

int restar(int a, int b) { return a - b; }

int multiplicar(int a, int b) { return a * b; }

float dividir(float a, float b) { if(b==0) return 0; return a / b; }

int modulo(int a, int b) { return a % b; }

int es_par(int numero) { return numero % 2 == 0; }

int es_impar(int numero) { return numero % 2 != 0; }

int cuadrado(int n) { return n * n; }

int cubo(int n) { return n * n * n; }

int maximo(int a, int b) { return (a > b) ? a : b; }

int minimo(int a, int b) { return (a < b) ? a : b; }

int valor_absoluto(int n) { return (n < 0) ? -n : n; }

int factorial(int n) { if(n<=1) return 1; return n * factorial(n-1); }

int fibonacci(int n) { if(n<=1) return n; return fibonacci(n-1) + fibonacci(n-2); }

int sumar_arreglo(int arr[], int tamano) { int suma = 0; for(int i=0; i<tamano; i++) suma += arr[i]; return suma; }

int promedio_arreglo(int arr[], int tamano) { return sumar_arreglo(arr, tamano) / tamano; }

int contar_positivos(int arr[], int tamano) { int c = 0; for(int i=0; i<tamano; i++) if(arr[i]>0) c++; return c; }

int contar_negativos(int arr[], int tamano) { int c = 0; for(int i=0; i<tamano; i++) if(arr[i]<0) c++; return c; }

int buscar_elemento(int arr[], int tamano, int objetivo) { for(int i=0; i<tamano; i++) if(arr[i]==objetivo) return i; return -1; }

int existe_elemento(int arr[], int tamano, int objetivo) { return buscar_elemento(arr, tamano, objetivo) != -1; }

void invertir_arreglo(int arr[], int tamano) { int temp; for(int i=0; i<tamano/2; i++) { temp = arr[i]; arr[i] = arr[tamano-1-i]; arr[tamano-1-i] = temp; } }

int longitud_cadena(char *cadena) { int l = 0; while(cadena[l] != '\0') l++; return l; }

void copiar_cadena(char *destino, char *origen) { int i = 0; while((destino[i] = origen[i]) != '\0') i++; }

int comparar_cadenas(char *c1, char *c2) { int i = 0; while(c1[i] == c2[i]) { if(c1[i] == '\0') return 1; i++; } return 0; }

void concatenar_cadenas(char *destino, char *origen) { int i = longitud_cadena(destino); int j = 0; while((destino[i+j] = origen[j]) != '\0') j++; }

char a_mayuscula(char c) { if(c >= 'a' && c <= 'z') return c - 32; return c; }

char a_minuscula(char c) { if(c >= 'A' && c <= 'Z') return c + 32; return c; }

void cadena_mayusculas(char *cadena) { for(int i=0; cadena[i]!='\0'; i++) cadena[i] = a_mayuscula(cadena[i]); }

void cadena_minusculas(char *cadena) { for(int i=0; cadena[i]!='\0'; i++) cadena[i] = a_minuscula(cadena[i]); }

int es_letra(char c) { return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'); }

int es_digito(char c) { return (c >= '0' && c <= '9'); }

int es_vocal(char c) { char m = a_minuscula(c); return (m=='a'||m=='e'||m=='i'||m=='o'||m=='u'); }

int contar_vocales(char *cadena) { int c = 0; for(int i=0; cadena[i]!='\0'; i++) if(es_vocal(cadena[i])) c++; return c; }

int contar_consonantes(char *cadena) { int c = 0; for(int i=0; cadena[i]!='\0'; i++) if(es_letra(cadena[i]) && !es_vocal(cadena[i])) c++; return c; }

int area_rectangulo(int base, int altura) { return base * altura; }

int perimetro_rectangulo(int base, int altura) { return 2 * (base + altura); }

float area_triangulo(float base, float altura) { return (base * altura) / 2; }

float area_circulo(float radio) { return 3.14159 * radio * radio; }

float perimetro_circulo(float radio) { return 2 * 3.14159 * radio; }

int es_primo(int n) { if(n<=1) return 0; for(int i=2; i*i<=n; i++) if(n%i==0) return 0; return 1; }

int siguiente_primo(int n) { int actual = n + 1; while(!es_primo(actual)) actual++; return actual; }

int mcd(int a, int b) { if(b==0) return a; return mcd(b, a%b); }

int mcm(int a, int b) { return (a*b)/mcd(a,b); }

int potencia(int base, int exp) { int res = 1; for(int i=0; i<exp; i++) res *= base; return res; }

int suma_digitos(int n) { int suma = 0; n = valor_absoluto(n); while(n>0) { suma += n%10; n /= 10; } return suma; }

int invertir_numero(int n) { int invertido = 0; int temp = valor_absoluto(n); while(temp>0) { invertido = invertido*10 + temp%10; temp /= 10; } return (n<0) ? -invertido : invertido; }

int es_palindromo_numero(int n) { return n == invertir_numero(n); }

int bisiesto(int anio) { return (anio%4==0 && anio%100!=0) || (anio%400==0); }

int dias_en_mes(int mes, int anio) { if(mes==2) return bisiesto(anio) ? 29 : 28; if(mes==4||mes==6||mes==9||mes==11) return 30; return 31; }

int fecha_valida(int dia, int mes, int anio) { if(anio<1 || mes<1 || mes>12) return 0; return dia>=1 && dia<=dias_en_mes(mes, anio); }

int celsius_a_fahrenheit(int c) { return (c * 9/5) + 32; }

int fahrenheit_a_celsius(int f) { return (f - 32) * 5/9; }

int km_a_metros(int km) { return km * 1000; }

int metros_a_cm(int m) { return m * 100; }

float horas_a_minutos(float horas) { return horas * 60; }

float minutos_a_segundos(float min) { return min * 60; }

int calcular_edad(int anio_nacimiento, int anio_actual) { return anio_actual - anio_nacimiento; }

int es_mayor_de_edad(int edad) { return edad >= 18; }

int obtener_decena(int numero) { return (valor_absoluto(numero) / 10) % 10; }

int obtener_unidad(int numero) { return valor_absoluto(numero) % 10; }
