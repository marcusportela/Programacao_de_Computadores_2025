import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner leitura = new Scanner(System.in);
        int qtdHrDia;
        int qtdMinDia;
        int totalmin;
        double salario;
        double acrescimo;

        System.out.println("Quantas horas o funcionario trabalhou?");
        qtdHrDia = leitura.nextInt();
        System.out.println("Quantos minutos o funcionario trabalhou?");
        qtdMinDia = leitura.nextInt();
        System.out.println("Qual o salario?");
        salario = leitura.nextDouble();

        totalmin = ((qtdHrDia*60) + qtdMinDia);
        if (totalmin > 480) {
            System.out.println("Funcionário possui horas extras");
            acrescimo = (salario/13200) * (totalmin-480);
            System.out.println("Acrescimo do dia é de: R$" + acrescimo);
        } else {
            System.out.println("Funcionário não possui horas extras");
        }

    }
}