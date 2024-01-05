from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse( '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemplo de Página</title>
    <!-- Seção para adicionar links para folhas de estilo, scripts, etc. -->
</head>
<body>
    <!-- Corpo da página -->
    <header>
        <h1>Título da Página</h1>
        <p>Subtítulo ou descrição breve.</p>
    </header>
    <nav>
        <!-- Seção de navegação, links para outras partes da página ou site -->
        <ul>
            <li><a href="#secao1">Seção 1</a></li>
            <li><a href="#secao2">Seção 2</a></li>
            <!-- Adicione mais itens conforme necessário -->
        </ul>
    </nav>
    <main>
        <!-- Conteúdo principal da página -->
        <section id="secao1">
            <h2>Seção 1</h2>
            <p>Conteúdo da Seção 1.</p>
        </section>
        <section id="secao2">
            <h2>Seção 2</h2>
            <p>Conteúdo da Seção 2.</p>
        </section>
        <!-- Adicione mais seções conforme necessário -->
    </main>
    <footer>
        <!-- Rodapé da página -->
        <p>&copy; 2024 Exemplo de Página</p>
    </footer>
    <!-- Seção para adicionar scripts ao final da página, se necessário -->
</body>
</html>
''')
