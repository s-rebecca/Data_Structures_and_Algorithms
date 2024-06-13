#include <iostream>
using namespace std;

int main() {
	int t,l,r;
	cin>>t;
	
	for(int i=0; i<t; i++){
	    cin>>l>>r;
	    int sum = 0;
	    
	    for(int j=l;j<=r;j++){
	        int num = j%10;
	        if (num == 2|| num == 3|| num == 9){
	            sum++;
	        }
	    }
	    
	    cout<<sum<<endl;
	}
	
	return 0;
}
