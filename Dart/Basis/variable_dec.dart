void main()
{
  String name = 'RR';
  int age = 007;
  double height = 1.8;
  print("Name = $name, Age = $age, Height= $height");
  //Correct
  print("My Name has ${name.length} letters");
  //Wrong
  print("My Name has $name.length letters\n\n\n");

  // var
  var var_name = 'RR';
  print("Name = $var_name");

  var var_age = 23;
  print("Name = $var_age");

  var var_height = 1.8;
  print("Name = $var_height");
}