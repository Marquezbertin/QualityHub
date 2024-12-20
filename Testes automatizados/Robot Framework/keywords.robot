*** Keywords ***
Abrir Navegador
    [Arguments]    ${url}    ${browser}
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

Inserir Credenciais
    [Arguments]    ${username}    ${password}
    Input Text    id=username    ${username}
    Input Text    id=password    ${password}

Clicar Botao Login
    Click Button    id=loginButton

Verificar Login Com Sucesso
    Element Should Be Visible    id=logoutButton

Verificar Mensagem De Erro
    Element Should Be Visible    id=errorMessage

Fechar Navegador
    Close Browser