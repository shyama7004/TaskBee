import 'package:flutter/material.dart';
import 'src/screens/example_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: ExampleScreen(),
    );
  }
}
