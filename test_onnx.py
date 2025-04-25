import onnx

# Load the ONNX model
model_path = r"C:\Users\didri\Desktop\LearnReflect VideoEnchancer\AI-onnx\Vocal_Isolation_UNet.onnx"
model = onnx.load(model_path)

# Print model inputs
logging.info("Inputs:")
for input in model.graph.input:
    input_name = input.name
    input_shape = [dim.dim_value for dim in input.type.tensor_type.shape.dim]
    logging.info(f"Name: {input_name}, Shape: {input_shape}")

# Print model outputs
logging.info("\nOutputs:")
for output in model.graph.output:
    output_name = output.name
    output_shape = [dim.dim_value for dim in output.type.tensor_type.shape.dim]
    logging.info(f"Name: {output_name}, Shape: {output_shape}")
