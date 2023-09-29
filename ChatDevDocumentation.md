## ComposedPhase
Esta es una clase base abstracta para todas las fases compuestas. Inicializa el nombre de la fase, el número de ciclo, la composición, la configuración de todas las fases simples, la configuración de todos los roles, el tipo de modelo y la ruta del archivo de registro. También contiene métodos abstractos que deben ser implementados en las clases hijas.

## Art
Esta clase hereda de la clase ComposedPhase. No implementa ninguna funcionalidad adicional.

## CodeCompleteAll
Esta clase hereda de la clase ComposedPhase. Implementa los métodos abstractos de la clase ComposedPhase. Se utiliza para completar todo el código.

## CodeReview
Esta clase hereda de la clase ComposedPhase. Implementa los métodos abstractos de la clase ComposedPhase. Se utiliza para la revisión de código.

## HumanAgentInteraction
Esta clase hereda de la clase ComposedPhase. Implementa los métodos abstractos de la clase ComposedPhase. Se utiliza para la interacción entre humanos y agentes.

## Test
Esta clase hereda de la clase ComposedPhase. Implementa los métodos abstractos de la clase ComposedPhase. Se utiliza para pruebas.
## Codes
Esta clase se utiliza para gestionar y manipular los codebooks. Tiene varios métodos:
  - `__init__`: Inicializa la clase con los parámetros dados.
  - `_format_code`: Formatea el código dado.
  - `_update_codes`: Actualiza los códigos con el nuevo contenido generado.
  - `_rewrite_codes`: Reescribe los códigos en el directorio dado.
  - `_get_codes`: Devuelve el contenido de los codebooks.
  - `_load_from_hardware`: Carga los codebooks desde el directorio dado.
