# Telegram-E-commerce-Data-Extractor

This week’s objective is to collect and label real-world Amharic-language e-commerce posts from Telegram, with the goal of training a Named Entity Recognition (NER) model for product, price, and location extraction.

---

### ✅ Task 1: Data Ingestion & Preprocessing

- Used Telethon to scrape messages from 5 Amharic Telegram vendor channels.
- Pagination implemented via offset_id to collect up to 2,000 messages per channel.
- Each message includes:
  - Channel Title
  - Channel Username
  - Message ID
  - Message Text
  - Date
  - Media Path (or "N/A")
- Text encoded in UTF-8 to preserve Amharic characters.
- Output stored in: `data/raw/telegram_messages.csv`

📂 Example entry:

| Channel Title | Channel Username | Message Text |
|---------------|------------------|------------------------------|
| Shager Store  | @shageronlinestore | አዲስ iPhone 14 Pro Max፡ 130000 ብር። አዲስ አበባ። |

---

### ✅ Task 2: Manual NER Labeling (CoNLL Format)

- Manually labeled 50 sample messages using a 6-tag NER scheme:
  - B-Product, I-Product
  - B-PRICE, I-PRICE
  - B-LOC, I-LOC
  - O (non-entity)
- Labels created in Python using a token-label list and saved in CoNLL format.
- Blank lines separate sentences.

📄 Example snippet:

iPhone B-Product
14 I-Product
Pro I-Product
130000 B-PRICE
ብር I-PRICE
አዲስ B-LOC
አበባ I-LOC


- Output file: `data/labeled/labeled_data.txt`

---

### 🔜 Next Step: Fine-tuning NER models (Task 3)

Coming up: Load labeled data, tokenize, and fine-tune multilingual transformer models for Amharic NER.

