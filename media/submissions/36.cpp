#include<stdio.h>
#include<iostream>
main(){
int x;
scanf("%d",&x);
while(x!=42){
printf("%d\n",x);
scanf("%d",&x);
}
return 0;
}