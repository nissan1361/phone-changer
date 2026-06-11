import sys
from io import StringIO

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QRadioButton, QButtonGroup,
    QPushButton, QTextEdit, QProgressBar,
)
from PyQt6.QtCore import Qt

from main import rekomendovat


class PhoneWizard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Подбор смартфона")
        self.setMinimumSize(640, 520)
        self.resize(720, 600)

        central = QWidget()
        self.setCentralWidget(central)
        self.layout = QVBoxLayout(central)
        self.layout.setContentsMargins(24, 24, 24, 24)

        self.questions = [
            ("Какой у вас бюджет?", [
                "до 20 000 ₽ — надёжный бюджетный телефон",
                "20 000 – 40 000 ₽ — хороший средний сегмент",
                "40 000 – 70 000 ₽ — выше среднего, почти флагман",
                "от 70 000 ₽ — флагман без компромиссов",
            ]),
            ("Насколько важна камера?", [
                "не важно — сфоткать документы и всё",
                "средне — иногда снимаю на отдыхе",
                "важно — люблю фотографировать",
                "очень важно — снимаю фото/видео постоянно",
                "критически важно — увлекаюсь мобильной фотографией",
            ]),
            ("Как часто вы играете в игры на телефоне?", [
                "не играю вообще",
                "редко — казуальные игры",
                "иногда — нетребовательные игры",
                "часто — современные игры на средних настройках",
                "постоянно — хочу максимум графики и FPS",
            ]),
            ("Насколько важна автономность?", [
                "не важно — всегда есть розетка",
                "средне — хватает на день",
                "важно — хочется полтора дня без подзарядки",
                "очень важно — телефон живёт в руках весь день",
                "критически важно — розетки рядом нет часами",
            ]),
            ("Какая экосистема вам ближе?", [
                "Android — гибкость, свобода настройки",
                "iPhone — всё работает из коробки, связка с Mac/iPad",
            ]),
            ("Какой размер телефона предпочитаете?", [
                "компактный — чтобы удобно лежал в одной руке",
                "обычный или большой — для видео и игр",
            ]),
        ]

        self.idx = 0
        self.groups: list[QButtonGroup] = []
        self._init_widgets()
        self._show_question()

    def _init_widgets(self):
        self.progress = QProgressBar()
        self.progress.setTextVisible(True)
        self.layout.addWidget(self.progress)

        self.header = QLabel()
        self.header.setStyleSheet("font-weight: bold; font-size: 11pt;")
        self.layout.addWidget(self.header)

        self.prompt = QLabel()
        self.prompt.setWordWrap(True)
        self.prompt.setStyleSheet("font-size: 13pt; margin-bottom: 8px;")
        self.layout.addWidget(self.prompt)

        for _ in self.questions:
            g = QButtonGroup(self)
            self.groups.append(g)

        self.radio_layout = QVBoxLayout()
        self.layout.addLayout(self.radio_layout)

        self.layout.addStretch()

        btn_row = QHBoxLayout()
        self.layout.addLayout(btn_row)

        self.back_btn = QPushButton("← Назад")
        self.back_btn.clicked.connect(self._prev)
        btn_row.addWidget(self.back_btn)

        btn_row.addStretch()

        self.next_btn = QPushButton("Далее →")
        self.next_btn.clicked.connect(self._next)
        btn_row.addWidget(self.next_btn)

        self._clear_radio_buttons()

    def _clear_radio_buttons(self):
        while self.radio_layout.count():
            item = self.radio_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def _show_question(self):
        self._clear_radio_buttons()

        q_text, options = self.questions[self.idx]

        self.progress.setValue(int((self.idx + 1) / len(self.questions) * 100))
        self.progress.setFormat(f"{self.idx + 1} / {len(self.questions)}")
        self.header.setText(f"Вопрос {self.idx + 1} из {len(self.questions)}")
        self.prompt.setText(q_text)

        group = self.groups[self.idx]
        for i, opt in enumerate(options, 1):
            rb = QRadioButton(opt)
            rb.setStyleSheet("font-size: 11pt; padding: 4px 0;")
            group.addButton(rb, i)
            self.radio_layout.addWidget(rb)

        if self.idx == 0:
            self.back_btn.setEnabled(False)
        else:
            self.back_btn.setEnabled(True)

        if self.idx == len(self.questions) - 1:
            self.next_btn.setText("Показать результат")
        else:
            self.next_btn.setText("Далее →")

    def _prev(self):
        self.idx -= 1
        self._show_question()

    def _next(self):
        group = self.groups[self.idx]
        if group.checkedId() == -1:
            return

        if self.idx < len(self.questions) - 1:
            self.idx += 1
            self._show_question()
        else:
            self._show_result()

    def _show_result(self):
        self._clear_radio_buttons()
        self.progress.setValue(100)
        self.progress.setFormat("Готово")
        self.header.setText("РЕЗУЛЬТАТ ПОДБОРА")
        self.prompt.setText("")

        answers = [g.checkedId() for g in self.groups]

        buf = StringIO()
        old = sys.stdout
        sys.stdout = buf
        try:
            rekomendovat(*answers)
        finally:
            sys.stdout = old

        text_area = QTextEdit()
        text_area.setPlainText(buf.getvalue())
        text_area.setReadOnly(True)
        text_area.setStyleSheet("font-size: 11pt;")
        self.radio_layout.addWidget(text_area)

        self.back_btn.setEnabled(True)

        self.next_btn.setText("Пройти заново")
        try:
            self.next_btn.clicked.disconnect()
        except TypeError:
            pass
        self.next_btn.clicked.connect(self._restart)

    def _restart(self):
        self.idx = 0
        for group in self.groups:
            group.setExclusive(False)
            for btn in group.buttons():
                btn.setChecked(False)
            group.setExclusive(True)

        try:
            self.next_btn.clicked.disconnect()
        except TypeError:
            pass
        self.next_btn.clicked.connect(self._next)

        self._show_question()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhoneWizard()
    window.show()
    sys.exit(app.exec())
