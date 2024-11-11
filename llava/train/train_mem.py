from llava.train.train import train
import os
os.environ['HF_HOME'] = '/mnt/NVME-VM/projects/cache'
if __name__ == "__main__":
    train(attn_implementation="flash_attention_2")
