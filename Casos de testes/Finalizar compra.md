# Caso de Teste: Finalizar Compra

## Identificação
- **ID**: CT-005
- **Título**: Teste de Finalização de Compra
- **Prioridade**: Alta

## Descrição
Verificar se o sistema permite finalizar uma compra com sucesso.

## Pré-condições
- O usuário deve estar logado no sistema.
- O carrinho de compras deve conter pelo menos um produto.

## Passos
1. Navegar para o carrinho de compras.
2. Clicar no botão "Finalizar Compra".
3. Inserir as informações de pagamento válidas.
4. Inserir o endereço de entrega válido.
5. Confirmar a compra.

## Resultados Esperados
- O sistema deve processar o pagamento e exibir uma mensagem de confirmação de compra.
- Um e-mail de confirmação deve ser enviado para o usuário.
- O status do pedido deve ser atualizado para "Processando".

## Resultados Obtidos
- [ ] Sucesso
- [ ] Falha

## Notas
- Verificar se o sistema lida corretamente com diferentes métodos de pagamento.
- Testar com diferentes endereços de entrega para garantir a funcionalidade.

## Referências
- Kaner, C., Falk, J., & Nguyen, H. Q. (1999). Testing Computer Software (2ª edição). Wiley.