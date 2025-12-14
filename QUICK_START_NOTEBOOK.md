# Quick Start Guide for Retrieval Notebook

## Fast Start

1. **Open the notebook:**
   ```bash
   jupyter notebook retrieval_notebook.ipynb
   ```

2. **Configure in Cell 2:**
   ```python
   config = {
       'ocr_type': 'gt',           # Change OCR type here
       'retriever_type': 'bm25',   # 'bm25' or 'bge-m3'
       'retrieve_top_k': 2,        # Number of docs to retrieve
   }
   ```

3. **Run all cells:** Cell → Run All

4. **View results:** Check the output cells and the generated JSON file in `./output/retrieval/{ocr_type}/`

## Common Configurations

### Test with BM25 (faster, no GPU needed)
```python
config['retriever_type'] = 'bm25'
```

### Test with BGE-M3 (better quality, needs GPU)
```python
config['retriever_type'] = 'bge-m3'
```

### Test different OCR types
```python
config['ocr_type'] = 'gt'        # Ground truth
config['ocr_type'] = 'MinerU'    # MinerU OCR results
```

### Retrieve more documents
```python
config['retrieve_top_k'] = 5
```

## What You Get

- **JSON Output:** `./output/retrieval/{ocr_type}/all_{retriever}_top{k}.json`
- **Interactive Results:** DataFrames showing performance metrics
- **Analysis:** Results grouped by evidence source and domain
- **Sample Results:** Detailed view of actual retrieval outputs

## Notebook Sections

1. **Blocks 1-3:** Setup and imports
2. **Block 4:** Configuration (⚠️ edit here)
3. **Blocks 5-9:** Pipeline execution
4. **Blocks 10-13:** Results visualization and analysis

## Tips

- Start with `ocr_type='gt'` and `retriever_type='bm25'` for fastest results
- Use `retrieve_top_k=2` for initial testing (as in the PowerShell script)
- Check the "Sample Retrieval Results" section (Block 13) to see actual retrieved documents
- Results are automatically saved - you can rerun visualization cells without rerunning retrieval

## Troubleshooting

**Missing dependencies:**
```bash
pip install -r requirements.txt
```

**Data files not found:**
Ensure `data/qas_v2.json` and `data/retrieval_base/{ocr_type}/` exist

**Out of memory (for BGE-M3):**
- Use CPU instead: Add `os.environ['CUDA_VISIBLE_DEVICES'] = ''` before Block 5
- Or use BM25 instead: `config['retriever_type'] = 'bm25'`

For detailed documentation, see [NOTEBOOK_README.md](NOTEBOOK_README.md)
