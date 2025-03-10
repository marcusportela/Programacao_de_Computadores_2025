# 🕒 Cálculo de Horas Extras em Java  

## 📌 Sobre o Projeto  
Na disciplina "Programação de computadores", cursada no oitavo semestre da faculdade UDF, fizemos um programa em **Java** que permite calcular as horas extras de um funcionário com base no tempo trabalhado e no salário informado. Ele determina se houve trabalho além da carga horária padrão (8 horas ou 480 minutos) e calcula o acréscimo salarial correspondente.  

## 🛠️ Como Funciona?  
1. O usuário insere:  
   - **Horas** e **minutos** trabalhados no dia  
   - **Salário mensal** do funcionário  
2. O programa converte as horas em minutos e verifica se o total ultrapassa **480 minutos** (8 horas).  
3. Se o funcionário trabalhar mais de **8 horas (480 minutos)**, ele terá direito a um acréscimo no salário.  
O cálculo funciona assim:  
a. Pegamos o **salário mensal** e dividimos por **13.200** (número total de minutos em um mês de trabalho).  
b. Multiplicamos esse valor pelo número de **minutos extras trabalhados** (total de minutos do dia menos 480).  

O resultado é o valor extra que o funcionário recebe por aquele dia de trabalho.  

4. O resultado é exibido na tela.  

## 📚 Conceitos Aplicados  
- **Entrada de Dados:** `Scanner` para capturar informações do usuário.  
- **Operações Matemáticas:** Cálculo de tempo e remuneração adicional.  
- **Estrutura Condicional (`if-else`)** para verificar se há horas extras.  
- **Manipulação de Tipos de Dados:**  
  - `int` para horas e minutos trabalhados.  
  - `double` para salário e acréscimo.  

## 📌 Requisitos para Executar  
- **Java 8+** instalado  
- **IDE** (Eclipse, IntelliJ, VS Code) ou terminal com `javac`  

## 🎯 Como Executar  
1. Compile o código:  
   ```sh
   javac Main.java

## 📄 Referência  
- **Livro: SIERRA, Kathy e BATES, Bert. Use a Cabeça!: Java** aprendizado em programação orientada a objetos (OO) e Java. Alta Books; 2ª edição (16 novembro 2007). 496 p.  
- **Apostila: ALURA. Java e Orientação a Objetos**. Disponível em: [Alura](https://www.alura.com.br/apostila-java-orientacao-objetos?srsltid=AfmBOorrlWglMhV0ahe7XvrtmAERfQ-eaR_OPUalyvcHbAj3PC2JCDNM). Acesso em 4 mar. 2025.
