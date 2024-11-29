# Conceitos Fundamentais de Qualidade de Software

## O que é Qualidade de Software?

Qualidade de software refere-se ao grau em que um sistema ou componente atende aos requisitos funcionais, não funcionais e às expectativas do usuário, garantindo confiabilidade, eficiência, segurança e facilidade de manutenção.

De acordo com o padrão ISO/IEC 25010:2011, a qualidade de um software pode ser avaliada por suas características de qualidade, como:

* Funcionalidade
* Desempenho
* Usabilidade
* Confiabilidade
* Segurança
* Compatibilidade
* Manutenibilidade
* Portabilidade

Citação:
“Software quality involves understanding the complex interplay of technical, organizational, and human factors that contribute to the creation of robust, reliable systems.”
— Ian Sommerville, Software Engineering (10th Edition).

## Dimensões da Qualidade de Software

1. Produto vs. Processo
A qualidade pode ser analisada sob duas perspectivas:

Qualidade do Produto: Características inerentes ao software, como desempenho e segurança.

Qualidade do Processo: Métodos e práticas usados para desenvolver o software. Um processo de alta qualidade frequentemente resulta em um produto de alta qualidade (Pressman, Software Engineering: A Practitioner’s Approach).

2. Modelo de Qualidade ISO/IEC 25010
O modelo ISO/IEC 25010 organiza a qualidade em dois blocos principais:

Qualidade em Uso: Mede a satisfação do usuário final durante o uso do sistema.
Qualidade do Produto: Avalia características como segurança e confiabilidade do software.
Fonte: ISO/IEC 25010 Standard.

3. Características de Qualidade

3.1 Funcionalidade : 

O software deve atender aos requisitos e ser adequado ao propósito pretendido.

Exemplo: Um sistema bancário deve garantir transações seguras e precisas.

3.2. Desempenho: 

Refere-se ao tempo de resposta, throughput e uso eficiente de recursos.

Fonte: Capítulo 8, Sommerville, Software Engineering.

3.3. Usabilidade: 

A facilidade com que o sistema pode ser usado por usuários específicos.

Referência: Nielsen, J. (1993). Usability Engineering.

3.4. Segurança: 

Proteção contra acesso não autorizado e ataques.

Referência: Bishop, M. (2004). Introduction to Computer Security.

## Por que a Qualidade de Software é Importante?

A falta de qualidade em software pode causar:

* Impactos financeiros: Custos de manutenção e retrabalho.
* Impactos na segurança: Brechas de segurança podem levar a roubos de dados.
* Impactos reputacionais: Softwares mal projetados afetam a confiança dos usuários.

Exemplo de caso real:

O erro de cálculo no software da missão Ariane 5 causou sua destruição 40 segundos após o lançamento, resultando em um prejuízo de mais de US$ 370 milhões (Referência: Lion, C., Ariane 5: Flight 501 Failure).

O Ariane 5, foguete desenvolvido pela Agência Espacial Europeia (ESA), foi destruído 40 segundos após o lançamento em seu voo inaugural em 4 de junho de 1996, causando um prejuízo de aproximadamente US$ 370 milhões. A falha foi atribuída a um erro de software no sistema de navegação inercial, causado por uma conversão inadequada de dados.

Durante o lançamento, um valor de velocidade horizontal, que deveria ser armazenado como um número de 64 bits em ponto flutuante, foi acidentalmente convertido para um formato de 16 bits. O valor excedeu o limite, resultando em um overflow e falha do sistema. Este erro não foi tratado corretamente, pois o software não possuía mecanismos robustos de verificação e exceção, e o sistema de backup, que também utilizava o mesmo código, falhou.

O incidente destacou a importância de uma verificação rigorosa de código e a necessidade de testes realistas para cenários de falha. Além disso, evidenciou os riscos da reutilização de software sem considerar as diferenças operacionais entre sistemas. O caso Ariane 5 tornou-se um exemplo clássico sobre como pequenas falhas no design de software podem resultar em consequências catastróficas em sistemas críticos.

## Referências Científicas e Materiais Utilizados
* Sommerville, I. (2015). Software Engineering (10ª edição). Pearson.
* Pressman, R. (2014). Software Engineering: A Practitioner’s Approach (8ª edição). McGraw Hill.
* ISO/IEC 25010:2011 - Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models.
* Nielsen, J. (1993). Usability Engineering. Academic Press.
* Bishop, M. (2004). Introduction to Computer Security. Addison-Wesley.
* Lion, C. Ariane 5: Flight 501 Failure.
* Knight, J. C. (2002). Safety Critical Systems: Challenges and Directions. IEEE Software
