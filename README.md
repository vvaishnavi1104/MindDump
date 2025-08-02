# 🧠 MindDump – A Distraction-Free Thought Organizer

MindDump is a simple, minimal web app that lets you quickly jot down thoughts, ideas, and tasks — then automatically tags and groups them using basic NLP logic. It’s designed for people who need a fast, clean mental inbox without the clutter of traditional note-taking apps.

---

## 🚀 Features

- 📝 Add quick thoughts or ideas
- 🧠 Auto-tagging using keyword-based logic
- 🗃️ Groups entries by tags like `Work`, `Urgent`, `Idea`, etc.
- 🔍 Search bar to filter notes in real-time
- 🕒 Timestamps for each entry
- 💾 Persistent storage using a simple JSON file
- 🎨 Clean, distraction-free interface

---

## 🛠️ Tech Stack

| Layer     | Technology        |
|-----------|-------------------|
| Frontend  | HTML, CSS         |
| Backend   | Python, Flask     |
| Storage   | JSON file         |
| NLP       | Rule-based keyword tagging (Python dictionary)

---

## 🧠 How Auto-Tagging Works

MindDump uses a simple keyword-to-tag mapping. For example:
- `"project"` → `Work`
- `"deadline"` → `Urgent`
- `"idea"` → `Idea`

If no keyword is matched, the entry is tagged as `General`.

---

## 📦 Setup Instructions

1. **Clone the repository**:
git clone https://github.com/vvaishnavi1104/MindDump.git
cd minddump

2. **Install dependencies**:

pip install flask

3. **Run the app**:

python app.py

4. **Open in your browser**:

http://localhost:5000
---

## ✅ Future Enhancements

* Export notes to Notion or Markdown
* User login and authentication
* SQLite or MongoDB for scalable storage
* Smarter NLP using spaCy or embeddings
* Mobile-friendly responsive design

---

## 📸 Screenshot

<img width="1660" height="715" alt="Screenshot 2025-08-02 234910" src="https://github.com/user-attachments/assets/ec5711a6-5cff-4c5a-b7a1-e5e7e4c29599" />



---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Vaishnavi V** – [GitHub](https://github.com/vvaishnavi1104)
Feel free to reach out if you'd like to collaborate or fork it for your own use!

```

