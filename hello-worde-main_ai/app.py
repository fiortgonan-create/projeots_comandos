from flask import Flask, render_template, request, redirect, url_for, flash

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Chave secreta necessária para usar mensagens flash (alertas) e sessões futuramente
app.secret_key = 'chave_secreta_helpdesk_comandos'

# ==============================================================================
# ROTA 1: PÁGINA INICIAL (HOME)
# ==============================================================================
@app.route('/')
def home():
    # Apenas renderiza a tela principal (dashboard)
    return render_template('home.html')


# ==============================================================================
# ROTA 2: TELA DE LOGIN
# ==============================================================================
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Se o usuário clicou no botão "entrar" (método POST)
    if request.method == 'POST':
        # Captura os dados do formulário baseados no atributo 'name' do HTML
        email = request.form.get('email')
        senha = request.form.get('senha')

        # [FUTURO]: Aqui entrará o SELECT do MySQL para verificar se o usuário existe
        print(f"--> TENTATIVA DE LOGIN: E-mail: {email} | Senha: {senha}")

        # Após logar com sucesso, redireciona para a tela inicial
        return redirect(url_for('home'))

    # Se for requisição GET (apenas acessando a página), mostra o HTML de login
    return render_template('login.html')


# ==============================================================================
# ROTA 3: TELA DE CADASTRO
# ==============================================================================
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    # Se o usuário preencheu os dados e clicou em "cadastrar"
    if request.method == 'POST':
        # Capturando todos os campos do seu grid de cadastro
        nome = request.form.get('nome')
        cpf = request.form.get('CPF')
        celular = request.form.get('celular')
        email = request.form.get('email')
        senha = request.form.get('senha')
        data_nasc = request.form.get('data_nascimento')
        estado = request.form.get('estado')
        cidade = request.form.get('cidade')

        # [FUTURO]: Aqui entrará o INSERT INTO do MySQL para salvar o usuário no banco
        print(f"--> NOVO CADASTRO RECEBIDO:")
        print(f"Nome: {nome} | CPF: {cpf} | Email: {email} | Nasc: {data_nasc}")

        # Redireciona para a página de login para ele poder acessar a conta criada
        return redirect(url_for('login'))

    return render_template('cadastro.html')


# ==============================================================================
# ROTA 4: TELA DE ABERTURA DE CHAMADOS (SOLICITAR TÉCNICO)
# ==============================================================================
@app.route('/chamado', methods=['GET', 'POST'])
def chamado():
    # Se o usuário preencheu o chamado e enviou
    if request.method == 'POST':
        nome_cliente = request.form.get('nome_cliente')
        tipo_maquina = request.form.get('tipo_maquina')
        descricao = request.form.get('descricao')

        # Opcional: Coletar arquivos se houver upload (requer ajustes no form HTML futuramente)
        # arquivos = request.files.getlist('arquivo-erro')

        # [FUTURO]: Aqui entrará o INSERT INTO na tabela de chamados do MySQL
        print(f"--> NOVO CHAMADO ABERTO:")
        print(f"Usuário: {nome_cliente} | Máquina: {tipo_maquina}")
        print(f"Problema: {descricao}")

        # Retorna para a página principal (Home) depois de abrir o chamado
        return redirect(url_for('home'))

    return render_template('chamado.html')


# ==============================================================================
# EXECUÇÃO DO SERVIDOR
# ==============================================================================
if __name__ == '__main__':
    # O debug=True permite que o site atualize sozinho quando você salva alterações no código
    app.run(debug=True, port=5000)
