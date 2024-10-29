pip install -U huggingface_hub -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install torch-npu -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install torch -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyyaml setuptools  -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install numpy attrs decorator psutil absl-py cloudpickle psutil scipy synr tornado -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install transformers -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install accelerate>=0.26.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install torch_npu -i https://pypi.tuna.tsinghua.edu.cn/simple

git submodule add  https://github.com/InternLM/lmdeploy.git  lmdeploy

