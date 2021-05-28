import 'dart:ffi';

void main(){

  //Immunatble because of final keyword
  final person = Person("RR",23,1.8,67);
  //person.name = "RRR";
  //Cannot change the variable because it's immutable.
  print(person.details());
  print("BMI = ${person.bmi()}");

}

class Person{
  final String name;
  final int age;
  final double weight;
  final double height;

  Person(this.name,this.age,this.height,this.weight);
  String details()
  {
    return "Name = $name, Age = $age, Height = $height, Weight = $weight";
  }

  double bmi() => weight/(height*height);
}