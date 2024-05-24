#include <stdio.h>
int main()
{
    int quiz[5],count=0,sum = 0;
    int i;
    double avg;
    for (i=0;i<5;i++){
    printf("점수를 입력하시오:");
    scanf("%d",&quiz[i]);
    sum +=quiz[i];
    }
    
    avg = sum/5;
    
    printf("점수의 총합은 %d\n",sum);
    printf("점수의 평균은 %f\n",avg);
    for (i=0; i<5; i++){
      if (quiz[i] < avg){
        count +=1;
      }else{
        continue;
      }
      
      
    }
    printf("평균 미만의 수는 %d\n",count);
        for (i=0; i<5; i++){
          printf("%d학생의 평균과 차이는: %f", i+1,quiz[i]-avg);
        } 
    
}