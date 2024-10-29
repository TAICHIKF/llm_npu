import os
os.environ['DATA_DOWNLOAD_METHOD'] = '<your_download_method>'

from c2net.context import prepare
#初始化导入数据集和预训练模型到容器内
c2net_context = prepare()
#获取预训练模型路径
internlm2_5_7b_chat_path = c2net_context.pretrain_model_path+"/"+"internlm2_5-7b-chat"
#输出结果必须保存在该目录
you_should_save_here = c2net_context.output_path