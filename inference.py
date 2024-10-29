from lmdeploy import pipeline 
from lmdeploy import Pytorch

if name == "__main__":
    pipe = pipeline("/workspace/pretrainmodel/internlm2_5-7b-chat",                   
    backend_config = PytorchEngineConfig(tp=1, device_type="ascend"))   
    question = ["Shanghai is", "Please introduce China", "How are you?"]    
    response = pipe(question)   
    print(response)