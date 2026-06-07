# Multi-State Reasoning Business Planner with LangChain

A Python-based automation tool that utilizes LangChain and OpenAI's GPT models to generate a comprehensive business plan through **Multi-State Reasoning**. Instead of asking the LLM to write a plan in a single prompt, this project breaks the task into specialized sequential steps, passing the structural state and context from one step to the next to minimize hallucination and enhance accuracy.

---

## 🚀 How It Works (Multi-State Pipeline)

The workflow executes sequentially, simulating a team of specialized business consultants:

1. **Market Analysis:** Analyzes coffee culture, high-traffic zones, and preferences in Baku.
2. **Competitor Analysis:** Identifies main local/chain rivals based on the market profile.
3. **Cost Estimation:** Details setup, legal, equipment, and operational overheads.
4. **Revenue Forecast:** Models realistic pricing strategies and monthly profit projections.
5. **Risk Analysis:** Highlights legal, economic, and cultural risks in Azerbaijan.
6. **Final Business Plan Integration:** Compiles all the structured output states into a cohesive, production-ready Business Plan document.

---

## 🛠️ Features

* **LangChain Expression Language (LCEL):** Implements modern LangChain architecture using the `|` operator and `.invoke()` methods.
* **Context Preservation:** Each logic state feeds directly into dependent future states, maintaining a clean data lineage.
* **Modular Architecture:** Easily add, remove, or swap reasoning steps (e.g., adding a Marketing Strategy state).

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/forestboy1110/multi-state-business-planner.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
