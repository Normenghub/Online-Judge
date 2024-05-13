#include <stdio.h>
void add(int,int,char);
void substract(int,int,char);
void multiply(int,int,char);
void divide(int,int,char);
int main(){

int num1,num2;
char opr;
printf("숫자 2개 입력:");
scanf("%d%d",&num1,&num2);
fflush(stdin);
printf("연산자 입력: ");
    scanf(" %c", &opr);
    switch(opr){
    case '+':
    add(num1,num2,opr);
    break;
    case '-':
    substract(num1,num2,opr);
    break;
    case '*':
    break;
    multiply(num1,num2,opr);
    case '/':
    divide(num1,num2,opr);
    break;



 }
return 0;
 }

void add(int n1, int n2, char opr)
{
 int result;
  result= n1 + n2;

  printf("%d %c %d = %d\n",n1,opr,n2,result); 

}

void substract(int n1, int n2, char opr){
  int result;
  result= n1 - n2;

  printf("%d %c %d = %d\n",n1,opr,n2,result); 
 
 

}void multiply(int n1, int n2, char opr){
  int result;
  result= n1 * n2;

  printf("%d %c %d = %d\n",n1,opr,n2,result); 
 
 

}
void divide(int n1, int n2, char opr){
  float result;
  result= n1 / n2;

  printf("%d %c %d = %f\n",n1,opr,n2,result); 
 
 

}