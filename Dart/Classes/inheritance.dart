void main(){

  //Immunatble because of final keyword
  final person = Person("RR",23,1.8,67);
  //person.name = "RRR";
  //Cannot change the variable because it's immutable.
  print(person.details());
  print("BMI = ${person.bmi()}");
  final employee = Employee("RRR",22,1.9,65,"iDontKnow",65000);
  print("Employee: ${employee.name} \nSalary: ${employee.salary}");

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

class Employee extends Person{
  // Employee(String name, int age, double height, double weight, this.taxcode, this.salary) : super(name,age,height,weight);
  Employee(String name, int age, double height, double weight, this.taxcode, this.salary)
   : super(name,age,height,weight);
  final String taxcode;
  final int salary;
}