void main(){

  final square = Square(10);
  print("Area of square: ${square.area()}");

}
//Class is declared
abstract class Shape{
  double area();
}
//implementation of the class
class Square implements Shape{
  Square(this.sides);
  final double sides;
  double area() => sides * sides ;
}