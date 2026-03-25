from django.shortcuts import render
from .models import LegalDocument
from .forms import UploadForm

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Attempt to import custom AI core utilities
try:
    from ai_core.parser import extract_text
    from ai_core.grok import get_summary, ask_question
except ModuleNotFoundError as e:
    extract_text = None
    get_summary = None
    ask_question = None
    import logging
    logging.error("ai_core module not found: %s", e)

def upload_document(request):
    summary = None
    answer = None
    error_message = None

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()

            if extract_text and get_summary:
                try:
                    text = extract_text(doc.file.path)
                    summary = get_summary(text)
                    
                    question = request.POST.get('question')
                    if question and ask_question:
                        answer = ask_question(text, question)
                    elif question:
                        error_message = "Question-answering functionality is not available."

                except Exception as e:
                    error_message = f"Error processing document: {e}"
            else:
                error_message = "AI processing modules are not available."
    else:
        form = UploadForm()

    return render(request, 'assistant/upload.html', {
        'form': form,
        'summary': summary,
        'answer': answer,
        'error_message': error_message
    })
