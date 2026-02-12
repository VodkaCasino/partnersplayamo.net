#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для замены карточек казино в index.html
"""

import re

# Читаем файл
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Карточки для замены (casino-6 до casino-17)
replacements = {
    'casino-6': {
        'old_pattern': r'<a href="#view-bob-casino" class="telegram-button" id="casino-6"[^>]*>.*?</a>',
        'new': '''        <div class="telegram-button" id="casino-6">
            <div class="button-number">6</div>
            <div class="casino-logo">
                <img src="img/bob-casino.svg" alt="Bob Casino">
            </div>
            <div class="button-content">
                <h3>PLAY TELEGRAM</h3>
                <div class="accessSub">
                    GO TO TELEGRAM, OPEN THE MINI APP, AND PLAY TELEGRAM Bob Casino.
                </div>
            </div>
            <div class="telegram-widget">
                <figure style="margin: 0; padding: 0;">
                    <iframe src="https://t.me/partnersplayamo/35?comment=60&amp;embed=1" style="position: absolute; width: 96%; right: 0.1px; color: rgb(0, 0, 0); height: 97%; border-radius: 50%; border: none; z-index: 1;" loading="lazy"></iframe>
                </figure>
                <a href="tg://resolve?domain=partnersplayamo_bot" alt="Telegram MINI-APP REGISTRATION Bob Casino" class="tg" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; z-index: 2; text-decoration: none;">
                    <div style="position: relative; width: 100%; height: 100%; left: 1px; border-radius: 45%; cursor: pointer; transition: border-color 0.3s ease, transform 0.2s ease; background-image: linear-gradient(to bottom, #192232, #192232), linear-gradient(to bottom, var(--topLine) 20%, #192232 47%); overflow: hidden;">
                        <img src="img/telegram-icon.svg" alt="Telegram Bob Casino" loading="lazy" style="position: absolute; top: 50%; left: 47%; width: 60%; height: 60%; transform: translate(-50%, -50%); pointer-events: none;">
                    </div>
                </a>
            </div>
        </div>'''
    }
}

# Пока заменю только casino-6 вручную, остальные сделаю через search_replace
print("Скрипт создан. Замены будут выполнены через search_replace tool.")

