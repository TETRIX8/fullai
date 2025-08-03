# 🚀 FullAI - Полная документация ИИ моделей

Современный API Gateway для доступа к передовым моделям искусственного интеллекта с красивой документацией и интерактивными примерами.

## 🌟 Основные возможности

- **12+ ИИ моделей** - от текстовых до мультимодальных и аудио
- **Красивая документация** - полное описание всех моделей и примеров
- **Интерактивное тестирование** - попробуйте API прямо в браузере
- **Серверная обработка** - все запросы обрабатываются на Vercel
- **Высокая производительность** - кэширование и оптимизация
- **CORS поддержка** - для интеграции с любыми приложениями

## 🏠 Демо

- **Главная страница**: https://fullai.vercel.app
- **Интерактивные примеры**: https://fullai.vercel.app/examples.html
- **API Endpoints**: https://fullai.vercel.app/models
- **Статус сервиса**: https://fullai.vercel.app/api/status

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
https://fullai.vercel.app
```

### Получить список моделей
```bash
GET /models
```

**Пример:**
```bash
curl -X GET "https://fullai.vercel.app/models" \
  -H "Content-Type: application/json"
```

### Отправить запрос к модели
```bash
POST /chat
```

**Пример:**
```bash
curl -X POST "https://fullai.vercel.app/chat" \
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

Формат: `https://fullai.vercel.app/{запрос}?model={модель}&voice={голос}`

**Примеры:**

1. **Текстовый запрос:**
   ```
   https://fullai.vercel.app/Напиши%20статью%20об%20ИИ?model=deepseek
   ```

2. **Запрос с изображением:**
   ```
   https://fullai.vercel.app/Опиши%20изображение:https://example.com/image.jpg?model=mistral
   ```

3. **Аудио запрос:**
   ```
   https://fullai.vercel.app/Прочитай%20новости?model=openai-audio&voice=nova
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

### 4. Деплой на Vercel
```bash
vercel --prod
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
├── vercel.json             # Конфигурация Vercel
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

### Настройки Vercel
- **Runtime**: Python 3.9
- **Max Lambda Size**: 15MB
- **Max Duration**: 30 секунд
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
- **CDN** - глобальное распространение через Vercel

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции
3. Внесите изменения
4. Создайте Pull Request

## 📄 Лицензия

MIT License - см. файл LICENSE для деталей.

## 📞 Поддержка

- **Документация**: https://fullai.vercel.app
- **Примеры**: https://fullai.vercel.app/examples.html
- **API**: https://fullai.vercel.app/models
- **Статус**: https://fullai.vercel.app/api/status

---

**FullAI** - Ваш мост к миру искусственного интеллекта! 🚀
