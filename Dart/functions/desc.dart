import 'dart:ffi';

void main() {
  var height = 1.8;
  describe("RR", 22, height);
  final person1 = details("RRR", 23, height);
  print(person1);
  describe1("RRR", 23);
}

// Describe is a function with no return
void describe(String name, int age, double height)
{
  print("Name = $name, Age = $age, Height= $height");
}


// Describe is a function with return
String details(String name, int age, double height)
{
  return "Name = $name, Age = $age, Height= $height";
}


// Describe is a function with optional argument
void describe1(String name, int age, [double height = 0.0])
{
  // here height is optional
  print("Name = $name, Age = $age, Height= $height");
  //Output Name = RRR, Age = 23, Height= 0.0
}