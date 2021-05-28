void main(){

  //Immunatble because of final keyword
  final person = Person("RR",23,1.8);
  //person.name = "RRR";
  //Cannot change the variable because it's immutable.
  print(person.name);

}

class Person{
  final String name;
  final int age;
  final double height;

  Person(this.name,this.age,this.height);
}