# include <stdio.h>

long long factorial(int n ,int k){
     if(n==k || k == 0) return 1;
     else return factorial(n - 1,k) + factorial (n-1 , k-1);

}
