#include <iostream>
using namespace std;

int main() {
	int t, n, w, temp;
	cin >> t;
	for(int s=0; s<t;s++){
	    cin>>n>>w;
	    int a[n], amt=0;
	    for(int i=0; i<n; i++){
	        cin>>a[i];
	        for(int j=0; j<i; j++){
	            if(a[i]>a[j]){
	                temp = a[i];
	                a[i] = a[j];
	                a[j] = temp;
	            }
	        }
	    }
	    
	    for(int k=0; k<n; k++){
	        amt = amt+a[k];
	        if(amt>=w){
	            cout<<n-k-1;
	            cout<<endl;
	            break;
	        }
	    }
	}
	return 0;
}
