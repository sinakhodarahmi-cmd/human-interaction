# human-interaction
# Sentiment-Aware Human-AI Interaction Framework 🧠🤖

## 📌 Project Overview
This research project explores the intersection of **Human-Computer Interaction (HCI)** and **Affective Computing**. The goal is to develop a framework where an AI agent dynamically modulates its communicative persona based on the real-time emotional state of the user, thereby reducing cognitive dissonance and enhancing empathetic engagement.

## 🚀 Core Objective
To move beyond static AI responses by implementing a **Closed-Loop Feedback System** that maps user sentiment (Polarity) to specific LLM System Prompts.

## 🛠️ Technical Stack
- **Language:** Python 3.x
- **NLP Engine:** TextBlob (for Sentiment Quantization)
- **Generative Engine:** OpenAI GPT-4 / GPT-3.5 Turbo
- **Paradigm:** Prompt Engineering & Persona Modulation

## 🏗️ System Architecture
The framework operates through a three-tier pipeline:

1.  **Perceptual Layer:** Analygetical processing of user text to derive a `Polarity Score` ($\in [-1, 1]$).
2.  **Mapping Module:** A heuristic engine that translates numerical sentiment into a discrete `Instructional Persona`.
3.  **Generative Layer:** A dual-input injection process where the LLM receives both the user query and the empathetic constraints.

> *[Insert your Architecture Diagram here]*

## 💻 Implementation (Core Logic)
```python
# Core snippet demonstrating the Persona Mapping logic
def map_persona(polarity):
if polarity > 0.3:
return "Enthusiastic and High-Energy Persona"
elif polarity < -0.3:
return "Empathetic and Soothing Persona"
else:
return "Professional and Neutral Persona"
