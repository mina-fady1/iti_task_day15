from django.shortcuts import render

def index(request):
    card_symbols = [
        {'id': 'python', 'icon': 'fa-brands fa-python', 'color': '#3776ab', 'name': 'Python'},
        {'id': 'django', 'icon': 'fa-solid fa-gem', 'color': '#092e20', 'name': 'Django'},
        {'id': 'js', 'icon': 'fa-brands fa-js', 'color': '#f7df1e', 'name': 'JavaScript'},
        {'id': 'html', 'icon': 'fa-brands fa-html5', 'color': '#e34f26', 'name': 'HTML5'},
        {'id': 'css', 'icon': 'fa-brands fa-css3-alt', 'color': '#1572b6', 'name': 'CSS3'},
        {'id': 'react', 'icon': 'fa-brands fa-react', 'color': '#61dafb', 'name': 'React'},
        {'id': 'github', 'icon': 'fa-brands fa-github', 'color': '#ffffff', 'name': 'GitHub'},
        {'id': 'database', 'icon': 'fa-solid fa-database', 'color': '#f59e0b', 'name': 'Database'},
        {'id': 'server', 'icon': 'fa-solid fa-server', 'color': '#10b981', 'name': 'Server'},
        {'id': 'terminal', 'icon': 'fa-solid fa-terminal', 'color': '#ec4899', 'name': 'Terminal'},
        {'id': 'code', 'icon': 'fa-solid fa-code', 'color': '#6366f1', 'name': 'Code'},
        {'id': 'cpu', 'icon': 'fa-solid fa-microchip', 'color': '#06b6d4', 'name': 'CPU'},
    ]
    return render(request, 'memory_match/index.html', {'symbols': card_symbols})
