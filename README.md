# 🦄 LLM Testing

<div align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3vC-Ix8vbvgJRI1MUlgpXx7DhqhYn0wNQJw&s">

This repository has the purpose of learning and pratice LLM Testing.  
 The tests were developed using the **[Deepeval](https://github.com/confident-ai/deepeval)** framework.

</div>

## 📋 Pre-requirements

- [Python 3.x](https://www.python.org/downloads/) (I've used version `3.11.2` while making this project)
- [Ollama](https://ollama.com/) (Optional)

## 🦙 Ollama

For fast deploy of an LLM, I've used [Ollama](https://ollama.com/) to run pre-builds LLMs.

The tests were performed in the [qwen2 1.5B](https://ollama.com/library/qwen2:1.5b) LLM.

```bash
ollama run qwen2:1.5b
```

## 🌲 Virtual Environment

Run `python -m venv envname` to make a new virtual environment, e.g.:

```bash
python -m venv venv
```

### Active the environment:

- Windows

```bash
bugbank\Scripts\activate
```

- Linux/MacOs

```bash
source bugbank/bin/activate
```

## 🏗️ Installation

Install all the requirements

```bash
pip install -r requirements.txt
```

## ✔️ Running the tests

To run the tests make sure you are in the root folder of the project and type in the terminal

```bash
deepeval test run tests
```

## Support this project 🙌

If you want to support this project, leave a ⭐.

---

Made with ❤️ by [Rodrigo Molter](https://www.linkedin.com/in/rodrigo-molter/).
