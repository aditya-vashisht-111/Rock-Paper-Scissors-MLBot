# Rock Paper Scissors — Adaptive AI Agent

Intelligent Rock Paper Scissors agent implementing pattern recognition and n-gram prediction to counter multiple deterministic opponents. Developed as part of the freeCodeCamp Machine Learning curriculum.

---

## 🧠 Strategy Overview

Most traditional RPS implementations rely on randomness.  
This agent instead applies lightweight predictive modeling:

### **1. Opponent Modeling**
The bot logs opponent sequences to build a statistical profile of preferred transitions.

### **2. N-Gram Prediction**
A 5-gram frequency model is used to estimate the opponent’s next likely move based on recent history.

### **3. Counterplay**
The predicted move is countered immediately (`R → P`, `P → S`, `S → R`) to maximize win probability.

This approach proves effective against:

✔ **Cycle-based strategies**  
✔ **Pattern repetition**  
✔ **Mirror/counter strategies**  
✔ **Frequency-driven bots**

---

## 🏁 Challenge Requirements

To pass the original freeCodeCamp evaluation, the bot must consistently achieve:

> **≥ 60% win rate vs each opponent over 1000+ iterations**

This implementation surpasses the criteria, especially against highly deterministic opponents such as Quincy, Kris, and Mrugesh.

---

## 📦 Running Locally

Clone the project:

```bash
git clone <your_repo_url>
cd <project_folder>
