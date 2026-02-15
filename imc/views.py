from django.shortcuts import render

def calculadora_imc(request):
    resultado = None
    error = None
    
    if request.method == 'POST':
        try:
            peso = float(request.POST.get('peso'))
            altura = float(request.POST.get('altura'))
            
            if peso <= 0:
                error = "El peso debe ser un numero positivo mayor que cero."
            elif altura <= 0:
                error = "La altura debe ser un numero positivo mayor que cero."
            else:
                imc = peso / (altura ** 2)
                
                if imc < 18.5:
                    categoria = "Bajo peso"
                elif imc < 25:
                    categoria = "Peso normal"
                elif imc < 30:
                    categoria = "Sobrepeso"
                else:
                    categoria = "Obesidad"
                
                resultado = {
                    'peso': peso,
                    'altura': altura,
                    'imc': round(imc, 2),
                    'categoria': categoria,
                }
        except ValueError:
            error = "Ingrese valores numericos validos para peso y altura."
        except Exception as e:
            error = f"Error al procesar los datos: {str(e)}"
    
    context = {
        'resultado': resultado,
        'error': error,
    }
    return render(request, 'imc/index.html', context)
