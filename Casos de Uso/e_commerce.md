# Caso de Uso: Sistema de E-commerce

## Descrição
Este caso de uso descreve as interações entre os usuários e o sistema de e-commerce para realizar compras online.

## Atores
- **Cliente**: Usuário que navega e compra produtos.
- **Administrador**: Usuário que gerencia o catálogo de produtos e pedidos.
- **Sistema de Pagamento**: Serviço externo que processa pagamentos.

## Fluxo de Trabalho
1. **Cliente**: Navega pelo catálogo de produtos.
2. **Cliente**: Adiciona produtos ao carrinho de compras.
3. **Cliente**: Visualiza o carrinho de compras.
4. **Cliente**: Realiza o checkout.
5. **Sistema de Pagamento**: Processa o pagamento.
6. **Cliente**: Recebe confirmação do pedido.
7. **Administrador**: Gerencia o catálogo de produtos.
8. **Administrador**: Processa pedidos.

## Diagrama de Caso de Uso

+-------------------+ | Cliente | +-------------------+ | | Navegar pelo catálogo v +---------------------------+ | Sistema de E-commerce | +---------------------------+ | | Adicionar ao carrinho v +---------------------------+ | Carrinho de Compras | +---------------------------+ | | Realizar checkout v +---------------------------+ | Sistema de Pagamento | +---------------------------+ | | Processar pagamento v +---------------------------+ | Confirmação de Pedido | +---------------------------+ | | Gerenciar catálogo v +---------------------------+ | Administrador | +------------------------