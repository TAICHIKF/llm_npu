import oneflow as flow
from transformers import AutoTokenizer
import numpy as np

# Step 1: Load the model with PyTorch and save weights as .npz format
import torch
from transformers import AutoModelForCausalLM

model_path = "/workspace/models/Qwen2.5-7B-Instruct"
torch_model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16)
torch.save(torch_model.state_dict(), "/workspace/models/qwen_weights.pth")

# Convert weights to numpy
model_weights = torch.load("/workspace/models/qwen_weights.pth", map_location="cpu")
np_weights = {k: v.cpu().numpy() for k, v in model_weights.items()}
np.savez("/workspace/models/qwen_weights.npz", **np_weights)

# Step 2: Load weights in OneFlow
class OneFlowQwenModel(flow.nn.Module):
    def __init__(self):
        super().__init__()
        # Define model layers similar to Qwen architecture
        # self.layer1 = ...
        
    def load_weights(self, np_weights):
        # Load weights layer-by-layer
        for name, param in self.named_parameters():
            if name in np_weights:
                param.copy_(flow.tensor(np_weights[name]))

    def forward(self, inputs):
        # Define forward pass based on Qwen architecture
        pass

# Initialize and load weights
model = OneFlowQwenModel()
np_weights = np.load("/workspace/models/qwen_weights.npz")
model.load_weights(np_weights)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Step 3: Prepare inputs and move model to NPU
model.to("cuda")  # Adjust to 'cuda' or other NPU compatible with OneFlow
prompt = "Give me a short introduction to large language models."
inputs = tokenizer(prompt, return_tensors="np")

# Convert inputs to OneFlow tensors
input_ids = flow.tensor(inputs["input_ids"]).to("cuda")

# Step 4: Run inference
with flow.no_grad():
    output = model(input_ids)
    # Process output...

# Decode response
response = tokenizer.decode(output, skip_special_tokens=True)
print(response)