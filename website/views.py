from django.shortcuts import render
from django.http import HttpResponse
from website.forms import ContactMessageForm

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ContactMessageForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.save()

    form = ContactMessageForm()
    context = {'form': form,
               'skills': ['angularjs', 'Angular', 'ASP.NET API', 'ASP.NET MVC', 'Azure B2C', 'Azure SQL Database', 'C#',
    'CSS', 'Entity Framework', 'HTML', 'javascript', 'JIRA', 'Jenkins', 'Microsoft Windows Servers', '.Net Core 2.1',
    'nodejs npm', 'Power BI', 'Razor', 'React', 'SQL', 'SQL Server 2012', 'Stored Procedures', 'TFS', 'Visual Studio 2012',
    'Web Development', 'WIX', 'XML'],}
    return render(request, 'website/index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")