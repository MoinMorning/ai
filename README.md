# LocalGPT: Engaging in Private


## Highlights 🌟
- **Absolute Privacy**: Your data stays on your machine, guaranteeing complete security.
- **Flexible Model Integration**: Effortlessly incorporate a range of public models, including HF, GPTQ, GGML, and GGUF.
- **Varied Embeddings**: Select from an assortment of public embeddings.
- **LLM Reusability**: Once downloaded, your LLM can be reused without the need for additional downloads.
- **Conversation Memory**: Retains your past conversations (within a session).
- **API**: LocalGPT provides an API for developing RAG Applications.
- **User Interface**: LocalGPT offers two GUIs, one that utilizes the API and another that is standalone (built on streamlit).
- **Multi-platform Support**: Out-of-the-box support for multiple platforms. Interact with your data using `CUDA`, `CPU` or `MPS` and more!

## Learn More with Our Videos 🎥
- In-depth code walkthrough
- Llama-2 integration with LocalGPT
- Incorporating Chat History
- LocalGPT - Latest Update (09/17/2023)

## Technical Aspects 🛠️
By choosing the appropriate local models and leveraging the power of `LangChain`, you can execute the entire RAG pipeline on-premise, without any data leaving your environment, and with satisfactory performance.

- `ingest.py` employs `LangChain` tools to parse the document and generate embeddings locally using `InstructorEmbeddings`. It then saves the result in a local vector database using the `Chroma` vector store.
- `run_localGPT.py` uses a local LLM to comprehend questions and formulate answers. The context for the answers is extracted from the local vector store using a similarity search to find the right context from the docs.
- You can substitute this local LLM with any other LLM from HuggingFace. Ensure that the LLM you choose is in the HF format.

This project was motivated by the original privateGPT.

## Built With 🧩
- LangChain
- HuggingFace LLMs
- InstructorEmbeddings
- LLAMACPP
- ChromaDB
- Streamlit

# Setting Up the Environment 🌍

1. 📥 Clone the repository using git:

```shell
git clone https://github.com/PromtEngineer/localGPT.git

🐍 Install conda for managing virtual environments. Create and activate a new virtual environment.
conda create -n localGPT python=3.10.0
conda activate localGPT

🛠️ Install the dependencies using pip
To prepare your environment to run the code, first install all requirements:

pip install -r requirements.txt

Installing LLAMA-CPP :

LocalGPT uses LlamaCpp-Python for GGML (you will need llama-cpp-python <=0.1.76) and GGUF (llama-cpp-python >=0.1.83) models.

If you want to use BLAS or Metal with llama-cpp you can set appropriate flags:

For NVIDIA GPUs support, use cuBLAS

# Example: cuBLAS
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir

For Apple Metal (M1/M2) support, use

# Example: METAL
CMAKE_ARGS="-DLLAMA_METAL=on"  FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir

For more details, please refer to llama-cpp

Docker 🐳
Installing the required packages for GPU inference on NVIDIA GPUs, like gcc 11 and CUDA 11, may cause conflicts with other packages in your system. As an alternative to Conda, you can use Docker with the provided Dockerfile. It includes CUDA, your system just needs Docker, BuildKit, your NVIDIA GPU driver and the NVIDIA container toolkit. Build as docker build -t localgpt ., requires BuildKit. Docker BuildKit does not support GPU during docker build time right now, only during docker run. Run as docker run -it --mount src="$HOME/.cache",target=/root/.cache,type=bind --gpus=all localgpt.

Test dataset
For testing, this repository comes with Constitution of USA as an example file to use.

Ingesting your OWN Data.
Put your files in the SOURCE_DOCUMENTS folder. You can put multiple folders within the SOURCE_DOCUMENTS folder and the code will recursively read your files.

Support file formats:
LocalGPT currently supports the following file formats. LocalGPT uses LangChain for loading these file formats. The code in constants.py uses a DOCUMENT_MAP dictionary to map a file format to the corresponding loader. In order to add support for another file format, simply add this dictionary with the file format and the corresponding loader from LangChain.

DOCUMENT_MAP = {
    ".txt": TextLoader,
    ".md": TextLoader,
    ".py": TextLoader,
    ".pdf": PDFMinerLoader,
    ".csv": CSVLoader,
    ".xls": UnstructuredExcelLoader,
    ".xlsx": UnstructuredExcelLoader,
    ".docx": Docx2txtLoader,
    ".doc": Docx2txtLoader,
}

Ingest
Run the following command to ingest all the data.

If you have cuda setup on your system.

python ingest.py

You will see an output like this: <img width=“1110” alt=“Screenshot 2023-09-14 at 3 36 27 PM” src=“https://github.com/PromtEngineer/localGPT/assets/134474669/c9274e9a-842c-49b9-8d95-606c3d80011f”>

Use the device type argument to specify a given device. To run on cpu

python ingest.py --device_type cpu

To run on M1/M2

python ingest.py --device_type mps

Use help for a full list of supported devices.

python ingest.py --help

This will create a new folder called DB and use it for the newly created vector store. You can ingest as many documents as you want, and all will be accumulated in the local embeddings database. If you want to start from an empty database, delete the DB and reingest your documents.

Note: When you run this for the first time, it will need internet access to download the embedding model (default: Instructor Embedding). In the subsequent runs, no data will leave your local environment and you can ingest data without internet connection.

Ask questions to your documents, locally!
In order to chat with your documents, run the following command (by default, it will run on cuda).

python run_localGPT.py

You can also specify the device type just like ingest.py

python run_localGPT.py --device_type mps # to run on Apple silicon

This will load the ingested vector store and embedding model. You will be presented with a prompt:

> Enter a query: