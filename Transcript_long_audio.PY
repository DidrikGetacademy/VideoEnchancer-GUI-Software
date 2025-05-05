from smolagents import TransformersModel,FinalAnswerTool,SpeechToTextTool,CodeAgent
from Agents_tools import ExtractAudioFromVideo,Proccess_transcript_in_chunks,SaveMotivationalQuote
import torch
import gc
torch.cuda.empty_cache()
gc.collect()
model_path = r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\local_model\Qwen2.5-7B-Instruct-1M"
model = TransformersModel(
    model_id=model_path,
    load_in_8bit=True,
    device_map="cuda",
    max_new_tokens=3000, 
    trust_remote_code=True,
)
video_path = r"c:\Users\didri\AppData\Local\CapCut\Videos\A Process for Finding Purpose： Do THIS to Build the Life You Want ｜ Jay Shetty.mp4"
text_file = r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\Motivational_sentence.txt"
user_task = (
    "You have access to the variable `video_path`. First, extract the audio using the `ExtractAudioFromVideo` tool. "
    "Then, transcribe the audio using the `transcriber` tool (an instance of `SpeechToTextTool`) by providing the path returned from the `ExtractAudioFromVideo` tool. "
    "This tool will return the path to a `.txt` file containing the transcript. "
    
    "Next, when the Whisper model has returned the `.txt` file path, read the transcript using the `Proccess_transcript_in_chunks` tool by providing that path as `file_path`. DO not run the speectotool text again when its already been run. "
    "This tool returns a small chunk of the transcript at a time. Use a chunk size of at least 1000 characters to enable proper reasoning. "
    
    "After reading each chunk, reason carefully over its contents. "
    "You must not check whether a chunk exists using if chunk: as a condition for saving a quote.Instead, always assume a chunk exists if the tool has returned one, and then reason over the content of the chunk.Save a quote only if you determine it's motivational or insightful,"
    "You are not writing code to parse the transcript. You must reason over each chunk as if you are a human listening to the speaker. "
    "For each chunk, ask yourself: Was something inspiring, wise, or motivational said? "
    
    "If so, do the following:\n"
    "- Copy the quote exactly, or provide a concise summary if necessary.\n"
    "- Include the timestamp(s) shown in the chunk.\n"
    "- Use the `SaveMotivationalQuote` tool to write that quote and timestamp to `text_file`.\n"
    
    "If no motivational content is found, simply skip saving and move on. Then, call `Proccess_transcript_in_chunks` again to get the next chunk. "
    "Repeat this process until the tool returns an empty string (\"\"). "
    
    "IMPORTANT: Do not use keyword search. Do not write any code to detect or extract motivational phrases. "
    "You must reason through the chunk with your own understanding — as a thoughtful human would — interpreting tone, message, and emotional or philosophical meaning. "
    
    "When the `Proccess_transcript_in_chunks` tool returns an empty string, you have reached the end of the transcript. "
    "At that point, review the contents of `text_file` and provide your final answer."
)



context_vars = {
               "video_path": video_path,
               "text_file" : text_file
            }       

manager_agent  = CodeAgent(
            model=model,
        tools=[ExtractAudioFromVideo,Proccess_transcript_in_chunks,SaveMotivationalQuote, SpeechToTextTool(),FinalAnswerTool()], 
            max_steps=20,
            verbosity_level=2,
            additional_authorized_imports=['datetime'],
            planning_interval=4,
        )

Response = manager_agent.run(
            task=user_task,
            additional_args=context_vars
        )
from rich.console import Console
manager_agent.logger.console = Console(file=open(r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\agent_tree.txt", "w"), force_terminal=True)
manager_agent.visualize()
del model



