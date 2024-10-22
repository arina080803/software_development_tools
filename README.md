# software_development_tools

## Добавлено тестирование функций!

1.	Цели и задачи тестирования:

- проверка правильности работы функций вычисления площади и периметра для различных геометрических фигур
- необходимо протестировать функции на корректных данных, граничных значениях (нулевые значения, отрицательные числа) и некорректных данных (строки, None)

2.	Описание тестируемого продукта:

Набор функций для расчёта площади и периметра различных фигур: круга, прямоугольника, квадрата и треугольника.

3.	Область тестирования:

Функции для расчёта площади и периметра из следующих модулей:
- circle.py: area(r) и perimeter(r);
- rectangle.py: area(a, b) и perimeter(a, b);
- square.py: area(a) и perimeter(a);
- triangle.py: area(a, h) и perimeter(a, b, c)

4.	Стратегия тестирования:
   
Для каждой функции будут созданы тесты с корректными значениями, граничными случаями и некорректными данными. Все тесты будут выполнены с использованием библиотеки unittest.

5.	Критерии приемки:
   
Тесты считаются пройденными, если они возвращают ожидаемые результаты без ошибок и исключений. Для каждого модуля должны быть пройдены все предназначенные тесты.

6.	Ожидаемые результаты:
   
Все тесты должны успешно выполнить расчёты площади и периметра для корректных данных, а также корректно обрабатывать граничные и некорректные входные данные.
