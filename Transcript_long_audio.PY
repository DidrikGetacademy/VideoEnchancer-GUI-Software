from smolagents import TransformersModel,FinalAnswerTool,SpeechToTextTool,CodeAgent
from Agents_tools import ExtractAudioFromVideo, SaveMotivationalQuote, ChunkLimiterTool
import torch
import os
import gc
import yaml
from rich.console import Console
torch.cuda.empty_cache()
gc.collect()
model_path = r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\local_model\Qwen2.5-7B-Instruct-1M"


model = TransformersModel(
    model_id=model_path,
    load_in_8bit=True,
    device_map="cuda",
    max_new_tokens=2500, 
    trust_remote_code=True,
)


#model_path_assistant = r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\local_model\Phi-4-reasoning-plus"
# model_assistant_agent= TransformersModel(
#     model_id=model_path_assistant,
#         load_in_8bit=True,
#         device_map="cuda",
#         max_new_tokens=3000, 
# )


# video_path = r"c:\Users\didri\AppData\Local\CapCut\Videos\A Process for Finding Purpose： Do THIS to Build the Life You Want ｜ Jay Shetty.mp4"
video_path = r"c:\Users\didri\AppData\Local\CapCut\Videos\A Process for Finding Purpose： Do THIS to Build the Life You Want ｜ Jay Shetty.mp4"

text_file = r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\ManagedAgent_Storage.txt"




prompt_template = r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\Assets\agent_prompts\videotext_prompt.yaml"
loaded_reasoning_agent_prompts = r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\Assets\agent_prompts\loaded_reasoning_agent_prompts.yaml"
with open(prompt_template, 'r', encoding='utf-8') as f:
    loaded_prompt_templates = yaml.safe_load(f)
with open(loaded_reasoning_agent_prompts, 'r', encoding='utf-8') as f:
    loaded_reasoning_agent_prompts = yaml.safe_load(f)


Reasoning_Text_Agent = CodeAgent(
        name="ReasoningAgent",
        model=model,
        description=(
        "An agent that processes transcript chunks one at a time, reasoning through each to identify motivational quotes, deep insights, wisdom, or inspiring and meaningful content in the text.",
        " If such content is found, it execute the `SaveMotivationalQuote` Tool and stores the text/quote it found and the correct timestamp in the `text_file` variable that the manager agent has access to and must provide to the ReasoningAgent."
        "which invokes the SaveMotivationalQuote tool to record it. If no relevant content is detected, the chunk is ignored."
        ),
        tools=[SaveMotivationalQuote,FinalAnswerTool()],
        max_steps=25,
        prompt_templates=loaded_reasoning_agent_prompts  

)


manager_agent  = CodeAgent(
            model=model,
            tools=[ExtractAudioFromVideo,ChunkLimiterTool(), SpeechToTextTool(),FinalAnswerTool()], 
            max_steps=25,
            verbosity_level=4,
            #planning_interval=3,
            prompt_templates=loaded_prompt_templates,
            managed_agents=[Reasoning_Text_Agent]
        )


user_task = (
    "YOU MUST Follow these steps to achieve the user task.\n\n"
    
    "1. You have access to the variable `video_path`. First, extract the audio using the `ExtractAudioFromVideo` tool.\n\n"

    "2. Transcribe the audio using the `transcriber` tool (an instance of `SpeechToTextTool`) by providing the path returned from the `ExtractAudioFromVideo` tool.\n"
    "Note: The transcriber (`SpeechToTextTool`) will return the path to a `.txt` file containing the full transcript of the audio. Store this path in the variable `Full_transcript_path`.\n\n"

    "3. Retrieve a chunk of the transcript by calling the `chunk_limiter` tool and passing in variable `Full_transcript_path` and a `max_chars` value (e.g., 1000).\n"
    "Note: This tool returns one small portion of the transcript at a time. It does not return the full transcript. Choose a chunk size that allows for safe reasoning (e.g., 1000 characters).\n"

    "4. Pass the current chunk to the managed agent `ReasoningAgent` by calling it as:\n"
    " `ReasoningAgent.run(task=chunk, additional_args={\"text_file\: text_file})`\n"
    "This agent will reason through the chunk and extract any motivational or inspirational quotes. Refer to its description for details on behavior and tool usage.\n"
    "Wait for the response from `ReasoningAgent` before proceeding to the next chunk.\n\n"

    "5.Repeat the process: retrieve a chunk using `chunk_limiter`, send it to `ReasoningAgent`, wait for the response, and only then retrieve the next chunk.\n"
    "IMPORTANT: You must call `chunk_limiter` **one time per cycle** and wait for the reasoning agent to finish before calling it again.\n\n"
    "Repeat the following loop:\n"
        "   - Retrieve the next chunk using `chunk_limiter`.\n"
        "   - Pass the chunk to `ReasoningAgent` and wait for its response.\n"
        "   - Continue this loop until `chunk_limiter` returns an empty string.\n"
        "   - Once the full transcript is processed and `chunk_limiter` returns an empty string, provide the final answer.\n\n"

    "Remember: Stop this loop when `chunk_limiter` returns an empty string. This indicates that the full transcript has been processed.\n\n"
    "IMPORTANT:\n"
        "- You must call `chunk_limiter` **only once per cycle**, and only after `ReasoningAgent` completes processing the previous chunk.\n"
        "- DO NOT use code like `while chunk != \"\"` — this is incorrect and will break the task flow.\n"
        "- Always explicitly call `chunk_limiter` only after `ReasoningAgent` has finished."
)
Response = manager_agent.run(
            task=user_task,
            additional_args = {
                 "video_path": video_path,
                 "text_file" : text_file,
                 "Full_transcript_path": None
            }       
        )

with open(r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\Agent_logging.txt", "w") as f:
    manager_agent.logger.console = Console(file=f, force_terminal=True)
    manager_agent.visualize()
manager_agent.visualize()
del model


###huske liste imorgen
####Jeg må fokusere på å gjøre system prompt for begge agentene så verdifull og liten så mye så jeg ikke bruker opp context token/vinduet på modellen