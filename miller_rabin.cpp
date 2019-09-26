#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string>
#include<time.h>
#include<fstream>

using std::string;
using std::cin;
using std::cout;
using std::fstream;


int generateRandomInt(int input){
  int random_number = rand() % input;
  return random_number;
}
 


int main(){
  int k = 100; //for testing random number generation
  //seed the time for the random number generation
  srand(time(NULL));

  cout << "Hello World\n";
  cout << "This is the random generated number: " << generateRandomInt(k) << "\n\n";

  

  return 0;
}