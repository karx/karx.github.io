/* Read input from STDIN. Print your output to STDOUT*/
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
#include <algorithm> 


int main(int argc, char *a[])
{
    int n,t,i;
    scanf("%d",&t);
    while(t--) {
        int tickets[10000], usedTickets[10000];
        int incSum[10000], excSum[10000], pMaxSum[10000];
        scanf("%d",&n);
        
        for(i=0;i<n;i++)
        {
            usedTickets[i] = 0;
            incSum[i] = 0;
            excSum[i] = 0;
            scanf("%d",(tickets + i));
            // scanf("%d",(tickets + n - 1 -i));
        }

        int maxSum = 0;
        if (tickets[0] > 0) {
            maxSum = tickets[0];
            usedTickets[0]=1;
        }
        incSum[0] = tickets[0];
        excSum[0] = 0; 
        pMaxSum[0] = incSum[0] > excSum[0] ? incSum[0] : excSum[0];
        for(i=1;i<n;i++) {
            incSum[i] = excSum[i-1] + tickets[i];

            excSum[i] = 
                excSum[i-1]  > incSum[i-1] ? excSum[i-1] : incSum[i-1];

            pMaxSum[i] = incSum[i] > excSum[i] ? incSum[i] : excSum[i];
        }

        
        // for(i=0;i<n;i++) {
        //     printf("%5d",tickets[i]);
        // }
        // printf("\n");
        // for(i=0;i<n;i++) {
        //     printf("%5d",excSum[i]);
        // }
        // printf("\n");

        // for(i=0;i<n;i++) {
        //     printf("%5d",incSum[i]);
        // }
        // printf("\n");

        int maxSumz = pMaxSum[n-1];
        for(i=n-1;i>=0;i--) {
            if(maxSumz <= 0) {
                break;
            }
            if(pMaxSum[i] == maxSumz) {
                continue;
            } else {
                printf("%d",tickets[i+1]);
                maxSumz -= tickets[i+1];
            }
        }
        if(maxSumz != 0) {
            printf("%d", maxSumz); //would be same as tickets[0]
        }

        printf("\n");
        // printf("\n");
        // printf("\n");
    }
    //Write code here
    return 0;
}
