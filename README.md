<h4> --> Para visualizar a documentação e instalação do backend e frontend acesse a pasta de cada a partir desse diretório do GitHub, lá contém um README.md com a devida explicação sobre o mesmo <--</h4>
</br>
</br>
Projeto desenvolvido como um teste ténico da Verzel. Ele utiliza Flask, Vue.js, banco de dados SQLite e libs secundárias.
</br>
<h5> O projeto </h5>
O projeto simula um catálogo de venda de veículos, onde é possível filtrá-los e ordena-los a partir de todos seus parâmetros cadastrados. O sistema utiliza a lógica do token JWT para fazer requisições no server side a partir de um super usuário (Admin), ou seja, qualquer um pode criar uma conta, mas apenas usuários administradores conseguem criar, atualizar e deletar usuários e veículos. Essas requisições (possível verificar a documentação da API na página <strong>backend</strong>) são feitas com um parâmetro de headers chamado <strong>x-access-token</strong> onde carrega o token necessário para cada requisição especial
</br>
<h5> Banco de Dados </h5>
O banco de dados utilizado nesse sitema é o SQLite, pois possuí fácil integração com o backend e modelagem de dados (MySQL seria uma segunda opção, porém com maior dificuldade para quem for testar). O banco e suas tabelas são criadas logo na primeira vez que o server é ligado (arquivo main.py executado), assim como um super usuário criado a partir do email e senha fornecido nas variáveis de ambiente (verificar abaixo modelo de .env recomendado para esta aplicação), podendo depois administrar os próximos veículos e usuários criados.
</br>
<h5> Instalaçao </h5>
Para instalar os pacotes necessários para o backend (Flask) acesse a pasta <strong>backend</strong> e instale os pacotes listados no </strong>requirements.txt</strong> para então, conseguir rodar o arquivo main.py que se encontra na mesma pasta. - É recomendado utilização de ambiente virtual para não ter conflito de versões -. Para a instalação do frontend acesse a pasta <strong>frontend</strong> e siga o passo a passo do README onde explica como instalar a aplicação Vue, depois apenas rode o comando de <strong>serve</strong> para fazer a integração com ambos.
<br>
<h5>Token JWT</h5>
O sistema possui autenticação do tipo JWT (JSON Web Token), que é constituido por um token gerado no login do usuário, e nele contém as informações do mesmo (de forma codificada) junto com o tempo de validade do token, para realizar requisições no backend. O token é regenerado a cada 5 minutos, onde é feito uma requisição para manter o usuário logado, caso dê algum problema nesta requisição o usuário é deslogado e levado para a tela de login.
<br>
<h5> Deploy </h5>
Em breve será feito o deploy da aplicação e disponibilizarei o link <a href="#">aqui</a>
<br>
<h5> Demo </h5>
Demo gravado da aplicação rodando no dia 02/11/2022 com último commit apresentado aqui, <strong>https://www.youtube.com/watch?v=mCntW1af10Y&ab_channel=GabrielFranco<strong> - Recomendado olhar em 1.5x, pois realizei o teste de todas as utilização de forma devagar e vísivel -.
 </br>
  <h5> Tecnologias </h5>
  O app foi feito com as seguintes tecnologias:
  <ul>
   <li>Flask (Python)</li>
   <li>Vue.js</li>
   <ul>
    <li>Vuetify</li>
    <li>Vuex</li>
    <li>Vue Routes</li>
    <li>Axios</li>
   </ul>
  <li>SQLite</li>
  </ul>
 <br>
 <h5> Modelo .env (variáveis de ambiente) </h5>
 Para utilizar o token JWT é gerado uma decodificação através da secret-key salva no servidor Flask, para se ter essa variável é preciso que se gere uma randomização de caracteres e salve em variáveis de ambiente, assim como os dados do super administrador criado na primeira execução.
  Você pode criar um arquivo chamado <strong>.env</strong> no diretório <strong>backend</strong> e salvar como variáveis normais, ou então salvar diretamente no ambiente do sistema operacional.
 </br>
 </br>
  Exemplo de variáis salvas:
  <ul>
    <li>SECRET_KEY = 'random-string'</li>
    <li>ADMIN_EMAIL = 'adm@adm.com'</li>
    <li>ADMIN_PASSWORD = '12345'</li>
  </ul>
  </br>
  
    


