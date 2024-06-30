import 'package:flutter_test/flutter_test.dart';
import '../lib/src/models/example_model.dart';

// Placeholder for model tests
void main() {
  test('Example model test', () {
    var model = ExampleModel(id: '1', name: 'Test');
    expect(model.id, '1');
    expect(model.name, 'Test');
  });
}
