#include <stdio.h>

int main(){
    int kor[5] = {90,80,70,60,100};
    int math[5] = {81,91,81,81,100};
    int order[5] = {1,1,1,1,1};
    double avg[5];
    
    for(int i =0; i < 5; i++){
        avg[i] = (double) (kor[i] + math[i])/2;
    }
    for (int k = 0; k <4; k++){
        for (int z= k+1 ; z <=4 ; z++){
            if (avg[k] > avg[z]){
                order[z]++;
            }else if (avg[k] < avg[z]){
                order[k]++;
                
            }
            
        }
        
    }
    for (int j = 0; j <5; j++){
        printf("국어 = %d, 수학 = %d, 평균 = %.2f 석차 = %d ",kor[j],math[j], avg[j],order[j]);
        
    }
    
    
    
}

//  85.5 83.5 75.5 70.5 100     2 3 4 5 1
