//정수를 0이 될 때까지 계속 입력받는다.
//입력된 짝수의 개수와 홀수의 개수, 입력된 수의 최댓값, 최솟값을 출력한다. 
#include <stdio.h>
#include <stdlib.h>
int main()
{
	int evenCount=0, oddCount=0;
	int max, min;
	int number; //입력 받는 수 저장
	
	printf("숫자를 입력하세요: ");
	scanf("%d",&number);
	 if (number % 2 ==0){
	  evenCount +=1;
	  max = number;
	  min = number;
	  
	     
	 }else{
	     	  oddCount +=1;
	  max = number;
	  min = number;
	     
	 }
	
 while(1){
		printf("숫자를 입력하세요: ");
	scanf("%d",&number);
	if (number == 0){
		printf("짝수의 개수 %d개, 홀수의 개수 %d개, 최댓값 = %d, 최솟값 = %d\n",evenCount,oddCount,max,min);
		printf("프로그램을 종료 합니다. \n");
		exit(0);
		
	} else{
	      if (number % 2 ==0){
              evenCount +=1;
	           if (number > max){
                  max = number;
              } else if (number < min){
                  min = number;
              } else{
              }
	          
	          
	      }else{
	          oddCount +=1;
	         if (number > max){
                  max = number;
              } else if (number < min){
                  min = number;
              } else{
              } 
	          
	      }
	    
	}
	
	//최댓값, 최솟값 초기화
	
	//홀수,짝수 판별하여 개수를 저장한다.
}
}
