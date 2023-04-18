#include <stdio.h>

int main()
{
    int c=0,c1=0,x=0;
    //declaring variables and initializing to 0
    char str[111];
    printf("Enter a string please");
    scanf("%s",&str);
    //receiving input from user 
    for(int i=0;str[i]!='\0';i++) //loop that iterates through the string
    {
        if(str[i]==str[i+1])//comparing the character at the ith position with the character at the (i+1)th position
        {
            c++;//incrementing the counter variable
            x=i+1;//storing i+1 to compare with the next character
        }

        if(str[x]==str[x+1])//comparing the character at the xth position with the character at the (x+1)th position 
            c1++;//incrementing the second counter variable

    }
    if(c>c1)
        printf("%d",c);//displaying c if c is greater
    else
        printf("%d",c1);//displaying c1 if c1 is greater
return 0;
}
