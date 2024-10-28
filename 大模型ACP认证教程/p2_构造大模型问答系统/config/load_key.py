import os
import getpass
import dashscope
from dashscope.common.api_key import get_default_api_key
def load_key():
    api_key = get_default_api_key()
    if api_key is not None and api_key.startswith("sk-"):
        os.environ['DASHSCOPE_API_KEY'] = api_key
        return
    api_key = getpass.getpass("请输入你的api_key:")
    dashscope.save_api_key(api_key)
    os.environ['DASHSCOPE_API_KEY'] = api_key

if __name__ == '__main__':
    load_key()
    import os
    print(os.environ['DASHSCOPE_API_KEY'])
