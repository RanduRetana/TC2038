#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

int main() {
    std::string filename;
    int n;

    std::cout << "Ingrese el nombre del archivo: ";
    std::cin >> filename;
    
    std::cout << "Ingrese el valor de n: ";
    std::cin >> n;

    // Abrir el archivo
    std::ifstream infile(filename);

    if (!infile.is_open()) {
        std::cerr << "No se pudo abrir el archivo" << std::endl;
        return 1;
    }

    std::vector<std::vector<char>> table;
    std::vector<int> a(n, 0);
    std::string output;
    char ch;
    int row = 0;
    int col = 0;

    // Leer el archivo y llenar la tabla y el arreglo a
    while (infile.get(ch)) {
        if (col == 0) {
            table.push_back(std::vector<char>(n, n));
        }
        table[row][col] = ch;
        a[col] += ch;
        col++;
        if (col == n) {
            col = 0;
            row++;
        }
    }

    // Si el último renglón no está completo, se rellena con el valor n
    while (col != 0 && col < n) {
        table[row][col] = n;
        a[col] += n;
        col++;
    }

    // Calcular el hash
    for (int i = 0; i < n; i++) {
        a[i] = a[i] % 256;
        std::stringstream ss;
        ss << std::uppercase << std::setw(2) << std::setfill('0') << std::hex << a[i];
        output += ss.str();
    }

    // Imprimir la tabla
    std::cout << "Tabla:\n";
    for (const auto& r : table) {
        for (char c : r) {
            std::cout << c << ' ';
        }
        std::cout << '\n';
    }

    // Imprimir el arreglo a
    std::cout << "Arreglo a: ";
    for (int val : a) {
        std::cout << val << ' ';
    }
    std::cout << '\n';

    // Imprimir el hash
    std::cout << "Hash: " << output.substr(0, n/4) << '\n';

    return 0;
}
