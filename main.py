from settings import (
    DATABASE_SETTINGS,
    SURFACE_LENGTH,
    SURFACE_WIDTH,
    DOTS_PER_LENGTH,
    DOTS_PER_WIDTH,
    MU,
    DEVIATION,
    SIGMA
)


print('Запуск исследования...\n\n')
print(
    'Параметры исследования\n'
    f'- размер поверхности: {SURFACE_LENGTH} x {SURFACE_WIDTH} мм\n'
    f'- кол-во точек на длину поверхности: {DOTS_PER_LENGTH}\n'
    f'- кол-во точек на ширину поверхности: {DOTS_PER_WIDTH}\n'
    f'- величина допуска: {DEVIATION} мм\n'
    f'- математическое ожидание: {MU}\n'
    f'- значение сигма: {SIGMA}\n'
)

# TODO: Инициализация БД и сохранение в нее генерируемых поверхностей
#  Построение касательных плоскостей к поверхностям и вычисление зазоров
#  Расчет результатов
#  Графическое представление результатов
