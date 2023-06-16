# portscan-ssrf

Este é um script em Python que realiza um portscan em um URL específico, testando diferentes portas para uma vulnerabilidade de SSRF (Server-Side Request Forgery). O objetivo do script é identificar se o servidor alvo está respondendo a solicitações em cada porta testada.

Requisitos:

Certifique-se de ter o Python 3 instalado em seu sistema para executar este script. Além disso, você precisará instalar a biblioteca requests, que pode ser instalada via pip:

```
pip install requests 
```

Como usar:

Certifique-se de ter o script ```
portscan-ssrf.py``` no seu diretório de trabalho.
Abra o arquivo ```
portscan-ssrf.py```
em um editor de texto.
Substitua "http://host/parameter=http://localhost:" pelo URL desejado, onde a parte vulnerável com a SSRF está presente.
Execute o script usando o seguinte comando:
```python3 portscan-ssrf.py ```

O script testará cada porta especificada na lista portas e exibirá o tamanho da resposta e o conteúdo da resposta para cada solicitação.
Como funciona
O script usa a biblioteca requests para enviar solicitações HTTP ao servidor alvo em diferentes portas especificadas na lista portas. Ele constrói o URL de teste substituindo o valor da porta na parte vulnerável da URL fornecida. Em seguida, envia uma solicitação GET para esse URL e exibe o tamanho e o conteúdo da resposta.

Este script é um exemplo básico de como testar diferentes portas em uma vulnerabilidade SSRF. Ele pode ser personalizado de acordo com suas necessidades específicas.

Limitações:

Ele testa apenas as portas especificadas na lista portas. Você pode adicionar ou modificar as portas conforme necessário.
O script não implementa medidas de segurança avançadas ou verificações adicionais. É importante considerar os riscos e implementar salvaguardas adicionais ao realizar testes de SSRF.
