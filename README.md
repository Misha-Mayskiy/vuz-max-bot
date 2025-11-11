## Универсальный бот "Вузуслуги"

### Запуск через Docker

Для запуска проекта необходимо, чтобы на компьютере был установлен Docker и Docker Compose.

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/Misha-Mayskiy/vuz-max-bot.git
   cd vuz-max-bot
   ```

2. **Соберите и запустите контейнеры:**
   ```bash
   docker compose up --build
   ```

3. **Доступ к API:**
   После запуска сервер будет доступен по адресу: `http://localhost:8000`
   Документация API (Swagger): `http://localhost:8000/docs`

   **Тестовые данные:**
   При первом запуске автоматически создается Супер-Админ:
    - **Login:** admin
    - **Password:** admin
