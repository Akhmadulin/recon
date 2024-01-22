#!/bin/bash

# Проверяем установку Python и Pip
if ! command -v python3 &> /dev/null; then
    echo "Python3 не установлен. Устанавливаем..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

if ! command -v pip3 &> /dev/null; then
    echo "Pip3 не установлен. Устанавливаем..."
    sudo apt-get install -y python3-pip
fi

# Устанавливаем библиотеку python-telegram-bot версии 13.7
pip3 install python-telegram-bot==13.7

# Копируем main.py в /usr/bin/ и переименовываем в tbrecon
sudo cp main.py /usr/bin/tbrecon

# Делаем tbrecon исполняемым
sudo chmod +x /usr/bin/tbrecon

# Создаем systemd-сервис для tbrecon
echo "[Unit]
Description=Your Telegram Bot

[Service]
ExecStart=/usr/bin/python3 /usr/bin/tbrecon
Restart=always
User=your_username

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/tbrecon.service

# Перезапускаем systemd
sudo systemctl daemon-reload

# Запускаем бота
sudo systemctl start tbrecon.service

# Автозапуск при старте системы
sudo systemctl enable tbrecon.service

echo "Установка завершена."
