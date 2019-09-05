# Laboratório de Introdução à Programação Paralela. OpenMP
Material desenvolvido por Clynton Tomacheski para o Workshop no Flisol. 
Todos os exemplos foram escritos em C++. Mas é possível adaptá-los para C se for de sua preferência.

*Um programa executando em uma arquitetura de memória compartilhada é dividido em um conjunto de threads de controle.  Threads podem ser criadas no início do programa ou de forma dinâmica durante sua execução.   
As threads dentro de um processo compartilham estado que inclui as variáveis globais, variáveis estáticas, o sistema de arquivos e o heap global. Os registros, a pilha de execução e as variáveis de pilha locais são privadas a cada thread. 
Threads se comunicam implicitamente escrevendo e lendo variáveis compartilhadas, e se coordenam através de construções de sincronização.* 

## O que é OpenMP

**O**pen**MP** = *Open Multi-Processing*

Basicamente é uma API que permite o desenvolvimento de programas *multi-thread* em memória compartilhada em C/C++ e Fortran. OpenMP é **fácil** de usar e tem ênfase na paralelização de laços.

Contém três principais componentes:
- Diretivas de compilação
- Biblioteca de funções
- Variáveis de ambiente

## Primeiro programa: Hello World! (serial)
Vamos testar o gcc de sua máquina para garantir que está tudo certo. Crie o arquivo `main.cpp` contendo o seguinte código:

```cpp
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    cout << "Hello World!\n";
    return 0;
}
```

Para compilar e executar o programa:

```bash
$ g++ main.cpp -o output
$ ./output
```

## Primeiro programa: Hello World! (paralelo!)
Crie o arquivo `main.cpp` contendo o seguinte código:

```cpp
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    #pragma omp parallel
    {
        cout << "Hello World!\n";
        return 0;
    }
}
```

Para compilar e executar o programa:

```bash
$ g++ -fopenmp main.cpp -o output
$ ./output
```

Qual é a saída da execução? Exatamente **p** vezes o texto "Hello World!", sendo **p** o número de *threads* do processador.
Como podemos saber quantas threads podem ser executadas em nosso computador simultâneamente? Veja em /proc/cpuinfo o campo "physical id" quantos cores tem no seu computador, ou execute:
```
cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l
```
e no campo core id, quantas threads lógicas podem ser executadas.
```
# cat /proc/cpuinfo | egrep "core id|physical id" | tr -d "\n" | sed s/physical/\\nphysical/g | grep -v ^$ | sort | uniq | wc -l
```
Um aparte, o que são threads lógicas? Veja no documento em anexo o texto sobre *SMT*.

`#pragma omp parallel` é uma **diretiva de compilação** do OpenMP que indica que o bloco de código será executado em paralelo.

## Paralelizando um laço

Como dito anteriormente, o foco do OpenMP é a paralelização de laços. Normalmente em um algoritmo, as estruturas de *loop* representam a porção de código com maior custo computacional.

Sendo assim, existe a diretiva de compilação `#pragma omp for` em OpenMP. A seguir, são apresentadas duas formas de paralelizar um laço:

```cpp
#pragma omp parallel
{
    #pragma omp for
    for(int i = 0; i < n; i++)
    {
        cout << i << endl;
    }
}
```

Forma reduzida:

```cpp
#pragma omp parallel for
for(int i = 0; i < n; i++)
{
    cout << i << endl;
}
```
É possível perceber que a execução do laço não segue a ordenação do vetor percorrido.

## Usando funções da API do OpenMP
(./hangman.py)