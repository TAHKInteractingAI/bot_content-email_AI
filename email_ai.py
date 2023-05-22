import openai
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QInputDialog, QTextEdit, QMessageBox
class EmailGenerator(QWidget):
    def __init__(self):
        super().__init__()
        #openai.api_key = ""
        # Create widgets
        self.setWindowTitle("Email Generator by Open AI")
        self.resize(800, 400)
        self.recipient_label = QLabel("Tên người nhận:")
        self.recipient_edit = QLineEdit()
        self.sender_label = QLabel("Tên người gửi:")
        self.sender_edit = QLineEdit()
        self.keywords_label = QLabel("Keywords:")
        self.keywords_edit = QLineEdit()
        self.topic_label = QLabel("Topic:")
        self.topic_edit = QLineEdit()
        self.language_label = QLabel("Language:")
        self.language_combo = QComboBox()
        self.language_combo.addItem("Tiếng việt")
        self.language_combo.addItem("English")
        self.max_tokens_button = QPushButton("Set max_tokens")
        self.n_button = QPushButton("Set n")
        self.stop_button = QPushButton("Set stop")
        self.temperature_button = QPushButton("Set temperature")
        self.api_key_button = QPushButton("Set API Key")
        self.generate_button = QPushButton("Generate Email")
        self.result_textedit = QTextEdit()
        #self.result_label = QLabel()
        
        self.max_tokens_button.clicked.connect(self.set_max_tokens)
        self.n_button.clicked.connect(self.set_n)
        self.stop_button.clicked.connect(self.set_stop)
        self.temperature_button.clicked.connect(self.set_temperature)
        self.api_key_button.clicked.connect(self.set_api_key)

        # Create layout and add widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.recipient_label)
        self.layout.addWidget(self.recipient_edit)
        self.layout.addWidget(self.sender_label)
        self.layout.addWidget(self.sender_edit)
        self.layout.addWidget(self.keywords_label)
        self.layout.addWidget(self.keywords_edit)
        self.layout.addWidget(self.topic_label)
        self.layout.addWidget(self.topic_edit)
        self.layout.addWidget(self.language_label)
        self.layout.addWidget(self.language_combo)
        self.layout.addWidget(self.max_tokens_button)
        self.layout.addWidget(self.n_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.temperature_button)
        self.layout.addWidget(self.api_key_button)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.result_textedit)
        self.setLayout(self.layout)
        
        self.generate_button.clicked.connect(self.generate_email)
        self.show()
        # Set default values
        self.max_tokens = None
        self.n = None
        self.stop = None
        self.temperature = None
        self.api_key = None

    def set_max_tokens(self):
        # code to set max_tokens value
        new_value, ok = QInputDialog.getInt(self, "Set max_tokens", "Enter new value for max_tokens:")
        if ok:
            self.max_tokens = new_value
            self.max_tokens_button.setText(f'max_tokens: {new_value}')
        pass
    def set_n(self):
        # code to set n value
        new_value, ok = QInputDialog.getInt(self, "Set n", "Enter new value for n:")
        if ok:
            self.n = new_value
            self.n_button.setText(f'n: {new_value}')
        pass
    def set_stop(self):
        # code to set stop value
        new_value, ok = QInputDialog.getText(self, "Set stop", "Enter new value for stop:")
        if ok:
            self.stop = new_value
            self.stop_button.setText(f'stop: {new_value}')
        pass
    def set_temperature(self):
        # code to set temperature value
        new_value, ok = QInputDialog.getDouble(self, "Set temperature", "Enter new value for temperature:")
        if ok:
            self.temperature = new_value
            self.temperature_button.setText(f'temperature: {new_value}')
        pass
    def set_api_key(self):
        # code to set api key value
        new_value, ok = QInputDialog.getText(self, "Set API Key", "Enter new value for API Key:")
        if ok:
            self.api_key = new_value
            openai.api_key = self.api_key
            self.api_key_button.setText(f'API Key: {new_value}')
        pass
    
    def generate_email(self):
        if self.max_tokens is None:
            QMessageBox.warning(self, "Warning", "Bạn cần nhập max tokens trước khi tạo email")
            return
        if self.n is None:
            QMessageBox.warning(self, "Warning", "Bạn cần nhập n trước khi tạo email")
            return
        if self.temperature is None:
            QMessageBox.warning(self, "Warning", "Bạn cần nhập temperature trước khi tạo email")
            return
        if self.api_key is None:
            QMessageBox.warning(self, "Warning", "Bạn cần nhập API Key trước khi tạo email")
            return

        recipient_name = self.recipient_edit.text()
        sender_name = self.sender_edit.text()
        keywords = self.keywords_edit.text()
        topic = self.topic_edit.text()
        language = self.language_combo.currentText()

        if language == "English":
            prompt = (f"Write an email about {topic} addressed to {recipient_name} from {sender_name} using the following keywords: {keywords}")
        else:
            prompt = (f"Viết một email về {topic} gửi đến {recipient_name} từ {sender_name} sử dụng từ khóa: {keywords}")

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=self.max_tokens,
            n =self.n,
            stop=self.stop,
            temperature=self.temperature
        )
        email_text = response["choices"][0]["text"]
        self.result_textedit.setPlainText(email_text)
        #self.result_label.setText(email_text)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    email_generator = EmailGenerator()
    sys.exit(app.exec_())