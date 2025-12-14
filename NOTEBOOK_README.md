# RAG Retrieval Notebook

This Jupyter Notebook (`retrieval_notebook.ipynb`) replicates the functionality of the PowerShell script `retrieval.ps1` for executing retrieval tasks in the RAG pipeline.

## Overview

The notebook performs document retrieval using either BM25 or BGE-M3 retrievers and evaluates the results using the LCS (Longest Common Subsequence) metric.

## Features

- **Configurable Parameters**: Easy-to-modify configuration block for OCR type, retriever type, and other settings
- **Two Retriever Options**: Support for both BM25 and BGE-M3 retrievers
- **Comprehensive Results**: Displays results with detailed metrics and visualizations
- **Analysis Tools**: Built-in analysis by evidence source and domain
- **Sample Output**: Shows sample retrieval results for inspection

## Prerequisites

Ensure you have installed all required dependencies:

```bash
pip install -r requirements.txt
```

Required data files:
- `data/qas_v2.json` - Question-answer dataset
- `data/retrieval_base/gt/` - Ground truth retrieval documents (or other OCR types)

## Usage

### 1. Open the Notebook

```bash
jupyter notebook retrieval_notebook.ipynb
```

Or use JupyterLab:

```bash
jupyter lab retrieval_notebook.ipynb
```

### 2. Configure Parameters

In the "Configuration Parameters" cell (Block 2), modify the configuration dictionary:

```python
config = {
    'ocr_type': 'gt',              # Change to 'MinerU' or other OCR types
    'retriever_type': 'bm25',      # Change to 'bge-m3' for BGE-M3 retriever
    'retrieve_top_k': 2,           # Number of documents to retrieve
    'data_path': 'data/qas_v2.json',
    # ... other parameters
}
```

### 3. Run All Cells

Execute all cells in order using "Run All" from the Cell menu, or run each cell sequentially.

## Notebook Structure

1. **Import Packages**: Load all required libraries and modules
2. **Configuration Parameters**: Set up the retrieval pipeline configuration
3. **Set Random Seed**: Ensure reproducibility
4. **Load Dataset**: Load the QA dataset from JSON
5. **Initialize Model and Retriever**: Set up the retriever (BM25 or BGE-M3)
6. **Initialize Retrieval Task**: Create the retrieval task instance
7. **Execute Retrieval Pipeline**: Process all data points
8. **Compute Overall Metrics**: Calculate aggregate metrics
9. **Save Results**: Save output to JSON file
10. **Display Results Summary**: Show results in DataFrame format
11. **Results Analysis by Evidence Source**: Analyze performance by evidence type
12. **Results Analysis by Domain**: Analyze performance by document domain
13. **Sample Retrieval Results**: Display detailed results for sample queries

## Output

The notebook generates:

1. **JSON Output File**: Saved to `./output/retrieval/{ocr_type}/all_{retriever}_top{k}.json`
   - Contains all results, metrics, and metadata
   
2. **Visual Output in Notebook**:
   - Overall metrics (average LCS score)
   - Results DataFrame with all data points
   - Analysis by evidence source (table, text, formula, chart, etc.)
   - Analysis by domain (finance, academic, etc.)
   - Sample retrieval results with retrieved documents and ground truth

## Comparison with PowerShell Script

The notebook provides the same functionality as running:

```powershell
.\.venv\Scripts\python.exe quick_start.py `
    --model_name 'mock' `
    --retriever bm25 `
    --retrieve_top_k 2 `
    --data_path data/qas_v2.json `
    --docs_path "data/retrieval_base/gt" `
    --ocr_type gt `
    --task 'Retrieval' `
    --evaluation_stage 'retrieval' `
    --num_threads 1 `
    --show_progress_bar True
```

But with additional benefits:
- Interactive exploration of results
- Visual analysis and statistics
- Easy parameter modification
- Step-by-step execution
- Inline documentation

## Customization

### Using Different Retrievers

**BM25 (default)**:
```python
config['retriever_type'] = 'bm25'
```

**BGE-M3 (requires embedding model)**:
```python
config['retriever_type'] = 'bge-m3'
```

### Changing OCR Type

```python
config['ocr_type'] = 'MinerU'  # or 'gt', 'paddleocr', etc.
```

### Adjusting Retrieval Parameters

```python
config['retrieve_top_k'] = 5      # Retrieve more documents
config['chunk_size'] = 512         # Smaller chunks
config['chunk_overlap'] = 50       # Add overlap between chunks
```

## Troubleshooting

### Import Errors

If you encounter import errors, ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Missing Data Files

Ensure the data files exist:
- Check `data/qas_v2.json` exists
- Check `data/retrieval_base/{ocr_type}/` directory exists and contains JSON files

### CUDA/GPU Issues

If using BGE-M3 and encountering GPU issues:
- Ensure PyTorch is installed with CUDA support
- Or set environment variable to use CPU: `os.environ['CUDA_VISIBLE_DEVICES'] = ''`

## Notes

- The notebook uses a Mock LLM model as it's only performing retrieval (no generation)
- Results are automatically saved to the output directory
- Progress bars are enabled by default for better visibility
- All random seeds are set for reproducibility

## Related Files

- `retrieval.ps1` - Original PowerShell script
- `quick_start.py` - Python script for running RAG pipeline
- `src/tasks/retrieval.py` - Retrieval task implementation
- `src/retrievers/custom.py` - Retriever implementations
- `exp_scripts/exp_show.ipynb` - Results visualization notebook
