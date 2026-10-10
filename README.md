# Практическая работа №1. Этап 1: REPL

**Дисциплина:** Конфигурационное управление  
**Студент:** Алиев Довлат Фазильевич  
**Группа:** ИКБО-62-25  
**Вариант:** 2  
**Репозиторий:** https://github.com/Dovlat060108/mirea-config-v2-stage-1  
**Ветка этапа:** `stage-1`

## Общее описание

Консольный эмулятор UNIX-подобной оболочки на Python 3.10+.
Эта версия включает этапы 1-1. Внешние библиотеки не нужны.
Приглашение использует имя пользователя и имя компьютера реальной ОС.
Парсер разделяет ввод по пробельным символам. Кавычки, конвейеры,
перенаправления и раскрытие переменных окружения не поддерживаются.
Команды эмулятора не запускают программы реальной ОС.

## Реализованные этапы

1. REPL, парсер, приглашение ОС, заглушки ls/cd, exit и ошибки.

## Сборка, запуск и тестирование

Отдельная сборка не требуется: Python исполняет исходный код.
Все команды запускаются из корня репозитория.

```sh
python3 --version
sh run.sh
make test
# Равнозначный запуск тестов без make:
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Windows: `run.bat`; тесты: `set PYTHONPATH=src`, затем
`python -m unittest discover -s tests -v`.

## Команды и примеры

- `exit`: завершить сеанс; аргументы запрещены.
- `ls [путь]`, `cd [путь]`: заглушки; печатают имя и список аргументов.

## Демонстрация ошибок

```text
unknown
Ошибка: неизвестная команда: unknown
exit extra
Ошибка: использование: exit
```

Интерактивная проверка: `sh run.sh`, затем `ls`, `cd /docs`,
`ls a b`, `unknown`, `exit`. Проверка через stdin: `sh scripts/demo-repl.sh`.

## Проверка

При подготовке выполнено 6 автоматических тестов; все прошли.
Тесты проверяют результаты команд, неверные аргументы и обработку ошибок.

## Функции исходного кода

- `main.main`: Initialize and run the current stage.
- `shell.parse`: Split a command by whitespace, without quotes or expansion.
- `Shell.__init__`: Register the commands provided by the current stage.
- `Shell.prompt`: Use the actual OS username and hostname in the prompt.
- `Shell.execute`: Return success; display errors and keep the session usable.
- `Shell.stub`: Validate prototype ls/cd arguments and show their values.
- `Shell.exit`: Stop the current shell; exit accepts no arguments.
- `Shell.repl`: Read commands until exit, EOF or keyboard interrupt.

## Структура

- src/: исходный код, main.py - точка входа.
- tests/: автоматические тесты unittest.
- examples/: демонстрационные команды и данные.
- scripts/: сценарии реальной ОС для демонстрации.
- run.sh, run.bat, Makefile: запуск и тестирование.
- .gitignore: исключение временных файлов и результатов сборки.

PDF README предназначен для загрузки в СДО вместе с URL репозитория.
PDF и архивы не добавляются в исходный git-репозиторий.
