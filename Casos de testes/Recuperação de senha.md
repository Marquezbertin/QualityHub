# Caso de Teste: Recuperação de Senha

## Identificação
- **ID**: CT-003
- **Título**: Teste de Recuperação de Senha com E-mail Válido
- **Prioridade**: Média

## Descrição
Verificar se o sistema permite a recuperação de senha com um endereço de e-mail válido.

## Pré-condições
- O usuário deve estar registrado no sistema.
- O sistema deve estar acessível.

## Passos
1. Navegar para a página de login.
2. Clicar no link "Esqueci minha senha".
3. Inserir um endereço de e-mail válido registrado no sistema.
4. Clicar no botão "Enviar".

## Resultados Esperados
- O sistema deve enviar um e-mail de recuperação de senha para o endereço fornecido.
- Uma mensagem de confirmação deve ser exibida na interface.

## Resultados Obtidos
- [ ] Sucesso
- [ ] Falha

## Notas
- Verificar se o e-mail de recuperação contém um link válido para redefinição de senha.
- Testar com diferentes provedores de e-mail para garantir compatibilidade.

## Referências
- Black, R. (2009). Managing the Testing Process: Practical Tools and Techniques for Managing Hardware and Software Testing. Wiley.