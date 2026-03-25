from django.shortcuts import render, redirect
from .forms import UploadForm
from ai_core.parser import extract_text
from ai_core.gemini import get_summary, ask_question


def upload_document(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            doc = form.save()

            text = extract_text(doc.file.path)

            if not text:
                request.session['summary'] = "⚠️ Could not extract text."
                request.session['answer'] = None
            else:
                summary = get_summary(text)

                question = request.POST.get('question')
                answer = ask_question(text, question) if question else None

                request.session['summary'] = summary
                request.session['answer'] = answer

            return redirect('/')  # 🔥 KEY FIX

    else:
        form = UploadForm()

    summary = request.session.pop('summary', None)
    answer = request.session.pop('answer', None)

    return render(request, 'assistant/upload.html', {
        'form': form,
        'summary': summary,
        'answer': answer
    })