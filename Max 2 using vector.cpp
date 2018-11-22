#include <iostream>
#include<cstdio>
#include<vector>
using namespace std;

int main()
{
    int i,n,val;
    vector<int> v;
    cout<<"Enter the size of the vector :"<<endl;
    cin>>n;
    for(i=0;i<n;++i){
        cin>>val;
        v.push_back(val);
    }
    for(i=0;i<v.size();i++){
        cout<<"v["<<i<<"]"<<v[i]<<endl;
    }
    int firstmax_value=0;
    for(i=0;i<v.size();++i){
        if(v[i]>firstmax_value){
            firstmax_value=v[i];
        }
    }
    cout<<"The first  maximum value is = "<<firstmax_value<<endl;
    int secondmax_value=0;
    for(i=0;i<v.size();++i){
        if(v[i]<firstmax_value&&v[i]>secondmax_value){
            secondmax_value=v[i];
        }
    }
    cout<<"The second  maximum value is = "<<secondmax_value;

}
