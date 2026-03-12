// Función principal que se ejecuta al cargar la página
function calcularFigura() {
    const figura = prompt("Elige una figura: \n1. Triángulo \n2. Rectángulo \n3. Cuadrado \n4. Círculo");
    const operacion = prompt("¿Qué deseas calcular? \n1. Área \n2. Perímetro");

    switch (figura) {
        case '1': // Triángulo
            if (operacion === '1') { // Área
                const base = parseFloat(prompt("Ingresa la base del triángulo:"));
                const altura = parseFloat(prompt("Ingresa la altura del triángulo:"));
                alert(`El área del triángulo es: ${(base * altura) / 2}`);
            } else if (operacion === '2') { // Perímetro
                const ladoA = parseFloat(prompt("Ingresa la medida del lado a:"));
                const ladoB = parseFloat(prompt("Ingresa la medida del lado b:"));
                const ladoC = parseFloat(prompt("Ingresa la medida del lado c:"));
                alert(`El perímetro del triángulo es: ${ladoA + ladoB + ladoC}`);
            } else {
                alert("Operación no válida.");
            }
            break;

        case '2': // Rectángulo
            const baseRect = parseFloat(prompt("Ingresa la base del rectángulo:"));
            const alturaRect = parseFloat(prompt("Ingresa la altura del rectángulo:"));
            if (operacion === '1') { // Área
                alert(`El área del rectángulo es: ${baseRect * alturaRect}`);
            } else if (operacion === '2') { // Perímetro
                alert(`El perímetro del rectángulo es: ${2 * (baseRect + alturaRect)}`);
            } else {
                alert("Operación no válida.");
            }
            break;

        case '3': // Cuadrado
            const ladoCuadrado = parseFloat(prompt("Ingresa la medida de un lado del cuadrado:"));
            if (operacion === '1') { // Área
                alert(`El área del cuadrado es: ${ladoCuadrado * ladoCuadrado}`);
            } else if (operacion === '2') { // Perímetro
                alert(`El perímetro del cuadrado es: ${4 * ladoCuadrado}`);
            } else {
                alert("Operación no válida.");
            }
            break;

        case '4': // Círculo
            const radio = parseFloat(prompt("Ingresa el radio del círculo:"));
            if (operacion === '1') { // Área
                alert(`El área del círculo es: ${Math.PI * Math.pow(radio, 2)}`);
            } else if (operacion === '2') { // Perímetro (Circunferencia) - Usando la fórmula correcta
                alert(`El perímetro del círculo es: ${2 * Math.PI * radio}`);
            } else {
                alert("Operación no válida.");
            }
            break;

        default:
            alert("Figura no válida.");
            break;
    }
}

// Llamamos a la función para que inicie el programa
calcularFigura();