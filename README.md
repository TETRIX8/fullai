# 🌐 AKGPT & FullAI - Полная документация ИИ моделей

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/badge/PyPI-akgpt-orange.svg)](https://pypi.org/project/akgpt/)
[![Downloads](https://img.shields.io/badge/Downloads-1K+-brightgreen.svg)](https://pypi.org/project/akgpt/)

**Современный API Gateway и Python библиотека для доступа к передовым моделям искусственного интеллекта с красивой документацией и простым интерфейсом.**

---

## 🚀 AKGPT - Python Библиотека

**AKGPT** — это простая и мощная Python-библиотека для взаимодействия с Text-to-Text API. Она предоставляет унифицированный интерфейс для работы с различными моделями ИИ, включая поддержку изображений, потокового вывода и гибких параметров настройки.

### ✨ Особенности AKGPT

- 🎯 **Простота использования** - минималистичный API для быстрого старта
- 🤖 **12+ моделей ИИ** - от Gemini до GPT-5 Nano
- 📸 **Мультимодальность** - поддержка текста и изображений
- 🔄 **Потоковый вывод** - real-time генерация текста
- ⚙️ **Гибкие параметры** - температура, top_p, penalties и другие
- 🔐 **Приватные запросы** - защита конфиденциальности
- 📋 **JSON ответы** - структурированные данные
- 🌍 **Многоязычность** - поддержка всех языков

## 🌟 FullAI Gateway - Основные возможности

- **12+ ИИ моделей** - от текстовых до мультимодальных и аудио
- **Красивая документация** - полное описание всех моделей и примеров
- **Интерактивное тестирование** - попробуйте API прямо в браузере
- **Серверная обработка** - высокопроизводительная обработка запросов
- **Высокая производительность** - кэширование и оптимизация
- **CORS поддержка** - для интеграции с любыми приложениями

## 📚 Доступные модели

### 🧠 Текстовые модели

| Модель | Провайдер | Описание | Пример запроса |
|--------|-----------|----------|----------------|
| **DeepSeek V3** | Azure | Универсальная модель для обработки текста | `https://fullai.vercel.app/Напиши%20статью%20об%20ИИ?model=deepseek` |
| **DeepSeek R1 0528** | Azure | Модель с улучшенным логическим мышлением | `https://fullai.vercel.app/Реши%20математическую%20задачу?model=deepseek-r1` |
| **Grok-3 Mini** | Azure | Модель от xAI с инструментами | `https://fullai.vercel.app/Курс%20BTC%20к%20USD?model=grok` |

### 🖼️ Мультимодальные модели

| Модель | Провайдер | Описание | Пример запроса |
|--------|-----------|----------|----------------|
| **Mistral Small 3.1** | Cloudflare | Анализ изображений и текста | `https://fullai.vercel.app/Опиши%20изображение:https://example.com/image.jpg?model=mistral` |
| **OpenAI GPT-4.1 Mini** | Azure | Обработка текста и изображений | `https://fullai.vercel.app/Придумай%20пост%20для%20соцсети%20к%20фото:https://example.com/photo.jpg?model=openai` |
| **OpenAI O3 (Reasoning)** | chatwithmono.xyz | Сложные аналитические задачи | `https://fullai.vercel.app/Проанализируй%20график:https://example.com/chart.jpg?model=o3` |

### 🎙️ Аудио модели

| Модель | Провайдер | Описание | Пример запроса |
|--------|-----------|----------|----------------|
| **GPT-4o Audio Preview** | Azure | 13 голосов, аудио ввод/вывод | `https://fullai.vercel.app/Прочитай%20новости?model=openai-audio&voice=nova` |
| **Hypnosis Tracy** | Azure | Гипнотические аудио-сессии | `https://fullai.vercel.app/Создай%20гипнотическую%20сессию%20для%20сна?model=hypnosis` |

### 🔍 Специальные модели

| Модель | Провайдер | Описание | Пример запроса |
|--------|-----------|----------|----------------|
| **SearchGPT** | chatwithmono.xyz | Поиск в реальном времени | `https://fullai.vercel.app/Новости%20технологий%20за%20неделю?model=searchgpt` |
| **BIDARA (NASA)** | Azure | Биомиметический дизайн | `https://fullai.vercel.app/Создай%20дизайн%20в%20стиле%20биомиметики?model=bidara` |
| **MIDIjourney** | Azure | Генерация MIDI треков | `https://fullai.vercel.app/Создай%20MIDI%20трек%20в%20стиле%20jazz?model=midijourney` |
| **Evil (Uncensored)** | Cloudflare | Нефильтрованные ответы | `https://fullai.vercel.app/Необычный%20сценарий%20для%20фильма?model=evil` |

## 🛠️ API Документация

### Базовый URL
```
https://text.pollinations.ai
```

### Получить список моделей
```bash
GET /models
```

**Пример:**
```bash
curl -X GET "https://text.pollinations.ai/models" \
  -H "Content-Type: application/json"
```

### Отправить запрос к модели
```bash
POST /chat
```

**Пример:**
```bash
curl -X POST "https://text.pollinations.ai/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek",
    "messages": [
      {
        "role": "user",
        "content": "Привет! Как дела?"
      }
    ]
  }'
```

### Прямые URL запросы

Формат: `https://text.pollinations.ai/{запрос}?model={модель}&voice={голос}`

**Примеры:**

1. **Текстовый запрос:**
   ```
   https://text.pollinations.ai/Напиши%20статью%20об%20ИИ?model=deepseek
   ```

2. **Запрос с изображением:**
   ```
   https://text.pollinations.ai/Опиши%20изображение:https://example.com/image.jpg?model=mistral
   ```

3. **Аудио запрос:**
   ```
   https://text.pollinations.ai/Прочитай%20новости?model=openai-audio&voice=nova
   ```

### Доступные голоса для аудио моделей

```
alloy, echo, fable, onyx, nova, shimmer, coral, verse, ballad, ash, sage, amuch, dan
```

## 🔧 Технические параметры

| Модель | Провайдер | Входные данные | Выходные данные | Инструменты |
|--------|-----------|----------------|-----------------|-------------|
| DeepSeek V3 | Azure | Текст | Текст | ❌ |
| DeepSeek R1 | Azure | Текст | Текст | ❌ |
| Grok-3 Mini | Azure | Текст | Текст | ✅ |
| Mistral Small 3.1 | Cloudflare | Текст + Изобр. | Текст | ✅ |
| GPT-4.1 Mini | Azure | Текст + Изобр. | Текст | ✅ |
| GPT-4o Audio | Azure | Текст + Аудио | Аудио + Текст | ✅ |
| SearchGPT | chatwithmono | Текст | Текст | ✅ |
| O3 | chatwithmono | Текст + Изобр. | Текст | ✅ |

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/your-username/fullai.git
cd fullai
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Локальный запуск
```bash
python src/main.py
```

### 4. Деплой проекта
```bash
# Локальный запуск для тестирования
python -m flask run

# Или деплой на любую платформу
pip install -r requirements.txt
python src/main.py
```

## 📁 Структура проекта

```
fullai/
├── src/
│   ├── main.py              # Основной сервер Flask
│   └── static/
│       ├── index.html       # Главная страница документации
│       ├── examples.html    # Интерактивные примеры
│       ├── styles.css       # Стили
│       └── script.js        # JavaScript функциональность
├── config.json             # Конфигурация проекта
├── requirements.txt        # Python зависимости
└── README.md              # Документация
```

## 🔍 Мониторинг и статус

### Health Check
```bash
GET /health
```

### API Status
```bash
GET /api/status
```

**Пример ответа:**
```json
{
  "service": "FullAI Gateway",
  "status": "online",
  "target_api": {
    "url": "https://text.pollinations.ai",
    "status": "online"
  },
  "features": [
    "Text Models (DeepSeek, Grok, GPT)",
    "Multimodal Models (Mistral, GPT-4.1)",
    "Audio Models (GPT-4o Audio)",
    "Special Models (SearchGPT, BIDARA, MIDIjourney)"
  ],
  "supported_methods": ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
}
```

## 🎨 Особенности дизайна

- **Современный UI** - градиенты, анимации, стеклянный эффект
- **Адаптивный дизайн** - работает на всех устройствах
- **Интерактивность** - поиск, копирование кода, анимации
- **Темная тема** - приятная для глаз
- **Smooth scrolling** - плавная навигация

## 🔧 Конфигурация

### Переменные окружения
```bash
# Основной URL целевого API
TARGET_API_BASE_URL=https://text.pollinations.ai

# Время кэширования (в секундах)
CACHE_DURATION=300
```

### Настройки деплоя
- **Runtime**: Python 3.9+
- **Memory**: Оптимизированное использование памяти
- **Response Time**: Быстрые ответы (обычно < 5 секунд)
- **CORS**: Включен для всех доменов

## 🛡️ Безопасность

- **CORS защита** - настраиваемые заголовки
- **Валидация запросов** - проверка входных данных
- **Таймауты** - защита от зависших запросов
- **Обработка ошибок** - детальные сообщения об ошибках

## 📊 Производительность

- **Кэширование** - модели кэшируются на 5 минут
- **Стриминг** - большие ответы передаются по частям
- **Оптимизация** - сжатие и минификация статических файлов
- **CDN** - глобальное распространение и высокая доступность

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции
3. Внесите изменения
4. Создайте Pull Request

## 📄 Лицензия

MIT License - см. файл LICENSE для деталей.

## 📞 Поддержка

- **GitHub репозиторий**: https://github.com/TETRIX8/akgpt
- **PyPI пакет**: https://pypi.org/project/akgpt/
- **Документация AKGPT**: https://github.com/TETRIX8/akgpt#readme

---

# 📚 AKGPT - Подробная документация библиотеки

## 📦 Установка AKGPT

Установите библиотеку через pip:

```bash
pip install akgpt
```

Или установите последнюю версию с GitHub:

```bash
pip install git+https://github.com/TETRIX8/akgpt.git
```

---

## 🚀 Быстрый старт с AKGPT

### 📌 Основной запрос

```python
from akgpt import AKGPT

# Инициализация клиента
client = AKGPT()

# Простой запрос
prompt = "Что такое искусственный интеллект?"
result = client.query(prompt)

if result:
    print("Ответ API:", result)
```

### ⚙️ Запрос с дополнительными параметрами

```python
from akgpt import AKGPT

client = AKGPT()

prompt = "Напиши короткое стихотворение о роботах"
result = client.query(
    prompt=prompt,
    model="mistral",
    system="Ты талантливый поэт",
    temperature=0.8,
    max_tokens=200
)

if result:
    print("Стихотворение:", result)
```

---

## 🧠 Полный список параметров метода `query`

| Параметр | Тип | По умолчанию | Описание |
|----------|-----|--------------|----------|
| `prompt` | `str` | **обязательный** | Входной текстовый промпт |
| `model` | `str` | `"gemini"` | Модель для генерации |
| `system` | `str` | `None` | Системный промпт (роль модели) |
| `temperature` | `float` | `0.7` | Контроль случайности (0.0 - 3.0) |
| `top_p` | `float` | `1.0` | Ядерная выборка (0.0 - 1.0) |
| `max_tokens` | `int` | `150` | Максимальное количество токенов |
| `presence_penalty` | `float` | `0.0` | Штраф за повторяющиеся токены (-2.0 до 2.0) |
| `frequency_penalty` | `float` | `0.0` | Штраф за частоту токенов (-2.0 до 2.0) |
| `seed` | `int` | `None` | Сид для воспроизводимых результатов |
| `json_response` | `bool` | `False` | Вернуть ответ в формате JSON |
| `stream` | `bool` | `False` | Потоковая передача (SSE) |
| `private` | `bool` | `False` | Приватный запрос |
| `referrer` | `str` | `None` | Источник запроса |

---

## 🤖 Полный список доступных моделей

### 📝 Текстовые модели

| Код модели | Полное название | Провайдер | Описание |
|------------|-----------------|-----------|----------|
| `gemini` | Gemini 2.5 Flash Lite | Google | Быстрая и эффективная модель |
| `gpt-5-nano` | OpenAI GPT-5 Nano | OpenAI | Новейшая модель GPT-5 |
| `openai` | GPT-5 Nano (alias) | OpenAI | Псевдоним для gpt-5-nano |
| `openai-fast` | GPT-4.1 Nano | OpenAI | Быстрая версия GPT-4.1 |
| `mistral` | Mistral Small 3.1 24B | Mistral AI | Мощная французская модель |
| `nova-fast` | Amazon Nova Micro | Amazon | Быстрая модель от Amazon |
| `qwen-coder` | Qwen 2.5 Coder 32B | Alibaba | Специализированная модель для кода |

### 🔬 Специальные модели

| Код модели | Полное название | Провайдер | Описание |
|------------|-----------------|-----------|----------|
| `bidara` | BIDARA (NASA) | NASA | Биомиметический дизайн и исследования |
| `midijourney` | MIDIjourney | Различные | Генерация MIDI музыки |

---

## 💡 Продвинутые примеры использования

### 🌊 Потоковая генерация

```python
from akgpt import AKGPT

client = AKGPT()

prompt = "Расскажи увлекательную историю о космосе"
response = client.query(prompt, stream=True)

if hasattr(response, '__iter__'):
    print("Потоковый ответ:")
    for chunk in response:
        print(chunk, end='', flush=True)
else:
    print("Обычный ответ:", response)
```

### 🔐 Приватные запросы

```python
from akgpt import AKGPT

client = AKGPT()

# Приватный запрос не будет отображаться в публичной ленте
prompt = "Конфиденциальная информация о проекте"
result = client.query(prompt, private=True)

if result:
    print("Приватный ответ:", result)
```

### 📊 JSON ответы

```python
import json
from akgpt import AKGPT

client = AKGPT()

prompt = "Создай структурированные данные о планетах Солнечной системы"
result = client.query(prompt, json_response=True)

if result:
    print("JSON ответ:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
```

### 🧠 Использование системных промптов

```python
from akgpt import AKGPT

client = AKGPT()

prompts_and_systems = [
    ("Объясни квантовую физику", "Ты профессор физики"),
    ("Напиши код на Python", "Ты senior Python разработчик"),
    ("Придумай рецепт пиццы", "Ты шеф-повар итальянского ресторана")
]

for prompt, system in prompts_and_systems:
    result = client.query(prompt, system=system, model="mistral")
    print(f"Роль: {system}")
    print(f"Ответ: {result[:100]}...\n")
```

### 🎨 Творческая генерация с температурой

```python
from akgpt import AKGPT

client = AKGPT()

prompt = "Напиши стихотворение о программировании"

# Консервативная генерация (более предсказуемая)
conservative = client.query(prompt, temperature=0.2, model="gemini")

# Креативная генерация (более случайная)
creative = client.query(prompt, temperature=1.2, model="gemini")

print("Консервативное стихотворение:")
print(conservative)
print("\n" + "="*50 + "\n")
print("Креативное стихотворение:")
print(creative)
```

---

## 📸 Работа с изображениями

### Анализ изображения

```python
from akgpt import AKGPT
import base64

client = AKGPT()

# Загрузка и кодирование изображения
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Анализ изображения (только для модели openai)
image_base64 = encode_image_to_base64("path/to/your/image.jpg")
prompt = "Опиши что изображено на этой картинке"

result = client.query_with_image(
    prompt=prompt,
    image_base64=image_base64,
    model="openai",
    max_tokens=300
)

if result:
    print("Описание изображения:", result)
```

---

## 📋 Получение списка моделей

```python
from akgpt import AKGPT

client = AKGPT()

# Получить все доступные модели
models = client.get_available_models()
print(f"Доступно моделей: {len(models)}")

for i, model in enumerate(models, 1):
    print(f"{i}. {model}")

# Выбор модели для работы
selected_model = models[0]  # Первая доступная модель
result = client.query("Привет!", model=selected_model)
print(f"Ответ от модели {selected_model}: {result}")
```

---

## 🛠️ Полный интерактивный пример

```python
from akgpt import AKGPT

def interactive_ai_chat():
    client = AKGPT()
    
    print("🤖 Интерактивный чат с ИИ")
    print("Введите 'exit' для выхода")
    print("Введите 'models' для списка моделей")
    print("Введите 'help' для справки")
    
    current_model = "gemini"
    
    while True:
        user_input = input(f"\n[{current_model}] Вы: ").strip()
        
        if user_input.lower() == 'exit':
            print("👋 До свидания!")
            break
            
        elif user_input.lower() == 'models':
            models = client.get_available_models()
            print("Доступные модели:")
            for i, model in enumerate(models, 1):
                print(f"{i}. {model}")
            
            try:
                choice = int(input("Выберите номер модели: "))
                if 1 <= choice <= len(models):
                    current_model = models[choice-1]
                    print(f"Выбрана модель: {current_model}")
            except ValueError:
                print("Некорректный выбор")
            continue
            
        elif user_input.lower() == 'help':
            print("""
Команды:
- exit: выйти из чата
- models: показать доступные модели
- help: показать эту справку
            """)
            continue
            
        elif not user_input:
            continue
        
        try:
            # Генерация ответа
            response = client.query(
                prompt=user_input,
                model=current_model,
                temperature=0.7,
                max_tokens=200
            )
            
            print(f"🤖 ИИ: {response}")
            
        except Exception as e:
            print(f"❌ Ошибка: {e}")

# Запуск интерактивного чата
if __name__ == "__main__":
    interactive_ai_chat()
```

---

## ⚡ Оптимизация производительности

### Кэширование результатов

```python
from akgpt import AKGPT
from functools import lru_cache

class CachedAKGPT:
    def __init__(self):
        self.client = AKGPT()
    
    @lru_cache(maxsize=128)
    def cached_query(self, prompt, model="gemini", temperature=0.7):
        """Кэшированный запрос для повторяющихся промптов"""
        return self.client.query(
            prompt=prompt, 
            model=model, 
            temperature=temperature
        )

# Использование
cached_client = CachedAKGPT()

# Первый запрос - обращение к API
result1 = cached_client.cached_query("Что такое Python?")

# Второй запрос с теми же параметрами - из кэша
result2 = cached_client.cached_query("Что такое Python?")

print("Результат из кэша:", result1 == result2)
```

### Асинхронная обработка

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor
from akgpt import AKGPT

async def async_ai_requests():
    client = AKGPT()
    
    prompts = [
        "Расскажи про машинное обучение",
        "Что такое нейронные сети?",
        "Объясни глубокое обучение",
        "Что такое GPT модели?"
    ]
    
    # Асинхронное выполнение запросов
    with ThreadPoolExecutor(max_workers=4) as executor:
        loop = asyncio.get_event_loop()
        
        tasks = [
            loop.run_in_executor(executor, client.query, prompt)
            for prompt in prompts
        ]
        
        results = await asyncio.gather(*tasks)
        
        for prompt, result in zip(prompts, results):
            print(f"Вопрос: {prompt}")
            print(f"Ответ: {result[:100]}...\n")

# Запуск асинхронного примера
# asyncio.run(async_ai_requests())
```

---

## 🚨 Обработка ошибок

```python
from akgpt import AKGPT
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def robust_ai_query(prompt, max_retries=3):
    client = AKGPT()
    
    for attempt in range(max_retries):
        try:
            result = client.query(prompt, timeout=30)
            if result:
                return result
            else:
                logger.warning(f"Пустой ответ, попытка {attempt + 1}")
                
        except ConnectionError as e:
            logger.error(f"Ошибка соединения: {e}, попытка {attempt + 1}")
            
        except TimeoutError as e:
            logger.error(f"Таймаут: {e}, попытка {attempt + 1}")
            
        except Exception as e:
            logger.error(f"Неожиданная ошибка: {e}, попытка {attempt + 1}")
        
        if attempt < max_retries - 1:
            import time
            time.sleep(2 ** attempt)  # Экспоненциальная задержка
    
    return "Не удалось получить ответ после нескольких попыток"

# Использование
result = robust_ai_query("Расскажи про искусственный интеллект")
print(result)
```

---

## 📄 Лицензия

Эта библиотека распространяется под лицензией **MIT**. Подробности см. в файле [LICENSE](https://github.com/TETRIX8/akgpt/blob/main/LICENSE).

---

## 🙋‍♂️ Поддержка и сообщество

- 🐛 **Сообщить об ошибке**: [GitHub Issues](https://github.com/TETRIX8/akgpt/issues)
- 💡 **Предложить улучшение**: [GitHub Discussions](https://github.com/TETRIX8/akgpt/discussions)
- 📖 **Документация**: [GitHub README](https://github.com/TETRIX8/akgpt#readme)
- 📦 **PyPI пакет**: [akgpt на PyPI](https://pypi.org/project/akgpt/)

---

## 🏷️ Теги для поиска

```
#AI #ArtificialIntelligence #MachineLearning #NLP #Python #API #GPT #Gemini #Mistral #OpenAI #TextGeneration #ChatBot #LanguageModel #DeepLearning #MultiModal #Streaming #AsyncAI #PythonLibrary #SDK #APIClient #AITools #MLOps #DataScience #NeuralNetworks #Transformer
```

---

**AKGPT & FullAI** - Ваш мост к миру искусственного интеллекта! 🚀

---

🌟 **Создано с ❤️ командой [TETRIX8](https://github.com/TETRIX8)**
