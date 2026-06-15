from openai import OpenAI

# Point the OpenAI client at your LOCAL Ollama server instead of the cloud.
# This is the whole insight of the lab: "calling an LLM" is just an HTTP
# request to an inference server — wherever that server happens to run.
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

MODEL = "llama3.2:3b"


def main() -> None:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a concise assistant."},
            {"role": "user", "content": "In one sentence, what is an inference engine?"},
        ],
    )
    print(response.choices[0].message.content)

    # Reflection on "the same shape":
    # This call is identical in shape to a hosted API call because both rely on the 
    # standardized OpenAI HTTP/JSON protocol. Whether the base_url points to a 
    # remote cloud provider (like Gemini) or a local machine (localhost:11434), 
    # the client library sends the exact same POST request structure, 
    # proving that the model's physical location is just a configuration detail.

if __name__ == "__main__":
    main()