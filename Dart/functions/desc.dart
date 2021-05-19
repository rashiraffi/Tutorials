void main() {
  describe("RR", 22, 1.8);
  final person1 = details("RRR", 23, 1.9);
  print(person1);
}

// Describe is a function with no return
void describe(String name, int age, double height)
{
  print("Name = $name, Age = $age, Height= $height");
}

String details(String name, int age, double height)
{
  return "Name = $name, Age = $age, Height= $height";
}