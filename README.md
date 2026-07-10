# 🚀 GrowEasy AI CSV Importer — Full-Stack AI Data Pipeline

[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js&logoColor=white)](https://nextjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue?logo=typescript&logoColor=white)](https://www.typescriptlang.org)
[![Node.js](https://img.shields.io/badge/Node.js-20-green?logo=node.js&logoColor=white)](https://nodejs.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker&logoColor=white)](https://docker.com)
[![Gemini](https://img.shields.io/badge/AI-Google_Gemini-orange?logo=google&logoColor=white)](https://ai.google.dev)
[![Tailwind](https://img.shields.io/badge/Tailwind_CSS-v4-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com)

---

# 📌 Project Overview

A **production-grade, full-stack application** designed to seamlessly extract, validate, and map unstructured CRM lead data into a strict database schema using Large Language Models. This project demonstrates the ability to build intelligent systems and scalable AI solutions that create real-world impact and drive innovation.

> **Business Value:** Solves the classic problem of messy, unpredictable user data. Instead of relying on brittle Regular Expressions, it leverages AI to intelligently read raw CSV rows, accurately identify overflow data, enforce strict formatting, and output clean JSON ready for CRM database insertion.

---

# 🏗️ System Architecture

```text
Messy CSV File (Raw Data)
        │
        ▼
┌──────────────────────────────┐
│  Next.js UI (Drag & Drop)    │ ──► File ingestion & user interaction
└──────────────────────────────┘
        │
        ▼
┌──────────────────────────────┐
│ Node.js Backend (app.ts)     │ ──► Receives file via Multer middleware
└──────────────────────────────┘
        │
        ▼
┌──────────────────────────────┐
│  Data Parsing (PapaParse)    │ ──► Converts CSV text to iterable arrays
└──────────────────────────────┘
        │
        ▼
┌──────────────────────────────┐
│   Gemini AI Service          │ ──► Fuzzy matching & strict schema extraction
└──────────────────────────────┘
        │
        ▼
┌──────────────────────────────┐
│ Validation & Formatting      │ ──► Applies "-" fallbacks and strict JSON formatting
└──────────────────────────────┘
        │
        ▼
┌──────────────────────────────┐
│ Next.js Virtualized Table    │ ──► Renders 1000s of rows without DOM lag
└──────────────────────────────┘
```

---

# 🔧 Tech Stack

| Layer | Technology |
|--------|------------|
| **Frontend Framework** | Next.js (App Router), React, TypeScript |
| **Styling & Theming** | Tailwind CSS v4, next-themes (Dark Mode) |
| **UI Optimization** | @tanstack/react-virtual |
| **Backend Framework** | Node.js, Express, TypeScript |
| **File Processing** | Multer, PapaParse |
| **AI Engine** | Google Generative AI (gemini-2.5-flash) |
| **Containerization** | Docker, Docker Compose |
| **Architecture** | Strict OOP (Controllers, Services, Interfaces) |

---

# 🚀 Key Features & Engineering Decisions

## ✅ AI-Powered Data Extraction

Uses advanced prompt engineering to fuzzy-match columns, extract names/dates, and intelligently consolidate multiple phone numbers or emails into a `crm_note` overflow field.

---

## ✅ Virtualized Data Tables

Employs **@tanstack/react-virtual** on the frontend to calculate absolute positioning for rows. This allows the application to render massive CSV previews without freezing the browser DOM, ensuring smooth scrolling.

---

## ✅ Strict Schema Validation

Enforces constrained outputs for specific CRM statuses (e.g., `GOOD_LEAD_FOLLOW_UP`) and data sources (e.g., `meridian_tower`).

Automatically skips records that lack both a valid email and phone number to preserve database integrity.

---

## ✅ Smart Batching & Error Handling

Processes large CSVs in manageable chunks, strips out markdown formatting, and catches AI parsing errors to ensure pure, usable JSON is always returned to the client.

---

## ✅ Production-Ready UI

Features a fully responsive drag-and-drop interface with a seamless Dark/Light mode toggle, utilizing Tailwind CSS v4's modern utility classes and CSS variables.

---

# 📂 Project Structure

```text
ai-csv-parser/
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx
│   │   │   ├── layout.tsx
│   │   │   └── globals.css
│   │   │
│   │   └── components/
│   │       ├── ResultTable.tsx
│   │       └── TablePreview.tsx
│   │
│   ├── Dockerfile
│   └── tailwind.config.ts
│
├── backend/
│   ├── src/
│   │   ├── controllers/
│   │   ├── services/
│   │   │   ├── GeminiAiService.ts
│   │   │   └── LeadProcessor.ts
│   │   ├── routes/
│   │   └── index.ts
│   │
│   ├── Dockerfile
│   └── .env
│
├── docker-compose.yml
└── README.md
```

---

# ⚙️ Local Setup (Dockerized)

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-csv-parser.git

cd ai-csv-parser
```

---

## 2. Set Environment Variables

Create a `.env` file inside the backend directory.

```bash
cd backend

touch .env
```

Add the following:

```env
PORT=5000
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 3. Build & Run Containers

```bash
cd ..

docker compose up --build
```

---

## 4. Launch the Application

**Frontend**

```text
http://localhost:3000
```

**Backend**

```text
http://localhost:5000
```

---

# 🧪 Testing the Pipeline

### Upload Data

Drag and drop a raw CSV file onto the web interface.

### Preview

Review the parsed table data.

### Extract

Click to send the data to the backend `/api/upload` endpoint.

### Verify

Inspect the final virtualized table to confirm the AI correctly mapped fields like Source, formatted dates, and aggregated overflow data into the Notes column.

---

# 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/upload` | `POST` | Accepts multipart/form-data (CSV file), parses, batches, AI-extracts, and returns mapped CRM JSON records. |

---

# 🧠 AI Pipeline Details

### Constrained Outputs

The system prompt strictly forces Gemini to choose from a predefined list of allowed CRM statuses and source projects. If no valid match exists, it safely falls back to a blank string (displayed as `-` on the frontend).

---

### Data Preservation

The AI captures the primary email and phone number for indexing while preserving additional contact information and miscellaneous comments inside the `crm_note` field, ensuring no valuable data is lost.

---

### Date Formatting

Normalizes inconsistent date formats such as:

- `Yesterday`
- `12th May`
- `May 12`
- `12/05/2025`

into standardized **YYYY-MM-DD** ISO-compatible strings.

---

# 🌱 What This Project Demonstrates

| Skill Area | Demonstrated By |
|------------|-----------------|
| **Full-Stack Engineering** | Seamless integration between a Next.js frontend and a Node.js REST API |
| **AI Integration** | Practical application of LLMs for intelligent data transformation instead of RegEx |
| **Frontend Performance** | Windowing and virtualization for rendering massive datasets efficiently |
| **DevOps & Infrastructure** | Dockerized multi-container architecture with Docker Compose |
| **Industry Readiness** | Clean architecture, production-ready UI, error handling, and scalable design |

---

# 📄 License

This project is licensed under the **MIT License**.

---

## 💡 Highlights

- 🤖 AI-powered CRM data extraction
- 📦 Dockerized full-stack architecture
- ⚡ Virtualized rendering for large datasets
- 🎯 Strict schema validation
- 🧠 Intelligent prompt engineering
- 🌙 Dark/Light theme support
- 📁 Drag-and-drop CSV uploads
- 🛡️ Robust error handling
- 🚀 Production-ready architecture
- 📈 Scalable AI data processing pipeline

---

> **Built to production standards — demonstrating scalable AI-powered data processing, modern full-stack engineering, and intelligent automation.**
