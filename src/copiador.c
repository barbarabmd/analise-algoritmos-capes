#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 1024

// isolacao do campo nome
void extrair_nome(const char *linha, char *nome) {
    int i = 0;
    while (linha[i] != ',' && linha[i] != '\n' && linha[i] != '\0') {
        nome[i] = linha[i];
        i++;
    }
    nome[i] = '\0';
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Uso: %s <origem.csv> <destino.csv> <estatisticas.csv>\n", argv[0]);
        return 1;
    }

    FILE *f_orig = fopen(argv[1], "r");
    FILE *f_dest = fopen(argv[2], "a+"); 
    FILE *f_stat = fopen(argv[3], "w"); 

    if (!f_orig || !f_dest || !f_stat) {
        printf("Erro ao abrir os arquivos.\n");
        return 1;
    }

    char linha_orig[MAX_LINE], nome_orig[MAX_LINE];
    char linha_dest[MAX_LINE], nome_dest[MAX_LINE];
    long comparacoes = 0, nomes_inseridos = 0;

    if (fgets(linha_orig, sizeof(linha_orig), f_orig) != NULL) {
        fseek(f_dest, 0, SEEK_END);
        if (ftell(f_dest) == 0) {
            fputs(linha_orig, f_dest);
        }
        rewind(f_dest); 
    }

    // leitura do arquivo de origem linha por linha
    while (fgets(linha_orig, sizeof(linha_orig), f_orig)) {
        extrair_nome(linha_orig, nome_orig);
        
        rewind(f_dest); 
        int redundante = 0;

        // busca sequencial no arquivo de destino
        while (fgets(linha_dest, sizeof(linha_dest), f_dest)) {
            extrair_nome(linha_dest, nome_dest);
            comparacoes++; 
            
            if (strcmp(nome_orig, nome_dest) == 0) {
                redundante = 1;
                break;
            }
        }

        // ver se tem duplicata
        if (redundante) {
            printf("ERRO: nome redundante encontrado: %s\n", nome_orig);
        } else {
            fseek(f_dest, 0, SEEK_END);
            fputs(linha_orig, f_dest);
            nomes_inseridos++;
            
            // trava para fazer os experimentos especificos:
            // if (nomes_inseridos == 160) {
            //     break;
            // }
        }
    }

    // estatisticas com o cabecalho
    fprintf(f_stat, "nomes_inseridos,comparacoes\n");
    fprintf(f_stat, "%ld,%ld\n", nomes_inseridos, comparacoes);

    fclose(f_orig);
    fclose(f_dest);
    fclose(f_stat);

    return 0;
}
