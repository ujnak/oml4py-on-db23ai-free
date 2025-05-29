import oml
from oml.utils import ONNXPipeline, ONNXPipelineConfig
ONNXPipelineConfig.show_preconfigured()
ONNXPipelineConfig.show_templates()
pipeline = ONNXPipeline(model_name="sentence-transformers/all-MiniLM-L6-v2")
pipeline.export2file("all-MiniLM-L6-v2",output_dir="./work")
