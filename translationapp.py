import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPlainTextEdit, QTextEdit, QPushButton, QComboBox, QGridLayout, QMessageBox
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from googletrans import Translator

class TranslationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Translation App")
        self.setFixedSize(500, 400)
        self.setStyleSheet(
            """
            background-color: #272822;
            color: #F8F8F2;
            """
        )

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a grid layout
        self.layout = QGridLayout()

        # Logo
        logo_label = QLabel(self)
        logo_label.setPixmap(QPixmap("logo.png"))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Origin language input
        self.origin_combo = QComboBox()
        self.origin_combo.addItems(["English", "Spanish", "French", "German", "Japanese", "Korean"])
        self.origin_combo.setStyleSheet(
            """
            background-color: #75715E;
            color: #F8F8F2;
            """
        )

        # Target language input
        self.target_combo = QComboBox()
        self.target_combo.addItems(["English", "Spanish", "French", "German", "Japanese", "Korean"])
        self.target_combo.setStyleSheet(
            """
            background-color: #75715E;
            color: #F8F8F2;
            """
        )

        # Copy translated text button
        self.copy_button = QPushButton("Copy Translated Text")
        self.copy_button.setStyleSheet(
            """
            background-color: #A6E22E;
            color: black;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            """
        )
        self.copy_button.clicked.connect(self.copyTranslatedText)

        # Input text to translate
        self.input_text = QPlainTextEdit()
        self.input_text.setPlaceholderText("Enter text to translate...")
        self.input_text.setStyleSheet(
            """
            background-color: #75715E;
            color: #F8F8F2;
            """
        )

        # Translated text output
        self.translated_text = QTextEdit()
        self.translated_text.setReadOnly(True)
        self.translated_text.setStyleSheet(
            """
            background-color: #49483E;
            color: #F8F8F2;
            font-size: 14px;
            """
        )
        self.translated_text.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.translated_text.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.translated_text.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Translate button
        self.translate_button = QPushButton("Translate")
        self.translate_button.setStyleSheet(
            """
            background-color: #66D9EF;
            color: #F8F8F2;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            """
        )
        self.translate_button.clicked.connect(self.translateText)

        # Add widgets to the grid layout
        self.layout.addWidget(logo_label, 0, 0, 1, 2)
        self.layout.addWidget(QLabel("Origin Language:"), 1, 0)
        self.layout.addWidget(self.origin_combo, 1, 1)
        self.layout.addWidget(QLabel("Target Language:"), 2, 0)
        self.layout.addWidget(self.target_combo, 2, 1)
        self.layout.addWidget(self.input_text, 3, 0, 1, 2)  # Span 1 row and 2 columns
        self.layout.addWidget(self.translate_button, 4, 0, 1, 2)  # Span 1 row and 2 columns
        self.layout.addWidget(self.translated_text, 5, 0, 1, 2)  # Span 1 row and 2 columns
        self.layout.addWidget(self.copy_button, 6, 0, 1, 2)  # Span 1 row and 2 columns

        self.central_widget.setLayout(self.layout)

        # Create hover effects for buttons
        button_style = """
            QPushButton {
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #F92672;
                color: #F8F8F2;
            }
        """

        # Copy translated text button style
        copy_button_style = """
            QPushButton {
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
                background-color: #A6E22E;
                color: black;
            }
            QPushButton:hover {
                background-color: #66D9EF;
                color: #F8F8F2;
            }
        """

        # Add styles to the buttons
        self.copy_button.setStyleSheet(copy_button_style)
        self.translate_button.setStyleSheet(button_style)

    def translateText(self):
        translator = Translator()
        origin_lang = self.origin_combo.currentText()
        target_lang = self.target_combo.currentText()
        text_to_translate = self.input_text.toPlainText()

        # Check if the input text is empty before proceeding with translation
        if not text_to_translate:
            QMessageBox.warning(self, "Input Error", "Please enter text to translate.")
            return

        try:
            translated_result = translator.translate(text_to_translate, src=origin_lang.lower(), dest=target_lang.lower())
            self.translated_text.setPlainText(translated_result.text)
            # You can add the translation to favorites here if you want
        except Exception as e:
            self.translated_text.setPlainText("Translation Error")

    def copyTranslatedText(self):
        translated_text = self.translated_text.toPlainText()
        if translated_text:
            clipboard = QApplication.clipboard()
            clipboard.setText(translated_text)
            QMessageBox.information(self, "Copy Successful", "Translated text copied to clipboard.")
        else:
            QMessageBox.warning(self, "Copy Error", "There is no translated text to copy.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslationApp()
    window.show()
    sys.exit(app.exec())
