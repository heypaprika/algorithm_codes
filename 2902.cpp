//
//  2902.cpp
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
    getline(cin, a);
    for(string::iterator iter = a.begin(); iter != a.end(); ++iter){
        if (int(*iter) >= 65 && int(*iter) <= 90){
            cout << *iter;
        }
    }
    cout << endl;
}
