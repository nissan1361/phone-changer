<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/license-GPLv3-blue?style=flat-square">
  <img alt="License: GPL v3" src="https://img.shields.io/badge/license-GPLv3-blue?style=flat-square">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/python-3.14+-blue?style=flat-square">
  <img alt="Python 3.14+" src="https://img.shields.io/badge/python-3.14+-blue?style=flat-square">
</picture>

# 📱 Phone Changer — Подбор смартфона

Интерактивная программа, которая помогает подобрать смартфон по вашим предпочтениям: бюджет, камера, игры, автономность, экосистема и размер.

## ✨ Возможности

- **CLI-версия** (`main.py`) — консольный опросник с пошаговым подбором
- **GUI-версия** (`gui.py`) — графический интерфейс на PyQt6 с прогресс-баром и навигацией
- **Гибкие рекомендации** — алгоритм учитывает до 6 параметров и выдаёт актуальные модели 2024–2026 годов
- **Две экосистемы** — рекомендации как для Android, так и для iOS

## 🚀 Запуск

### Консольная версия

```bash
python main.py
```

### Графическая версия

```bash
pip install PyQt6
python gui.py
```

## ⚙️ Параметры подбора

| Параметр | Градации |
|----------|----------|
| 💰 Бюджет | до 20 000 ₽ / до 40 000 ₽ / до 70 000 ₽ / от 70 000 ₽ |
| 📷 Камера | не важно → критически важно (5 уровней) |
| 🎮 Игры | не играю → хочу максимум (5 уровней) |
| 🔋 Автономность | не важно → критически важна (5 уровней) |
| 🍏 Экосистема | Android / iOS |
| 📐 Размер | Компактный / Обычный или большой |

## 📁 Структура проекта

```
phone-changer/
├── main.py       # CLI-версия
├── gui.py        # GUI-версия (PyQt6)
├── file.py       # Вспомогательный файл
├── LICENSE       # GPLv3
└── README.md     # Этот файл
```

## 📄 Лицензия

Проект распространяется под лицензией GNU General Public License v3.0. Подробнее — в файле [LICENSE](LICENSE).
