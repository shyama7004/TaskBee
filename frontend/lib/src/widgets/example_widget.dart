import 'package:flutter/material.dart';

// Placeholder for a reusable widget
class ExampleWidget extends StatelessWidget {
  final String text;

  ExampleWidget({required this.text});

  @override
  Widget build(BuildContext context) {
    return Text(text);
  }
}
