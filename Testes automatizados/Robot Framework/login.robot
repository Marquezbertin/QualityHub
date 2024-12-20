*** Settings ***
Library    SeleniumLibrary
Resource   resources/keywords.robot

*** Variables ***
${URL}     http://exemplo.com/login

*** Test Cases ***
Login Com Sucesso
    [Documentation]    Teste de login com credenciais válidas
    Abrir Navegador    ${URL}    chrome
    Inserir Credenciais    usuario_valido    senha_valida
    Clicar Botao Login
    Verificar Login Com Sucesso
    Fechar Navegador

Login Com Falha
    [Documentation]    Teste de login com credenciais inválidas
    Abrir Navegador    ${URL}    chrome
    Inserir Credenciais    usuario_invalido    senha_invalida
    Clicar Botao Login
    Verificar Mensagem De Erro
    Fechar Navegador