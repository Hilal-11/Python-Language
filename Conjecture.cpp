
#include<iostream>
using namespace std;
int main(){
    
    long long n;
    cout<<"Enter value of n for colartz conjectue :- "<<endl;
    cin>>n;
    long long counter = 0;

    while (n != 1){
        if(n % 2 != 0) {
            cout<<n<<"\t";
            n = (3 * n) + 1;
            counter = counter + 1;
        }
        else{
            cout<<n<<"\t";
            n = (n / 2);
            counter = counter + 1;
        }
    }
    
    cout<<"\n\n total number of steps to reach 1 for value"<<n<<" = "<<counter;
    return 0;
} 
