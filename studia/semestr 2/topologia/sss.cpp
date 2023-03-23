```
#include <iostream>

using namespace std;
int main()
{
int wybor_zadania=0;
cin>>wybor_zadania;
const int rozmiar = 10;
int tablica1[rozmiar];
int max;
int min;
int min2;
double tablica2[rozmiar];
float dzielnik=10.0;
float suma=0;
string slowo;
string wzorzec;

switch(wybor_zadania){
        case 1:

        for (int i=0; i<rozmiar; i++){
	        
		cin >> tablica1[i];
		
	    }
	    min=tablica1[0];
	    max=tablica1[0];
	   for (int i=0; i<rozmiar; i++){
            if(tablica1[i]<=min){
                min=tablica1[i];
            }
            if(tablica1[i]>=max){
                max=tablica1[i];

            }
	    }
	    cout << max << " " << min;
        break;
        
        case 2:
        cin >> slowo;
        cin >> wzorzec;
        
        for (int i=0; i<slowo.size(); i++){
            int pom = 0;
            cout <<1;
            for(int j=0; j<wzorzec.size(); j++){
                if (slowo[i+j] == wzorzec[j]){
                    pom=pom+1;
                    cout <<2;
                }
            }
            if(pom == wzorzec.size()){
                suma=suma+1;
            }
		    
		        
	    }
        cout<<suma;
	    //jedna litera slowo wzorzec dluzszy niz tekst
	    //wzorzec dluzszy niz slowo
        break;
        case 3:

        for (int i=0; i<rozmiar; i++){
	        
		    cin >> tablica2[i];
		
	    }
	   for (int i=0; i<rozmiar; i++){
	        if(tablica2[i]==tablica2[i+1]){
	            suma+=1;
	        }
		
	    }
	    
	    
	    if((suma+1)==rozmiar){
	        cout<<"Not existing";
	    }
	    
	    
	    else{
	    min=tablica2[0];
	    for (int i=0; i<rozmiar; i++){
            if(tablica2[i]<=min){
                min=tablica2[i];
            }
        if(tablica2[i]>=max){
            
        max=tablica2[i];

        }
	    }
	    min2=max;
	    for (int i=0; i<rozmiar; i++){
            if(tablica2[i]<min2 && tablica2[i]!=min){
                min2=tablica2[i];

            }
	    }
	    cout<<min2;
	    
	    }

        break;
        default:
        cout<<"Wrong task number";
        break;
}


return 0;
}
```