
import ollama

from PyQt6.QtWidgets import (
  QApplication,
  QMainWindow,
  QWidget,
  QGridLayout,
  QTextEdit,
  QLineEdit,
  QPushButton
)

import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("Chatbot")
    
    layout = QGridLayout()

    self.centralWidget = QWidget()
    self.centralWidget.setLayout(layout)
    self.setCentralWidget(self.centralWidget)

    self.chatWindow = QTextEdit()
    self.chatWindow.setReadOnly(True)
    self.chatWindow.setPlaceholderText("Chat with chatbot")
    layout.addWidget(self.chatWindow, 0, 0, 1, 2)

    self.textBox = QLineEdit()
    self.textBox.returnPressed.connect(self.handler_send_button)
    self.textBox.setPlaceholderText("Type your message here...")

    layout.addWidget(self.textBox, 1, 0)

    self.sendButton = QPushButton("Send")
    self.sendButton.clicked.connect(self.handler_send_button)
    layout.addWidget(self.sendButton, 1, 1)

  def handler_send_button(self):

    myMessage = self.textBox.text()

    self.chatWindow.append("You: " + myMessage)
    self.textBox.clear()

    response = ollama.chat(model='llama3', messages=[
      {
        'role': 'user',
        'content': myMessage,
      },
    ])

    self.chatWindow.append("Chatbot: " + response['message']['content'])

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()