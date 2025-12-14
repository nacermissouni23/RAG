# retrieval_eval.ps1

param(
    [Parameter(Mandatory=$true)]
    [string]$OcrType,

    [Parameter(Mandatory=$true)]
    [string]$RetrieverType
)

# Use $OcrType and $RetrieverType variables for the script arguments
# The backtick (`) is used for line continuation in PowerShell
.\.venv\Scripts\python.exe quick_start.py `
    --model_name 'mock' `
    --retriever $RetrieverType `
    --retrieve_top_k 2 `
    --data_path data/qas_v2.json `
    --docs_path "data/retrieval_base/$OcrType" `
    --ocr_type $OcrType `
    --task 'Retrieval' `
    --evaluation_stage 'retrieval' `
    --num_threads 1 `
    --show_progress_bar True