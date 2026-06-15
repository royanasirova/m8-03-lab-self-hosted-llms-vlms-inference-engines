# Self-Hosting Benchmark Report

## Task 1 — Benchmark Two Local Models

| Model Name | Approximate Size / Quantization | Load Time / Speed | Approximate RAM Used | Subjective Quality Note |
| :--- | :--- | :--- | :--- | :--- |
| **Qwen 2.5 (0.5B)** | ~397 MB / Q4_K_M | Instant load / Lightning fast | System stayed around 10.8 GB | Very fast, but the analogy was messy, confusing, and scientifically inaccurate. |
| **Llama 3.2 (3B)** | ~2.0 GB / Q4_K_M | Brief pause to load / Good speed | System stayed around 10.7 GB (Ollama swapped models) | Noticeably smarter. Understood the concept of lingering heat much better, though the campfire analogy wasn't perfect. |

### Trade-off Observation
The smaller model (Qwen 0.5B) is incredibly lightweight and runs instantly without straining the computer's memory, making it ideal for low-resource hardware or simple automation tasks. However, it sacrifices reasoning capacity and coherence. The larger model (Llama 3.2 3B) requires significantly more memory and storage, but provides a vastly superior, more logical, and highly usable response.

## Task 3 — VLM: local vs hosted

Image used: `sample_chart.png`

Task performed: Chart Description and Visual Question Answering (VQA).

| System | Answer (short) | Speed | Cost |
|--------|----------------|-------|------|
| Local VLM (moondream) | Described a 4-bar chart displaying model inference speeds with different colors, but failed to read any specific text or data values. | Fast local generation; skipped network overhead but had a minor load time. | free / local |
| Gemini (multimodal)   | Perfectly extracted the title "Inference Speed by Model", all four model names, their exact throughput speeds (e.g., Qwen at 98 tok/s), and deduced the overall size vs. speed trend. | Blazing fast text generation streaming, though subject to minimal network request delay. | free tier |

**Comparison (2–3 sentences):**

> The local VLM kept up beautifully when identifying visual structures, spatial layouts, and basic bar colors without needing an internet connection or incurring cloud costs. However, it visibly fell short on optical character recognition (OCR) and grounded reasoning, where Gemini completely outperformed it by reading the precise axis text and extracting exact analytical data points.