#pragma once
#include <string>
using namespace std;

class Car {
private:
    string name;
public:
    Car(string name) : name(name) {}
    friend void info_car(Car& car, class Person& person);
};

class Person {
private:
    string name;
    int age;
public:
    Person(string name) : name(name) {}
    friend void info_car(Car& car, Person& person);
};

void info_car(Car& car, Person& person);