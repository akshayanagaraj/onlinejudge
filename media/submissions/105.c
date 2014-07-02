#include<stdio.h>
main()
{
int x;
scanf("%d",&x);
while(x!=42){
printf("%d",x);
scanf("%d",&x);
}
return 0;
}