# Настройки базы данных
DATABASE_SETTINGS = {
    "database_name": "surfaces",
    "host": "127.0.0.1",
    "user": "username",
    "password": "1234",
    "port": 5432
}

# Кол-во генерируемых поверхностей
GENERATION_TRIES_COUNT = 100

# Номинальная длина поверхности
SURFACE_LENGTH = 1

# Номинальная ширина поверхности
SURFACE_WIDTH = 1

# Кол-во точек по длине
DOTS_PER_LENGTH = 25

# Кол-во точек по ширине
DOTS_PER_WIDTH = 25

# Допуск (стандартное отклонение)
DEVIATION = 0.1

# Математическое ожидание
MU = 0

# Сигма (1/6 как в машиностроении)
SIGMA = 0.2 / 6
