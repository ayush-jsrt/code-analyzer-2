from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama

# Define the request format
class Prompt(BaseModel):
    prompt: str

app = FastAPI()

# Load the model on startup
@app.on_event("startup")
async def load_model():
    # Initialize the Llama model with the GGUF file
    app.state.llm = Llama(model_path="/models/starcoder2-3b-Q4_K_S.gguf")

# Define the generation endpoint
@app.post("/generate")
def generate_text(data: Prompt):
    # Call the model to generate text. Adjust max_tokens and stop tokens as needed.
    output = app.state.llm(
        data.prompt,
        max_tokens=64,
        stop=["\n"]
    )
    # Return the generated text from the first choice
    return {"generated_text": output["choices"][0]["text"]}