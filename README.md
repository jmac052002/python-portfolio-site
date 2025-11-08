# Python Portfolio Site

A simple Flask-based personal website to showcase my AWS, DevOps, and Python projects. Built to be pushed to GitHub and shown to recruiters as part of my portfolio.

## 📌 Overview

This app is a small Flask web app with:
- A **Home** page with intro + skills
- A **Projects** page that loops over Python data
- A **Contact** page with links
- Shared layout using Jinja templates
- Basic styling via `/static/style.css`

It’s meant to be simple, readable, and easy to extend (add pages like `/aws`, `/certs`, `/blog`, etc.).

---

## 🏗 Project Structure

```text
python-portfolio-site/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── projects.html
│   └── contact.html
└── static/
    └── style.css
