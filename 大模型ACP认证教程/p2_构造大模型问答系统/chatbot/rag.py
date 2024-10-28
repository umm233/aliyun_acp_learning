# 导入依赖
from llama_index.core import SimpleDirectoryReader,VectorStoreIndex,StorageContext,load_index_from_storage
from llama_index.embeddings.dashscope import DashScopeEmbedding,DashScopeTextEmbeddingModels
from llama_index.llms.dashscope import DashScope
# 这两行代码是用于消除 WARNING 警告信息，避免干扰阅读学习，生产环境中建议根据需要来设置日志级别
import logging
logging.basicConfig(level=logging.ERROR)

def indexing(document_path="./docs", persist_path="knowledge_base/test"):
    """
    建立索引
    参数
      path(str): 文档路径
    """
    # 解析 ./docs 目录下的所有文档
    documents = SimpleDirectoryReader(document_path).load_data()
    # 建立索引
    index = VectorStoreIndex.from_documents(
        documents,
        # 指定embedding 模型
        embed_model=DashScopeEmbedding(
            # 你也可以使用阿里云提供的其它embedding模型：https://help.aliyun.com/zh/model-studio/getting-started/models#3383780daf8hw
            model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V2
        ))
    # 持久化索引，将索引保存为本地文件
    index.storage_context.persist(persist_path)

def load_index(persist_path="knowledge_base/test"):
    """
    加载索引
    参数
      persist_path(str): 索引文件路径
    返回
      VectorStoreIndex: 索引对象
    """
    storage_context = StorageContext.from_defaults(persist_dir=persist_path)
    return load_index_from_storage(storage_context,embed_model=DashScopeEmbedding(
      model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V2
    ))

def create_query_engine(index):
    """
    创建查询引擎
    参数
      index(VectorStoreIndex): 索引对象
    返回
      QueryEngine: 查询引擎对象
    """
    query_engine = index.as_query_engine(
      streaming=True,
      llm=DashScope(model_name="qwen-plus")
    )
    return query_engine

def ask(question, query_engine):
    """
    向答疑机器人提问
    参数
      question(str): 问题
      query_engine(QueryEngine): 查询引擎对象
    返回
      str: 回答
    """
    streaming_response = query_engine.query(question)
    streaming_response.print_response_stream()



from llama_index.core import PromptTemplate
def update_prompt_template(
        query_engine,
        qa_prompt_tmpl_str = (
        "你要简短地回答问题。以下是参考信息"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "比如学员问xx功能的工具是什么，你只需要回复：工具是："
        "不要说其它的话。"
        "学员的提问是: {query_str}\n。"
        "你的回答是: "
    )):
    """
    修改prompt模板
    输入是prompt修改前的query_engine，以及提示词模板；输出是prompt修改后的query_engine
    """
    qa_prompt_tmpl_str = qa_prompt_tmpl_str
    qa_prompt_tmpl = PromptTemplate(qa_prompt_tmpl_str)
    query_engine.update_prompts(
        {"response_synthesizer:text_qa_template": qa_prompt_tmpl}
    )
    print("提示词模板修改成功")
    return query_engine
