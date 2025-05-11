from smolagents import TransformersModel,CodeAgent,DuckDuckGoSearchTool,FinalAnswerTool
import yaml
Model = TransformersModel(
    model_id = r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\AI-onnx\phi4_models\cuda\gpu-int4-rtn-block-32",
    max_new_tokens=2500

)
prompt_template = r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\Assets\agent_prompts\prompts.yaml"
with open(prompt_template, 'r', encoding='utf-8') as f:
        manager_prompt = yaml.safe_load(f)

agent = CodeAgent(
    model = Model,
    tools=[FinalAnswerTool(),DuckDuckGoSearchTool()],
    prompt_templates= manager_prompt,
    max_steps=30,


)

agent.run(task="Tell me your name!")