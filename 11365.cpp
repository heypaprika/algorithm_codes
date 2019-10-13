//
//  11365.cpp
//  practice1
//
//  Created by Chang Hyun Lee on 13/10/2019.
//  Copyright © 2019 Chang Hyun Lee. All rights reserved.
//

#include "iostream"
#include "algorithm"
using namespace std;

int main(void){
    string a;
    while(true){
        getline(cin, a);
        if(a == "END") break;
        reverse(a.begin(), a.end());
        cout<<a<<endl;
    }
}
