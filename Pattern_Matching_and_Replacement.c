#include <stdio.h>
#include <string.h>

#define MAX 1000

int main() {
    char STR[MAX], PAT[MAX], REP[MAX], RESULT[MAX];
    int i, j, k, found = 0;

    printf("Enter the main string (STR): ");
    fgets(STR, MAX, stdin);
    STR[strcspn(STR, "\n")] = '\0'; // remove newline

    printf("Enter the pattern string (PAT): ");
    fgets(PAT, MAX, stdin);
    PAT[strcspn(PAT, "\n")] = '\0';

    printf("Enter the replace string (REP): ");
    fgets(REP, MAX, stdin);
    REP[strcspn(REP, "\n")] = '\0';

    i = 0; j = 0;
    while (STR[i] != '\0') {
        // Check if PAT occurs at position i
        k = 0;
        while (PAT[k] != '\0' && STR[i + k] == PAT[k]) {
            k++;
        }

        if (PAT[k] == '\0') { // full match found
            found = 1;
            strcpy(&RESULT[j], REP);
            j += strlen(REP);
            i += strlen(PAT);
        } else {
            RESULT[j++] = STR[i++];
        }
    }
    RESULT[j] = '\0';

    if (found) {
        printf("\nResultant string after replacement: %s\n", RESULT);
    } else {
        printf("\nPattern \"%s\" not found in the main string.\n", PAT);
    }

    return 0;
}
