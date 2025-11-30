#include <iostream>
#include <string>
using namespace std;

class Car;
class Person {
private:
    string name;
    int age;
public:
    Person(string name) {
        this->name = name;
    }
    friend void info_car(Car& car, Person& person);
};

class Car {
private:
    string name;
public:
    Car(string name) {
        this->name = name;
    }
    friend void info_car(Car& car, Person& person);
};
void info_car(Car& car, Person& person) {
    cout << "A person named " << person.name << " has a " << car.name << " car." << endl;
}