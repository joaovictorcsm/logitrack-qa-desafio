# LogiTrack Pro — Desafio Técnico de QA

Projeto desenvolvido como parte de um desafio técnico de Qualidade, com foco na execução e documentação de testes funcionais no sistema LogiTrack Pro.

O projeto contempla a elaboração de cenários de teste, registro de evidências, análise da experiência do usuário e uma prova de conceito de automação utilizando Playwright.

##  Atividades realizadas

- Elaboração e execução de cenários de testes funcionais;
- Validação das funcionalidades de login, veículos, manutenções, viagens e dashboard;
- Execução de cenários positivos e negativos;
- Registro dos resultados obtidos e evidências;
- Identificação e documentação de comportamentos inesperados;
- Análise da experiência do usuário (UX);
- Automação de cenários de login com Playwright.

##  Estrutura do projeto

```text
logitrack-qa-desafio/
│
├── docs/
│   ├── 11_cenários_teste.xlsx
│   ├── analise_experiência_usuário.pdf
│   └── estrategia_testes_adicionais.pdf
│
├── evidencias/
│   └── Evidências dos cenários executados
│
├── teste_automacao/
│   └── test_login.py
│
├── .gitignore
└── README.md
```

### `docs/`

Contém a documentação produzida durante o desafio:

- Planilha com os cenários de teste, objetivo, pré-condições, dados utilizados, passos, resultados esperados, resultados obtidos, status e evidência;
- Documento com análise e recomendações relacionadas à experiência do usuário.

### `evidencias/`

Contém as capturas de tela utilizadas como evidências da execução dos cenários de teste.

### `testes/`

Contém a prova de conceito de automação desenvolvida com Python, Playwright e Pytest.

##  Automação de testes

Foram automatizados três cenários relacionados ao login:

1. Login com credenciais válidas;
2. Login com senha incorreta;
3. Login com usuário incorreto.

A automação verifica o comportamento da aplicação a partir da URL apresentada após a tentativa de autenticação.

##  Ferramentas utilizadas

- Python
- Playwright
- Pytest
- Microsoft Excel
- Visual Studio Code
- Git
- GitHub

##  Como executar a automação

### Pré-requisitos

É necessário possuir Python instalado.

Instale as dependências:

```bash
pip install pytest-playwright
```

Instale os navegadores utilizados pelo Playwright:

```bash
playwright install
```

### Executando os testes

Abra o terminal na pasta raiz do projeto e execute:

```bash
pytest teste_automacao/test_login.py -v --headed
```

A opção `--headed` permite acompanhar visualmente a execução dos testes no navegador.

##  Documentação dos testes

Os cenários funcionais e seus respectivos resultados estão documentados na planilha disponível em `docs/`.

As capturas de tela correspondentes às execuções estão organizadas na pasta `evidencias/`.

##  Estratégia de Testes Adicionais

Além dos testes funcionais executados, foram propostas estratégias adicionais para ampliar a cobertura de qualidade do sistema:

- **Testes de Segurança — Prioridade Alta:** validação de autenticação, sessão e controle de acesso, visando reduzir riscos de acessos não autorizados e exposição indevida de informações.

- **Automação de Interface — Prioridade Alta:** ampliação da automação para cenários críticos e repetitivos, reduzindo o risco de regressões. Como prova de conceito, foram automatizados cenários de login utilizando Playwright e Pytest.

- **Testes de Acessibilidade — Prioridade Média:** validação de formulários, campos, botões, menus e navegação, buscando reduzir barreiras de utilização e melhorar a acessibilidade da aplicação.

A estratégia completa, incluindo objetivos, áreas do sistema, riscos e prioridades, está disponível na pasta `docs/`.

##  Autor

João Victor Costa