import os

# 下载模型
os.system('huggingface-cli download --resume-download internlm/internlm2_5-7b-chat --local-dir /workspace/model')
# os.system('huggingface-cli download --resume-download Qwen/Qwen2.5-7B-Instruct --local-dir /workspace/models/qwen')