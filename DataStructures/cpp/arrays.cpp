#include <iostream>
#include <string>

using namespace std;

class CAR {
private:
    string model;
    string brand;
    string manufacture;

protected:
    void setBrand(string brand) {
        this->brand = brand;
    }
    void setModel(string model) {
        this->model = model;
    }
    void setDOM(string dateofman) {
        this->manufacture = dateofman;
    }

public:
    string getBrand() {
        return brand;
    }
    string getModel() {
        return model;
    }
    string getDOM() {
        return manufacture;
    }
};

class Person {
private:
    string name;
    int age = 0;
    CAR* car = nullptr;

public:
    void setName(string name, int age) {
        this->name = name;
        this->age = age;
    }

    void setCar(CAR* car) {
        this->car = car;
    }

    void printDetails() {
        cout << name << " is " << age << " years old and has ";
        if (car) {
            cout << car->getBrand() << " " << car->getModel() << " manufactured on " << car->getDOM();
        } else {
            cout << "no car";
        }
        cout << "." << endl;
    }
};

class Volvo : public CAR {
public:
    void setDetails(string model, string manufacture) {
        setBrand("Volvo");
        setModel(model);
        setDOM(manufacture);
    }
};

int main() {
    Person* P = new Person();
    P->setName("Chakradhar", 30);

    Volvo* myVolvo = new Volvo();
    myVolvo->setDetails("XC90", "2022-10-01");

    P->setCar(myVolvo);
    P->printDetails();

    delete myVolvo;
    delete P;
    return 0;
}
