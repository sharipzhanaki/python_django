from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get("a", "")
    b = request.GET.get("b", "")
    result = a + b
    context = {
        "a": a,
        "b": b,
        "result": result,
    }
    return render(request, "requestdataapp/request-query-params.html", context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    return render(request, "requestdataapp/user-bio-form.html")


MAX_FILE_SIZE = 1 * 1024 * 1024 # 1 Мб

def handle_file_upload(request: HttpRequest) -> HttpResponse:
    context = {}

    if request.method == "POST" and request.FILES.get("myfile"):
        myfile = request.FILES["myfile"]

        if myfile.size > MAX_FILE_SIZE:
            context["error"] = "Error: file exceeds the allowed size of 1 MB."
            return render(request, "requestdataapp/file-upload.html", context=context)

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        context["success"] = f"File {filename} saved successfully"
        context["filename"] = filename
        context["filesize"] = round(myfile.size / 1024, 2)

    return render(request, "requestdataapp/file-upload.html", context=context)
