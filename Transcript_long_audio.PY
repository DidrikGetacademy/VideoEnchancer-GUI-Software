from smolagents import TransformersModel,FinalAnswerTool,SpeechToTextTool,CodeAgent
from Agents_tools import ExtractAudioFromVideo,ReadTextFile
import torch
import gc
torch.cuda.empty_cache()
gc.collect()
model_path = r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\local_model\Qwen2.5-7B-Instruct-1M"
model = TransformersModel(
    model_id=model_path,
    load_in_8bit=True,
    device_map="cuda",
    max_new_tokens=1000, 
    trust_remote_code=True,
)
video_path = r"C:\Users\didri\AppData\Local\CapCut\Videos\A Process for Finding Purpose： Do THIS to Build the Life You Want ｜ Jay Shetty.mp4"
user_task = (
    "You have access to the video_path. First, extract the audio using ExtractAudioFromVideo. "
    "Then transcribe the audio using SpeechToTextTool — it will save the transcript to a .txt file. "
    "Next, read that transcript file. Then identify motivational quotes, wisdom, or inspirational messages spoken in the video. "
    "Avoid keyword-only checks — read the content fully. "
    "Provide the time frames (if available from transcript or estimate from chunking) and include the exact quotes or a summary of each inspiring moment. "
    "The goal is to create a list of time-based highlights for a motivational compilation video."
)

context_vars = {
               "video_path": video_path,
            }       

manager_agent  = CodeAgent(
            model=model,
        tools=[ExtractAudioFromVideo,ReadTextFile, SpeechToTextTool(),FinalAnswerTool()], 

            max_steps=15,
            verbosity_level=4,
            additional_authorized_imports=['datetime'],
            planning_interval=3,
        )

Response = manager_agent.run(
            task=user_task,
            additional_args=context_vars
        )
from rich.console import Console
manager_agent.logger.console = Console(file=open(r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\agent_tree.txt", "w"), force_terminal=True)
manager_agent.visualize()
del model



