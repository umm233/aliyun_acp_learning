from llama_index.embeddings.dashscope import DashScopeEmbedding, DashScopeTextEmbeddingModels
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.dashscope import DashScope
from llama_index.core.node_parser import SimpleFileNodeParser
from llama_index.core.response.notebook_utils import display_source_node

def process_and_query(query):
    # 加载文档
    documents = SimpleDirectoryReader(input_files=["./docs/内容开发工程师岗位指导说明书.pdf"]).load_data()
    
    # 将文档转为节点(切片/Chunk)
    parser = SimpleFileNodeParser()
    nodes = parser.get_nodes_from_documents(documents)
    
    # 创建向量存储索引
    index = VectorStoreIndex(nodes,
                             embed_model=DashScopeEmbedding(model_name=DashScopeTextEmbeddingModels.TEXT_EMBEDDING_V2))
    
    # 构建查询引擎
    query_engine = index.as_query_engine(streaming=True, llm=DashScope(model_name="qwen-plus"))
    
    # 执行查询
    response = query_engine.query(query)
    print("回答是：")
    response.print_response_stream()
    return response


def get_retrieved_nodes(response):
    print("\n")
    for i in range(len(response.source_nodes)):
        print("="*100)
        source_node = response.source_nodes[i]
        display_source_node(source_node=source_node, source_length=3000)





