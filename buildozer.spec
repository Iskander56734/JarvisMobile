[app]
title = Jarvis AI
package.name = jarvisai
package.domain = org.iskander
version = 1.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# НАМЕРТВО СШИВАЕМ ПИТОН И СИСТЕМНЫЕ ЗАВИСИМОСТИ МИКРОФОНА И ЗВУКА ДЖАРВИСА!
requirements = python3,kivy,requests


orientation = portrait
fullscreen = 1
android.api = 31
android.minapi = 21
android.ndk = 25b
android.private_storage = 1

# ЖЕСТКО ЗАПРАШИВАЕМ ПРАВА НА ЗАПИСЬ ЗВУКА ДЛЯ СМАРТФОНА!
android.permissions = INTERNET, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS

# ХАКЕРСКИЙ ИГНОР: Обходим сишные баги компиляции SSL и SQLite на 11-й минуте!
p4a.blacklist = sqlite3,openssl,ssl,_ssl,_sqlite3

android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
