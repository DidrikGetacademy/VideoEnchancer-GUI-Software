# Third-party
import torch

# Global Variables
COMPUTATION_DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
EXECUTION_PROVIDER_LIST = ["CUDAExecutionProvider", "CPUExecutionProvider"]
ONNX_MODEL_PATH = r"C:\Users\didri\Desktop\Programmering\VideoEnchancer program\AI-onnx\Vocal_isolation.onnx"
INPUT_FOLDER = "./"
OUTPUT_FOLDER = "./"
