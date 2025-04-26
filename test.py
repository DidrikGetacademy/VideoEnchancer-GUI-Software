from vllm import LLM

def test_vllm_flashattn():
    print("🚀 Starting VLLM + Flash-Attn Test...")

    # Load a tiny model for testing
    model = LLM(model="facebook/opt-125m", dtype="float16")

    # Generate text
    outputs = model.generate(["Hello, how are you today?"])

    for output in outputs:
        print("🧠 Model output:", output.outputs[0].text)

if __name__ == "__main__":
    test_vllm_flashattn()
